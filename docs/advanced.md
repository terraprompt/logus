# Advanced Features

Blogus provides several advanced features for sophisticated prompt engineering workflows.

## Batch Processing

Process multiple prompts simultaneously for efficiency:

```python
from blogus.core import analyze_prompt, JudgeLLMModel
import asyncio

async def batch_analyze_prompts(prompts, judge_model):
    """Analyze multiple prompts concurrently."""
    tasks = [
        asyncio.create_task(analyze_prompt_async(prompt, judge_model))
        for prompt in prompts
    ]
    return await asyncio.gather(*tasks)

def analyze_prompt_async(prompt, judge_model):
    """Wrapper for async analysis."""
    # This would need to be implemented with async LLM calls
    # For now, we'll simulate with regular calls
    return analyze_prompt(prompt, judge_model)

# Example usage
prompts = [
    "You are a helpful assistant.",
    "You are a Python programming expert.",
    "You are a financial advisor."
]

# In an async context:
# results = await batch_analyze_prompts(prompts, JudgeLLMModel.GPT_4)
```

## Custom Analysis Prompts

Create your own analysis workflows using the underlying `get_llm_response` function:

```python
from blogus.core import get_llm_response, JudgeLLMModel

def custom_prompt_analysis(prompt, judge_model):
    """Custom analysis with a specific focus."""
    analysis_prompt = f"""
Analyze the following prompt for bias and fairness:

Prompt: {prompt}
"""
    return get_llm_response(analysis_prompt, judge_model)
```

## Prompt Templates and Variables

Work with parameterized prompts effectively:

```python
from logus.core import generate_test, JudgeLLMModel
import re

def extract_variables(prompt_template):
    \"\"\"Extract variables from a prompt template.\"\"\"
    return re.findall(r"\\{([^}]+)\\}", prompt_template)

def generate_multiple_tests(prompt_template, judge_model, num_tests=3):
    \"\"\"Generate multiple test cases for a template.\"\"\"
    variables = extract_variables(prompt_template)
    print(f"Found variables: {variables}")
    
    test_cases = []
    for i in range(num_tests):
        test_case = generate_test(prompt_template, judge_model)
        test_cases.append(test_case)
    
    return test_cases

# Usage
template = "Translate the following {source_language} text to {target_language}: {text}"
test_cases = generate_multiple_tests(template, JudgeLLMModel.GPT_4, 5)

for i, test_case in enumerate(test_cases, 1):
    print(f"Test case {i}: {test_case.input}")
```

## Cross-Model Comparison Framework

Create systematic comparisons across multiple models:

```python
from blogus.core import execute_prompt, TargetLLMModel
from typing import Dict, List

class ModelComparison:
    def __init__(self, target_models: List[TargetLLMModel]):
        self.target_models = target_models
    
    def compare_execution(self, prompt: str) -> Dict[str, str]:
        """Execute prompt on all target models and collect responses."""
        results = {}
        for model in self.target_models:
            try:
                response = execute_prompt(prompt, model)
                results[model.value] = response
            except Exception as e:
                results[model.value] = f"Error: {str(e)}"
        return results
    
    def compare_consistency(self, prompt: str, test_cases: List[Dict]) -> Dict:
        """Test consistency across models with multiple test cases."""
        consistency_results = {}
        
        for model in self.target_models:
            model_results = []
            for test_case in test_cases:
                # This would require a more complex implementation
                # to substitute variables in the prompt
                pass
            consistency_results[model.value] = model_results
            
        return consistency_results

# Usage
models = [
    TargetLLMModel.GPT_4,
    TargetLLMModel.CLAUDE_3_OPUS,
    TargetLLMModel.GROQ_LLAMA3_70B
]

comparator = ModelComparison(models)
results = comparator.compare_execution("Explain photosynthesis.")
```

## Automated Prompt Evolution

Implement evolutionary algorithms for prompt optimization:

```python
from blogus.core import analyze_prompt, JudgeLLMModel, get_llm_response
import random

class PromptEvolver:
    def __init__(self, judge_model: str):
        self.judge_model = judge_model
    
    def mutate_prompt(self, prompt: str) -> str:
        """Apply random mutations to a prompt."""
        mutation_prompt = f"""
Take the following prompt and make a small, beneficial modification:

Original prompt: {prompt}

Modified prompt:
"""
        return get_llm_response(mutation_prompt, self.judge_model)
    
    def evolve_prompt(self, initial_prompt: str, generations: int = 10) -> str:
        """Evolve a prompt over multiple generations."""
        current_prompt = initial_prompt
        
        for generation in range(generations):
            # Analyze current prompt
            analysis = analyze_prompt(current_prompt, self.judge_model)
            
            # If score is high enough, stop evolving
            if analysis.overall_goal_alignment >= 9:
                break
                
            # Mutate the prompt
            mutated_prompt = self.mutate_prompt(current_prompt)
            
            # Compare scores
            mutated_analysis = analyze_prompt(mutated_prompt, self.judge_model)
            
            if mutated_analysis.overall_goal_alignment > analysis.overall_goal_alignment:
                current_prompt = mutated_prompt
                print(f"Generation {generation + 1}: Improved to {mutated_analysis.overall_goal_alignment}/10")
            else:
                print(f"Generation {generation + 1}: No improvement ({analysis.overall_goal_alignment}/10)")
        
        return current_prompt

# Usage
evolver = PromptEvolver(JudgeLLMModel.GPT_4)
optimized_prompt = evolver.evolve_prompt("You are a helpful assistant.")
```

