# Getting Started with Blogus

This guide will help you install and set up Blogus for prompt engineering.

## Installation

### Basic Installation

To install Blogus with basic functionality:

```bash
pip install blogus
```

### Web Interface Installation

To install Blogus with web interface support:

```bash
pip install blogus[web]
```

### Development Installation

To install Blogus for development:

```bash
git clone https://github.com/terraprompt/blogus.git
cd blogus
pip install -e .
```

For web interface development:

```bash
pip install -e .[web]
```

## API Keys Setup

Logus uses LiteLLM to support a wide range of AI models. You'll need API keys for the models you want to use:

### Required Environment Variables

Set these as environment variables:

```bash
export OPENAI_API_KEY=your_openai_api_key
export ANTHROPIC_API_KEY=your_anthropic_api_key
export GROQ_API_KEY=your_groq_api_key
```

### Supported Providers

Logus supports models from:
- OpenAI (GPT models)
- Anthropic (Claude models)
- Groq (Mixtral, Llama models)
- And many more through LiteLLM

For other models supported by LiteLLM, please refer to the [LiteLLM documentation](https://docs.litellm.ai/docs/) for the required environment variables.

## Quick Start Examples

### Command Line Interface

Analyze a prompt:

```bash
blogus analyze "You are an AI assistant that helps people find information."
```

Generate a test case:

```bash
blogus test "You are an AI assistant that helps people find information."
```

Execute a prompt:

```bash
blogus execute "Explain quantum computing in simple terms."
```

### Library Usage

```python
from blogus.core import TargetLLMModel, JudgeLLMModel, analyze_prompt, execute_prompt

# Analyze a prompt
prompt = "You are a helpful assistant."
analysis = analyze_prompt(prompt, JudgeLLMModel.GPT_4)
print(f"Goal alignment: {analysis.overall_goal_alignment}/10")

# Execute a prompt
response = execute_prompt(prompt, TargetLLMModel.GPT_3_5_TURBO)
print(f"Response: {response}")
```

## Next Steps

- Learn about [Core Concepts](core_concepts.md)
- Explore the [Prompt Development Lifecycle](prompt_lifecycle.md)
- Check out the [Command Line Interface](cli.md) documentation