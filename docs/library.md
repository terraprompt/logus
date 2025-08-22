# Library Usage

Blogus can be integrated directly into your Python applications as a library.

## Installation

```bash
pip install blogus
```

For web interface features:
```bash
pip install blogus[web]
```

## Basic Usage

### Importing Modules

```python
from blogus.core import (
    TargetLLMModel,
    JudgeLLMModel,
    analyze_prompt,
    execute_prompt,
    analyze_fragments,
    generate_test,
    infer_goal,
    analyze_logs
)
```

### Simple Analysis

```python
from blogus.core import analyze_prompt, JudgeLLMModel

prompt = "You are a helpful assistant that provides concise answers."
analysis = analyze_prompt(prompt, JudgeLLMModel.GPT_4)

print(f"Goal alignment: {analysis.overall_goal_alignment}/10")
print(f"Effectiveness: {analysis.estimated_effectiveness}/10")

for suggestion in analysis.suggested_improvements:
    print(f"Suggestion: {suggestion}")
```

### Prompt Execution

```python
from blogus.core import execute_prompt, TargetLLMModel

prompt = "Explain quantum computing in simple terms."
response = execute_prompt(prompt, TargetLLMModel.GPT_4)
print(response)
```

### Fragment Analysis

```python
from blogus.core import analyze_fragments, JudgeLLMModel

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

## Advanced Usage

### Custom Goal Specification

```python
from blogus.core import analyze_prompt, JudgeLLMModel

prompt = "You are a Python tutor."
goal = "Teach Python programming concepts effectively"
analysis = analyze_prompt(prompt, JudgeLLMModel.GPT_4, goal)
```

### Test Case Generation

```python
from blogus.core import generate_test, JudgeLLMModel

prompt = "Translate the following {source_language} text to {target_language}: {text}"
test_case = generate_test(prompt, JudgeLLMModel.CLAUDE_3_OPUS)

print(f"Input: {test_case.input}")
print(f"Expected output: {test_case.expected_output}")
print(f"Goal relevance: {test_case.goal_relevance}/5")
```

### Log Generation

```python
from blogus.core import analyze_logs, JudgeLLMModel

prompt = "You are a helpful assistant."
logs = analyze_logs(prompt, JudgeLLMModel.GPT_4)

for log in logs:
    print(f"[{log.type.upper()}] {log.message}")
```

### Goal Inference

```python
from blogus.core import infer_goal, JudgeLLMModel

prompt = "You are a financial advisor who helps people plan for retirement."
inferred_goal = infer_goal(prompt, JudgeLLMModel.CLAUDE_3_OPUS)
print(f"Inferred goal: {inferred_goal}")
```

## Working with Results

### PromptAnalysis Object

```python
from blogus.core import PromptAnalysis

# The analyze_prompt function returns a PromptAnalysis object
analysis = PromptAnalysis(
    overall_goal_alignment=8,
    suggested_improvements=[
        "Add specific examples of desired response formats",
        "Include context about the target audience"
    ],
    estimated_effectiveness=7,
    inferred_goal="Help users with their queries",
    is_goal_inferred=True
)

print(f"Alignment score: {analysis.overall_goal_alignment}")
print(f"Effectiveness estimate: {analysis.estimated_effectiveness}")
print(f"Goal was inferred: {analysis.is_goal_inferred}")
if analysis.inferred_goal:
    print(f"Inferred goal: {analysis.inferred_goal}")
```

### Fragment Object

```python
from blogus.core import Fragment

# The analyze_fragments function returns a list of Fragment objects
fragment = Fragment(
    text="Always be polite and respectful.",
    type="instruction",
    goal_alignment=4,
    improvement_suggestion="Consider adding specific examples of polite interactions"
)

print(f"Fragment text: {fragment.text}")
print(f"Fragment type: {fragment.type}")
print(f"Goal alignment: {fragment.goal_alignment}/5")
print(f"Suggestion: {fragment.improvement_suggestion}")
```

### Test Object

```python
from blogus.core import Test

# The generate_test function returns a Test object
test_case = Test(
    input={
        "source_language": "English",
        "target_language": "French",
        "text": "Hello, how are you?"
    },
    expected_output="Bonjour, comment allez-vous?",
    goal_relevance=5
)

print(f"Test input: {test_case.input}")
print(f"Expected output: {test_case.expected_output}")
print(f"Goal relevance: {test_case.goal_relevance}/5")
```

## Error Handling

```python
from logus.core import analyze_prompt, JudgeLLMModel
import json

try:
    prompt = "You are a helpful assistant."
    analysis = analyze_prompt(prompt, JudgeLLMModel.GPT_4)
    # Process analysis...
except ValueError as e:
    print(f"Error parsing analysis results: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Model Selection

### Available Target Models

```python
from logus.core import TargetLLMModel

# Enum of available target models
models = list(TargetLLMModel)
for model in models:
    print(f"Target model: {model.value}")
```

### Available Judge Models

```python
from logus.core import JudgeLLMModel

# Enum of available judge models
models = list(JudgeLLMModel)
for model in models:
    print(f"Judge model: {model.value}")
```

## Integration Examples

### Batch Prompt Analysis

```python
from logus.core import analyze_prompt, JudgeLLMModel

prompts = [
    "You are a helpful assistant.",
    "You are a Python programming expert.",
    "You are a financial advisor."
]

for prompt in prompts:
    analysis = analyze_prompt(prompt, JudgeLLMModel.GPT_4)
    print(f"Prompt: {prompt}")
    print(f"  Alignment: {analysis.overall_goal_alignment}/10")
    print(f"  Effectiveness: {analysis.estimated_effectiveness}/10")
```

### Cross-Model Testing

```python
from blogus.core import analyze_prompt, JudgeLLMModel, execute_prompt, TargetLLMModel

prompt = "Explain photosynthesis."
judge_models = [JudgeLLMModel.GPT_4, JudgeLLMModel.CLAUDE_3_OPUS]
target_models = [TargetLLMModel.GPT_3_5_TURBO, TargetLLMModel.GROQ_LLAMA3_70B]

# Analyze with different judge models
for model in judge_models:
    analysis = analyze_prompt(prompt, model)
    print(f"Analysis with {model.value}:")
    print(f"  Goal alignment: {analysis.overall_goal_alignment}/10")
    print(f"  Effectiveness: {analysis.estimated_effectiveness}/10")

# Execute with different target models
for model in target_models:
    response = execute_prompt(prompt, model)
    print(f"Response from {model.value}:")
    print(f"  {response[:100]}...")
```

### Automated Test Generation

```python
from logus.core import generate_test, JudgeLLMModel

prompt_template = "Summarize the following text in {language}: {text}"
num_tests = 5

for i in range(num_tests):
    test_case = generate_test(prompt_template, JudgeLLMModel.CLAUDE_3_OPUS)
    print(f"Test case {i+1}:")
    print(f"  Input: {test_case.input}")
    print(f"  Expected: {test_case.expected_output}")
    print(f"  Relevance: {test_case.goal_relevance}/5")
    print()
```

## Best Practices

1. **Choose Appropriate Models**: Use more capable models for analysis and less expensive models for execution when possible
2. **Handle Errors Gracefully**: Always wrap Logus calls in try-except blocks
3. **Cache Results**: For repeated analysis of the same prompts, consider caching results
4. **Validate Outputs**: Always validate that the returned objects have the expected structure
5. **Use Type Hints**: Take advantage of the provided type hints for better code reliability
6. **Batch Operations**: When analyzing multiple prompts, consider batching to optimize performance

The library interface provides powerful programmatic access to all of Logus's prompt engineering capabilities.