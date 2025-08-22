# Core Module API

This document provides detailed API documentation for the `logus.core` module.

## Module Overview

The `core` module contains the fundamental prompt engineering functionality of Logus.

```python
from logus import core
```

## Enums

### TargetLLMModel

Enumeration of models that can be used as target models for prompt execution.

**Members:**
- `CLAUDE_3_OPUS`: `claude-3-opus-20240229`
- `CLAUDE_3_SONNET`: `claude-3-sonnet-20240229`
- `CLAUDE_3_HAIKU`: `claude-3-haiku-20240307`
- `GPT_4`: `gpt-4o`
- `GPT_4_TURBO`: `gpt-4-turbo`
- `GPT_3_5_TURBO`: `gpt-3.5-turbo`
- `GROQ_LLAMA3_70B`: `groq/llama3-70b-8192`
- `GROQ_MIXTRAL_8X7B`: `groq/mixtral-8x7b-32768`
- `GROQ_GEMMA_7B`: `groq/gemma-7b-it`

### JudgeLLMModel

Enumeration of models that can be used as judge models for prompt analysis.

**Members:**
- `CLAUDE_3_OPUS`: `claude-3-opus-20240229`
- `CLAUDE_3_SONNET`: `claude-3-sonnet-20240229`
- `CLAUDE_3_HAIKU`: `claude-3-haiku-20240307`
- `GPT_4`: `gpt-4o`
- `GPT_4_TURBO`: `gpt-4-turbo`
- `GPT_3_5_TURBO`: `gpt-3.5-turbo`
- `GROQ_LLAMA3_70B`: `groq/llama3-70b-8192`
- `GROQ_MIXTRAL_8X7B`: `groq/mixtral-8x7b-32768`
- `GROQ_GEMMA_7B`: `groq/gemma-7b-it`

## Classes

### Fragment

Represents a fragment of a prompt with analysis results.

```python
class Fragment:
    def __init__(
        self, text: str, type: str, goal_alignment: int, improvement_suggestion: str
    )
```

**Parameters:**
- `text` (str): The text content of the fragment
- `type` (str): The type of fragment (instruction, context, example, or constraint)
- `goal_alignment` (int): Alignment score with the goal (1-5 scale)
- `improvement_suggestion` (str): Suggested improvements for better goal alignment

**Attributes:**
- `text` (str): The text content of the fragment
- `type` (str): The type of fragment
- `goal_alignment` (int): Alignment score with the goal
- `improvement_suggestion` (str): Suggested improvements

### Log

Represents a log message generated during prompt analysis.

```python
class Log:
    def __init__(self, type: str, message: str)
```

**Parameters:**
- `type` (str): The type of log (info, warning, or error)
- `message` (str): The log message content

**Attributes:**
- `type` (str): The type of log
- `message` (str): The log message content

### Test

Represents a test case for evaluating prompt performance.

```python
class Test:
    def __init__(
        self, input: Dict[str, str], expected_output: str, goal_relevance: int
    )
```

**Parameters:**
- `input` (Dict[str, str]): Input variables and their values for the test
- `expected_output` (str): The expected output for the given input
- `goal_relevance` (int): Relevance of the test to achieving the prompt's goal (1-5 scale)

**Attributes:**
- `input` (Dict[str, str]): Input variables and their values
- `expected_output` (str): The expected output
- `goal_relevance` (int): Relevance score

### PromptAnalysis

Represents a comprehensive analysis of a prompt's effectiveness.

```python
class PromptAnalysis:
    def __init__(
        self,
        overall_goal_alignment: int,
        suggested_improvements: List[str],
        estimated_effectiveness: int,
        inferred_goal: Optional[str] = None,
        is_goal_inferred: bool = False,
    )
```

**Parameters:**
- `overall_goal_alignment` (int): Overall alignment with the goal (1-10 scale)
- `suggested_improvements` (List[str]): List of suggested improvements
- `estimated_effectiveness` (int): Estimated effectiveness in achieving the goal (1-10 scale)
- `inferred_goal` (Optional[str], optional): The inferred goal if not explicitly provided
- `is_goal_inferred` (bool, optional): Whether the goal was inferred or explicitly provided

