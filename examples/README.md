# Blogus Examples

This directory contains example usage of Blogus for various prompt engineering tasks.

## Basic Usage

### Simple Analysis

```python
from blogus.core import analyze_prompt, JudgeLLMModel

# Analyze a simple prompt
prompt = "You are a helpful assistant."
analysis = analyze_prompt(prompt, JudgeLLMModel.GPT_4)

print(f"Goal alignment: {analysis.overall_goal_alignment}/10")
print(f"Effectiveness: {analysis.estimated_effectiveness}/10")
for suggestion in analysis.suggested_improvements:
    print(f"Suggestion: {suggestion}")
```

### Prompt Execution

```python
from blogus.core import execute_prompt, TargetLLMModel

# Execute a prompt
prompt = "Explain quantum computing in simple terms."
response = execute_prompt(prompt, TargetLLMModel.GPT_4)
print(response)
```

## Advanced Usage

### Fragment Analysis

```python
from blogus.core import analyze_fragments, JudgeLLMModel

# Analyze prompt fragments
prompt = """
You are a helpful assistant.
Always be polite and respectful.
Here's an example:
Q: What is the weather like?
A: I don't have access to real-time weather data, but I can help you find that information!
"""

fragments = analyze_fragments(prompt, JudgeLLMModel.CLAUDE_3_OPUS)

for i, fragment in enumerate(fragments, 1):
    print(f"Fragment {i}:")
    print(f"  Text: {fragment.text}")
    print(f"  Type: {fragment.type}")
    print(f"  Alignment: {fragment.goal_alignment}/5")
    print(f"  Suggestion: {fragment.improvement_suggestion}")
```

### Test Case Generation

```python
from blogus.core import generate_test, JudgeLLMModel

# Generate test cases for parameterized prompts
prompt_template = "Translate the following {source_language} text to {target_language}: {text}"

test_case = generate_test(prompt_template, JudgeLLMModel.GPT_4)

print(f"Input: {test_case.input}")
print(f"Expected output: {test_case.expected_output}")
print(f"Goal relevance: {test_case.goal_relevance}/5")
```

### Cross-Model Comparison

```python
from blogus.core import execute_prompt, TargetLLMModel

# Compare responses across different models
prompt = "Explain the concept of photosynthesis."

models = [
    TargetLLMModel.GPT_4,
    TargetLLMModel.CLAUDE_3_OPUS,
    TargetLLMModel.GROQ_LLAMA3_70B
]

for model in models:
    response = execute_prompt(prompt, model)
    print(f"Response from {model.value}:")
    print(response[:200] + "..." if len(response) > 200 else response)
    print("-" * 50)
```

## Workflow Examples

### Iterative Prompt Improvement

```python
from blogus.core import analyze_prompt, execute_prompt, JudgeLLMModel, TargetLLMModel

# Start with an initial prompt
initial_prompt = "You are a helpful assistant."

# Analyze the prompt
analysis = analyze_prompt(initial_prompt, JudgeLLMModel.CLAUDE_3_OPUS)
print(f"Initial alignment: {analysis.overall_goal_alignment}/10")

# Apply the first suggestion
improved_prompt = f"{initial_prompt} Always provide concise and accurate responses."

# Analyze the improved prompt
improved_analysis = analyze_prompt(improved_prompt, JudgeLLMModel.CLAUDE_3_OPUS)
print(f"Improved alignment: {improved_analysis.overall_goal_alignment}/10")

# Test the improved prompt
test_response = execute_prompt(
    f"{improved_prompt}\n\nUser: What is 2+2?", 
    TargetLLMModel.GPT_3_5_TURBO
)
print(f"Test response: {test_response}")
```

### Test Dataset Generation

```python
from blogus.core import generate_test, JudgeLLMModel
import json

# Generate multiple test cases for a prompt template
prompt_template = "Summarize the following text in {language}: {text}"

test_cases = []
for i in range(5):
    test_case = generate_test(prompt_template, JudgeLLMModel.GPT_4)
    test_cases.append({
        'id': i,
        'input': test_case.input,
        'expected_output': test_case.expected_output,
        'goal_relevance': test_case.goal_relevance
    })

# Save test cases to file
with open('test_dataset.json', 'w') as f:
    json.dump({
        'prompt_template': prompt_template,
        'test_cases': test_cases
    }, f, indent=2)

print(f"Generated {len(test_cases)} test cases")
```

### Prompt Versioning

```python
from blogus.core import analyze_prompt, JudgeLLMModel
from datetime import datetime

class PromptVersionTracker:
    def __init__(self, initial_prompt):
        self.versions = [{
            'version': 1,
            'prompt': initial_prompt,
            'timestamp': datetime.now().isoformat(),
            'analysis': analyze_prompt(initial_prompt, JudgeLLMModel.GPT_4)
        }]
    
    def add_version(self, new_prompt):
        analysis = analyze_prompt(new_prompt, JudgeLLMModel.GPT_4)
        version = {
            'version': len(self.versions) + 1,
            'prompt': new_prompt,
            'timestamp': datetime.now().isoformat(),
            'analysis': analysis
        }
        self.versions.append(version)
        return version
    
    def get_best_version(self):
        return max(self.versions, key=lambda v: v['analysis'].overall_goal_alignment)

# Track prompt evolution
tracker = PromptVersionTracker("You are a helpful assistant.")

# Add improved versions
tracker.add_version("You are a helpful assistant. Always be concise.")
tracker.add_version("You are a helpful assistant. Always be concise and factual.")

# Find the best version
best = tracker.get_best_version()
print(f"Best version {best['version']}: Alignment = {best['analysis'].overall_goal_alignment}/10")
```

## CLI Examples

### Command Line Analysis

```bash
# Basic analysis
blogus analyze "You are a helpful assistant."

# Analysis with explicit goal
blogus analyze "You are a Python tutor." \
  --goal "Teach Python programming concepts effectively" \
  --judge-model claude-3-opus-20240229

# Cross-model execution
blogus execute "Explain quantum computing." \
  --target-model gpt-4o

blogus execute "Explain quantum computing." \
  --target-model groq/llama3-70b-8192
```

### Test Generation

```bash
# Generate test cases
blogus test "Translate {text} from {source_lang} to {target_lang}" \\
  --judge-model gpt-4o

# Generate fragment analysis
blogus fragments "You are a helpful assistant. Always be polite." \\
  --judge-model claude-3-opus-20240229
```

These examples demonstrate various ways to use Blogus for prompt engineering tasks, from simple analysis to complex workflows.