# API Reference

This document provides detailed information about Logus's API.

## Package Structure

```
logus/
├── core.py          # Core functionality
├── cli.py           # Command-line interface
├── web.py           # Web interface
└── web_cli.py       # Web CLI entry point
```

## Core Module

The `core` module contains the fundamental prompt engineering functionality.

### Enums

#### TargetLLMModel

Enumeration of models that can be used as target models for prompt execution.

```python
from logus.core import TargetLLMModel

# Available models
TargetLLMModel.CLAUDE_3_OPUS
TargetLLMModel.CLAUDE_3_SONNET
TargetLLMModel.CLAUDE_3_HAIKU
TargetLLMModel.GPT_4
TargetLLMModel.GPT_4_TURBO
TargetLLMModel.GPT_3_5_TURBO
TargetLLMModel.GROQ_LLAMA3_70B
TargetLLMModel.GROQ_MIXTRAL_8X7B
TargetLLMModel.GROQ_GEMMA_7B
```

#### JudgeLLMModel

Enumeration of models that can be used as judge models for prompt analysis.

```python
from logus.core import JudgeLLMModel

# Available models (same as TargetLLMModel)
JudgeLLMModel.CLAUDE_3_OPUS
JudgeLLMModel.CLAUDE_3_SONNET
JudgeLLMModel.CLAUDE_3_HAIKU
JudgeLLMModel.GPT_4
JudgeLLMModel.GPT_4_TURBO
JudgeLLMModel.GPT_3_5_TURBO
JudgeLLMModel.GROQ_LLAMA3_70B
JudgeLLMModel.GROQ_MIXTRAL_8X7B
JudgeLLMModel.GROQ_GEMMA_7B
```

### Classes

#### Fragment

Represents a fragment of a prompt with analysis results.

**Attributes:**
- `text` (str): The text content of the fragment
- `type` (str): The type of fragment (instruction, context, example, or constraint)
- `goal_alignment` (int): Alignment score with the goal (1-5 scale)
- `improvement_suggestion` (str): Suggested improvements for better goal alignment

#### Log

Represents a log message generated during prompt analysis.

**Attributes:**
- `type` (str): The type of log (info, warning, or error)
- `message` (str): The log message content

#### Test

Represents a test case for evaluating prompt performance.

**Attributes:**
- `input` (Dict[str, str]): Input variables and their values for the test
- `expected_output` (str): The expected output for the given input
- `goal_relevance` (int): Relevance of the test to achieving the prompt's goal (1-5 scale)

#### PromptAnalysis

Represents a comprehensive analysis of a prompt's effectiveness.

**Attributes:**
- `overall_goal_alignment` (int): Overall alignment with the goal (1-10 scale)
- `suggested_improvements` (List[str]): List of suggested improvements
- `estimated_effectiveness` (int): Estimated effectiveness in achieving the goal (1-10 scale)
- `inferred_goal` (Optional[str]): The inferred goal if not explicitly provided
- `is_goal_inferred` (bool): Whether the goal was inferred or explicitly provided

### Functions

#### get_llm_response

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

#### infer_goal

Infer the goal of a prompt using an LLM.

```python
def infer_goal(prompt: str, model: str) -> str
```

**Parameters:**
- `prompt` (str): The prompt to analyze
- `model` (str): The judge LLM model to use for inference

**Returns:**
- `str`: The inferred goal as a string

#### analyze_fragments

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

#### analyze_logs

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

#### analyze_prompt

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

#### generate_test

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

#### execute_prompt

Execute a prompt using the specified target LLM.

```python
def execute_prompt(prompt: str, target_model: str) -> str
```

**Parameters:**
- `prompt` (str): The prompt to execute
- `target_model` (str): The target LLM model to use for execution

**Returns:**
- `str`: The response from the LLM as a string

## CLI Module

The `cli` module provides the command-line interface.

### Commands

All CLI commands are available through the `logus` command.

#### analyze

Analyze a prompt for effectiveness and alignment with a goal.

#### execute

Execute a prompt with the specified target LLM.

#### fragments

Analyze prompt fragments for goal alignment.

#### goal

Infer the goal of a prompt.

#### logs

Generate logs for a prompt.

#### test

Generate a test case for a prompt.

## Web Module

The `web` module provides the web interface through FastAPI.

### API Endpoints

#### POST /api/infer-goal

Infer the goal of a prompt.

#### POST /api/analyze-fragments

Analyze prompt fragments for goal alignment.

#### POST /api/analyze-logs

Generate logs for a prompt.

#### POST /api/analyze-prompt

Perform a comprehensive analysis of a prompt.

#### POST /api/generate-test

Generate a test case for a prompt.

#### POST /api/execute-prompt

Execute a prompt using the specified target LLM.

#### GET /

Serve the main web interface.

#### GET /agent

Serve the agent interface.

This API reference provides detailed information about using Logus programmatically.