**Attributes:**
- `overall_goal_alignment` (int): Overall alignment score
- `suggested_improvements` (List[str]): Improvement suggestions
- `estimated_effectiveness` (int): Effectiveness estimate
- `inferred_goal` (Optional[str]): Inferred goal
- `is_goal_inferred` (bool): Whether goal was inferred

## Functions

### get_llm_response

Get a response from the specified LLM using LiteLLM.

```python
def get_llm_response(model: str, prompt: str, max_tokens: int = 1000) -> str
```

**Parameters:**
- `model` (str): The LLM model to use
- `prompt` (str): The prompt to send to the model
- `max_tokens` (int, optional): Maximum number of tokens to generate. Defaults to 1000.

**Returns:**
- `str`: The response from the LLM as a string

**Example:**
```python
response = get_llm_response("gpt-4o", "Explain quantum computing")
```

### infer_goal

Infer the goal of a prompt using an LLM.

```python
def infer_goal(prompt: str, model: str) -> str
```

**Parameters:**
- `prompt` (str): The prompt to analyze
- `model` (str): The judge LLM model to use for inference

**Returns:**
- `str`: The inferred goal as a string

**Example:**
```python
goal = infer_goal("You are a Python tutor", "gpt-4o")
```

### analyze_fragments

Analyze prompt fragments for goal alignment.

```python
def analyze_fragments(
    prompt: str, judge_model: str, goal: Optional[str] = None
) -> List[Fragment]
```

**Parameters:**
- `prompt` (str): The prompt to analyze
- `judge_model` (str): The judge LLM model to use for analysis
- `goal` (Optional[str], optional): The goal of the prompt. Defaults to None.

**Returns:**
- `List[Fragment]`: A list of Fragment objects with analysis results

**Raises:**
- `ValueError`: If the judge model response cannot be parsed as valid JSON

**Example:**
```python
fragments = analyze_fragments(
    "You are a helpful assistant. Always be polite.",
    "gpt-4o"
)
```

### analyze_logs

Analyze prompt for potential issues and generate logs.

```python
def analyze_logs(
    prompt: str, judge_model: str, goal: Optional[str] = None
) -> List[Log]
```

**Parameters:**
- `prompt` (str): The prompt to analyze
- `judge_model` (str): The judge LLM model to use for analysis
- `goal` (Optional[str], optional): The goal of the prompt. Defaults to None.

**Returns:**
- `List[Log]`: A list of Log objects with analysis results

**Raises:**
- `ValueError`: If the judge model response cannot be parsed as valid JSON

**Example:**
```python
logs = analyze_logs("You are a helpful assistant.", "gpt-4o")
```

### analyze_prompt

Perform a comprehensive analysis of a prompt.

```python
def analyze_prompt(
    prompt: str, judge_model: str, goal: Optional[str] = None
) -> PromptAnalysis
```

**Parameters:**
- `prompt` (str): The prompt to analyze
- `judge_model` (str): The judge LLM model to use for analysis
- `goal` (Optional[str], optional): The goal of the prompt. Defaults to None.

**Returns:**
- `PromptAnalysis`: A PromptAnalysis object with analysis results

**Raises:**
- `ValueError`: If the judge model response cannot be parsed as valid JSON

**Example:**
```python
analysis = analyze_prompt(
    "You are a helpful assistant.",
    "gpt-4o"
)
```

### generate_test

Generate a test case for a prompt.

```python
def generate_test(
    prompt: str, judge_model: str, goal: Optional[str] = None
) -> Test
```

**Parameters:**
- `prompt` (str): The prompt to generate a test for
- `judge_model` (str): The judge LLM model to use for test generation
- `goal` (Optional[str], optional): The goal of the prompt. Defaults to None.

**Returns:**
- `Test`: A Test object with the generated test case

**Raises:**
- `ValueError`: If the judge model response cannot be parsed as valid JSON

**Example:**
```python
test_case = generate_test(
    "Translate {text} to French",
    "gpt-4o"
)
```

### execute_prompt

Execute a prompt using the specified target LLM.

```python
def execute_prompt(prompt: str, target_model: str) -> str
```

**Parameters:**
- `prompt` (str): The prompt to execute
- `target_model` (str): The target LLM model to use for execution

**Returns:**
- `str`: The response from the LLM as a string

**Example:**
```python
response = execute_prompt(
    "Explain quantum computing",
    "gpt-4o"
)
```