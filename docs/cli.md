# Command Line Interface

Blogus provides a comprehensive command-line interface for prompt engineering tasks.

## Overview

The `blogus` command provides access to all core prompt engineering functionality:

```bash
blogus [OPTIONS] COMMAND [ARGS]...
```

## Commands

### analyze

Analyze a prompt for effectiveness and alignment with a goal.

```bash
blogus analyze [OPTIONS] PROMPT
```

Options:
- `--target-model`: Target LLM model for prompt execution
- `--judge-model`: Judge LLM model for analysis
- `--goal`: Explicit goal for the prompt (will be inferred if not provided)

Example:
```bash
blogus analyze "You are a helpful assistant." \
  --judge-model gpt-4o \
  --goal "Provide helpful responses to user queries"
```

### execute

Execute a prompt with the specified target LLM.

```bash
blogus execute [OPTIONS] PROMPT
```

Options:
- `--target-model`: Target LLM model to use for execution

Example:
```bash
blogus execute "Explain quantum computing in simple terms." \\
  --target-model claude-3-opus-20240229
```

### fragments

Analyze prompt fragments for goal alignment.

```bash
blogus fragments [OPTIONS] PROMPT
```

Options:
- `--target-model`: Target LLM model for prompt execution
- `--judge-model`: Judge LLM model for analysis
- `--goal`: Explicit goal for the prompt (will be inferred if not provided)

Example:
```bash
blogus fragments "You are a helpful assistant. Always be polite." 
  --judge-model gpt-4o
```

### goal

Infer the goal of a prompt.

```bash
blogus goal [OPTIONS] PROMPT
```

Options:
- `--judge-model`: Judge LLM model for analysis

Example:
```bash
blogus goal "You are a Python programming tutor."
```

### logs

Generate logs for a prompt.

```bash
blogus logs [OPTIONS] PROMPT
```

Options:
- `--target-model`: Target LLM model for prompt execution
- `--judge-model`: Judge LLM model for analysis
- `--goal`: Explicit goal for the prompt (will be inferred if not provided)

Example:
```bash
blogus logs "You are a helpful assistant." 
  --judge-model claude-3-opus-20240229
```

### test

Generate a test case for a prompt.

```bash
blogus test [OPTIONS] PROMPT
```

Options:
- `--target-model`: Target LLM model for prompt execution
- `--judge-model`: Judge LLM model for test generation
- `--goal`: Explicit goal for the prompt (will be inferred if not provided)

Example:
```bash
blogus test "Translate English to French: {text}" 
  --judge-model gpt-4o
```

## Global Options

- `--help`: Show help message and exit

## Model Selection

Blogus supports a wide range of models through LiteLLM:

### Target Models
- `gpt-4o`: OpenAI's GPT-4o
- `gpt-4-turbo`: OpenAI's GPT-4 Turbo
- `gpt-3.5-turbo`: OpenAI's GPT-3.5 Turbo
- `claude-3-opus-20240229`: Anthropic's Claude 3 Opus
- `claude-3-sonnet-20240229`: Anthropic's Claude 3 Sonnet
- `claude-3-haiku-20240307`: Anthropic's Claude 3 Haiku
- `groq/llama3-70b-8192`: Groq's Llama 3 70B
- `groq/mixtral-8x7b-32768`: Groq's Mixtral 8x7B
- `groq/gemma-7b-it`: Groq's Gemma 7B

### Judge Models
Same as target models - choose based on analysis needs rather than cost.

## Workflow Examples

### Basic Analysis and Execution

```bash
# Analyze a prompt
blogus analyze "You are an AI assistant that helps with coding questions."

# Execute the prompt
blogus execute "You are an AI assistant that helps with coding questions."
```

### Test Generation
```bash
# Generate a test for a variable-based prompt
blogus test "Summarize the following text in {language}: {text}" \\
  --judge-model gpt-4o
```

### Fragment Analysis
```bash
# Get detailed fragment analysis
blogus fragments "You are a helpful assistant. Always respond politely. Here's an example: Q: Hello! A: Hi there!" \\
  --judge-model claude-3-opus-20240229
```

The CLI provides a powerful way to integrate prompt engineering into your development workflow.