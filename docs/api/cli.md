# CLI Module API

This document provides detailed API documentation for the `logus.cli` module.

## Module Overview

The `cli` module provides the command-line interface for Logus using Click.

```python
from logus import cli
```

## CLI Group

### cli

Main CLI group for Logus commands.

```python
@click.group()
def cli()
```

**Description:**
The main entry point for all Logus CLI commands.

## Commands

### analyze

Analyze a prompt for effectiveness and alignment with a goal.

```python
@click.command()
@click.argument("prompt", type=str)
@click.option("--target-model", type=click.Choice([m.value for m in TargetLLMModel]), default=TargetLLMModel.GPT_4, help="Target LLM model to use for prompt execution")
@click.option("--judge-model", type=click.Choice([m.value for m in JudgeLLMModel]), default=JudgeLLMModel.GPT_4, help="Judge LLM model to use for analysis")
@click.option("--goal", type=str, default=None, help="Goal for the prompt (will be inferred if not provided)")
def analyze(prompt, target_model, judge_model, goal)
```

**Parameters:**
- `prompt` (str): The prompt to analyze
- `--target-model` (str): Target LLM model to use for prompt execution
- `--judge-model` (str): Judge LLM model to use for analysis
- `--goal` (str, optional): Goal for the prompt. Will be inferred if not provided

**Example:**
```bash
logus analyze "You are a helpful assistant." \
  --judge-model claude-3-opus-20240229 \
  --goal "Provide helpful responses"
```

### execute

Execute a prompt with the specified target LLM.

```python
@click.command()
@click.argument("prompt", type=str)
@click.option("--target-model", type=click.Choice([m.value for m in TargetLLMModel]), default=TargetLLMModel.GPT_4, help="Target LLM model to use for execution")
def execute(prompt, target_model)
```

**Parameters:**
- `prompt` (str): The prompt to execute
- `--target-model` (str): Target LLM model to use for execution

**Example:**
```bash
logus execute "Explain quantum computing" \
  --target-model gpt-4o
```

### fragments

Analyze prompt fragments for goal alignment.

```python
@click.command()
@click.argument("prompt", type=str)
@click.option("--target-model", type=click.Choice([m.value for m in TargetLLMModel]), default=TargetLLMModel.GPT_4, help="Target LLM model to use for prompt execution")
@click.option("--judge-model", type=click.Choice([m.value for m in JudgeLLMModel]), default=JudgeLLMModel.GPT_4, help="Judge LLM model to use for analysis")
@click.option("--goal", type=str, default=None, help="Goal for the prompt (will be inferred if not provided)")
def fragments(prompt, target_model, judge_model, goal)
```

**Parameters:**
- `prompt` (str): The prompt to analyze
- `--target-model` (str): Target LLM model to use for prompt execution
- `--judge-model` (str): Judge LLM model to use for analysis
- `--goal` (str, optional): Goal for the prompt. Will be inferred if not provided

**Example:**
```bash
logus fragments "You are a helpful assistant. Always be polite." \
  --judge-model gpt-4o
```

### goal

Infer the goal of a prompt.

```python
@click.command()
@click.argument("prompt", type=str)
@click.option("--judge-model", type=click.Choice([m.value for m in JudgeLLMModel]), default=JudgeLLMModel.GPT_4, help="Judge LLM model to use for analysis")
def goal(prompt, judge_model)
```

**Parameters:**
- `prompt` (str): The prompt to analyze
- `--judge-model` (str): Judge LLM model to use for inference

**Example:**
```bash
logus goal "You are a Python programming tutor"
```

### logs

Generate logs for a prompt.

```python
@click.command()
@click.argument("prompt", type=str)
@click.option("--target-model", type=click.Choice([m.value for m in TargetLLMModel]), default=TargetLLMModel.GPT_4, help="Target LLM model to use for prompt execution")
@click.option("--judge-model", type=click.Choice([m.value for m in JudgeLLMModel]), default=JudgeLLMModel.GPT_4, help="Judge LLM model to use for analysis")
@click.option("--goal", type=str, default=None, help="Goal for the prompt (will be inferred if not provided)")
def logs(prompt, target_model, judge_model, goal)
```

**Parameters:**
- `prompt` (str): The prompt to analyze
- `--target-model` (str): Target LLM model to use for prompt execution
- `--judge-model` (str): Judge LLM model to use for analysis
- `--goal` (str, optional): Goal for the prompt. Will be inferred if not provided

**Example:**
```bash
logus logs "You are a helpful assistant." \
  --judge-model claude-3-opus-20240229
```

### test

Generate a test case for a prompt.

```python
@click.command()
@click.argument("prompt", type=str)
@click.option("--target-model", type=click.Choice([m.value for m in TargetLLMModel]), default=TargetLLMModel.GPT_4, help="Target LLM model to use for prompt execution")
@click.option("--judge-model", type=click.Choice([m.value for m in JudgeLLMModel]), default=JudgeLLMModel.GPT_4, help="Judge LLM model to use for test generation")
@click.option("--goal", type=str, default=None, help="Goal for the prompt (will be inferred if not provided)")
def test(prompt, target_model, judge_model, goal)
```

**Parameters:**
- `prompt` (str): The prompt to generate a test for
- `--target-model` (str): Target LLM model to use for prompt execution
- `--judge-model` (str): Judge LLM model to use for test generation
- `--goal` (str, optional): Goal for the prompt. Will be inferred if not provided

**Example:**
```bash
logus test "Translate {text} to French" \
  --judge-model gpt-4o
```

## Usage Examples

### Basic Analysis
```bash
logus analyze "You are an AI assistant that helps with coding questions."
```

### Cross-Model Testing
```bash
# Analyze with a powerful judge model
logus analyze "Explain photosynthesis." \
  --judge-model claude-3-opus-20240229

# Execute with different target models
logus execute "Explain photosynthesis." \
  --target-model gpt-4o

logus execute "Explain photosynthesis." \
  --target-model groq/llama3-70b-8192
```

### Test Generation
```bash
# Generate a test for a variable-based prompt
logus test "Summarize the following text in {language}: {text}" \
  --judge-model gpt-4o
```

The CLI module provides a powerful command-line interface for all prompt engineering tasks.