## Test Dataset Management

Create and manage comprehensive test datasets:

```python
from logus.core import generate_test, JudgeLLMModel
from typing import List, Dict
import json

class TestDataset:
    def __init__(self, prompt_template: str):
        self.prompt_template = prompt_template
        self.test_cases = []
    
    def generate_test_cases(self, judge_model: str, num_cases: int = 10):
        \"\"\"Generate multiple test cases.\"\"\"
        for i in range(num_cases):
            try:
                test_case = generate_test(self.prompt_template, judge_model)
                self.test_cases.append({
                    'id': i,
                    'input': test_case.input,
                    'expected_output': test_case.expected_output,
                    'goal_relevance': test_case.goal_relevance
                })
            except Exception as e:
                print(f"Failed to generate test case {i}: {e}")
    
    def save_to_file(self, filename: str):
        \"\"\"Save test dataset to JSON file.\"\"\"
        dataset = {
            'prompt_template': self.prompt_template,
            'test_cases': self.test_cases
        }
        with open(filename, 'w') as f:
            json.dump(dataset, f, indent=2)
    
    def load_from_file(self, filename: str):
        \"\"\"Load test dataset from JSON file.\"\"\"
        with open(filename, 'r') as f:
            dataset = json.load(f)
        self.prompt_template = dataset['prompt_template']
        self.test_cases = dataset['test_cases']

# Usage
dataset = TestDataset("Translate {text} from {source_lang} to {target_lang}")
dataset.generate_test_cases(JudgeLLMModel.GPT_4, 20)
dataset.save_to_file("translation_tests.json")
```

## Prompt Versioning and Tracking

Implement version control for prompt evolution:

```python
from datetime import datetime
from typing import List, Dict
import hashlib

class PromptVersion:
    def __init__(self, prompt: str, goal: str = None, metadata: Dict = None):
        self.prompt = prompt
        self.goal = goal
        self.metadata = metadata or {}
        self.timestamp = datetime.now()
        self.version_hash = self._compute_hash()
    
    def _compute_hash(self) -> str:
        \"\"\"Compute a hash of the prompt content.\"\"\"
        content = f"{self.prompt}|{self.goal}|{sorted(self.metadata.items())}"
        return hashlib.md5(content.encode()).hexdigest()

class PromptTracker:
    def __init__(self, initial_prompt: str, initial_goal: str = None):
        self.versions: List[PromptVersion] = []
        initial_version = PromptVersion(initial_prompt, initial_goal)
        self.versions.append(initial_version)
        self.current_version = 0
    
    def update_prompt(self, new_prompt: str, new_goal: str = None, metadata: Dict = None):
        \"\"\"Add a new version of the prompt.\"\"\"
        new_version = PromptVersion(new_prompt, new_goal, metadata)
        
        # Check if this is actually a new version
        if new_version.version_hash != self.versions[-1].version_hash:
            self.versions.append(new_version)
            self.current_version = len(self.versions) - 1
            return True
        return False
    
    def get_version(self, version_index: int = None) -> PromptVersion:
        \"\"\"Get a specific version of the prompt.\"\"\"
        if version_index is None:
            version_index = self.current_version
        return self.versions[version_index]
    
    def get_changelog(self) -> List[Dict]:
        \"\"\"Get a changelog of all versions.\"\"\"
        changelog = []
        for i, version in enumerate(self.versions):
            changelog.append({
                'version': i,
                'timestamp': version.timestamp.isoformat(),
                'hash': version.version_hash,
                'is_current': i == self.current_version
            })
        return changelog

# Usage
tracker = PromptTracker(
    "You are a helpful assistant.",
    "Provide helpful responses to user queries"
)

# After making improvements
tracker.update_prompt(
    "You are a helpful assistant. Always be concise and accurate in your responses.",
    "Provide helpful, concise, and accurate responses to user queries",
    {'improvement_reason': 'Added conciseness requirement'}
)

print(f"Current version: {tracker.current_version}")
print(f"Total versions: {len(tracker.versions)}")
```

## Integration with CI/CD Pipelines

Use Logus in automated testing pipelines:

```python
from logus.core import analyze_prompt, execute_prompt, JudgeLLMModel, TargetLLMModel
import sys

def run_prompt_tests(prompt_file: str, threshold: int = 7) -> bool:
    \"\"\"Run automated tests on a prompt.\"\"\"
    with open(prompt_file, 'r') as f:
        prompt = f.read()
    
    # Analyze prompt quality
    analysis = analyze_prompt(prompt, JudgeLLMModel.GPT_4)
    
    print(f"Prompt alignment score: {analysis.overall_goal_alignment}/10")
    print(f"Estimated effectiveness: {analysis.estimated_effectiveness}/10")
    
    # Check if prompt meets quality threshold
    if analysis.overall_goal_alignment < threshold:
        print(f"Prompt quality below threshold of {threshold}")
        return False
    
    # Execute a basic test
    test_input = "Hello, how are you?"
    response = execute_prompt(f"{prompt}\n\nUser: {test_input}", TargetLLMModel.GPT_3_5_TURBO)
    
    print(f"Test response: {response[:100]}...")
    
    # Additional validation logic would go here
    
    return True

# Usage in CI/CD
if __name__ == "__main__":
    prompt_file = sys.argv[1] if len(sys.argv) > 1 else "prompt.txt"
    success = run_prompt_tests(prompt_file)
    sys.exit(0 if success else 1)
```

These advanced features enable sophisticated prompt engineering workflows and can be combined in various ways to create powerful automation systems.