# Logus: Craft, Analyze, and Perfect Your AI Prompts

![Logus Logo](https://via.placeholder.com/150?text=Logus)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/logus.svg)](https://badge.fury.io/py/logus)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

## Why Logus?

In the rapidly evolving field of AI and large language models, crafting effective prompts has become a crucial skill. Logus is born out of the need for a sophisticated, user-friendly tool that empowers developers, researchers, and AI enthusiasts to:

- Analyze and refine prompts in real-time
- Generate and manage test cases
- Execute prompts across multiple AI models
- Visualize and understand prompt effectiveness

Whether you're a seasoned prompt engineer or just starting your journey with AI, Logus provides the tools you need to elevate your prompt crafting skills.

## What is Logus?

Logus is an advanced prompt engineering tool available as:
1. **A Python library** for programmatic use in your applications
2. **A command-line interface** for quick analysis and testing
3. **A web interface** with an intuitive frontend for interactive prompt engineering

Key features include:

- **Real-time Prompt Analysis**: Get instant feedback on your prompts' effectiveness and alignment with your goals.
- **Multi-model Support**: Test your prompts across various AI models, including GPT-4, Claude, and more.
- **Test Case Generation**: Automatically generate relevant test cases for your prompts.
- **Interactive Code Editor**: A feature-rich editor with syntax highlighting and real-time analysis feedback (in web UI).
- **Execution Environment**: Run your prompts and see the results immediately.
- **Test Case Management**: Store and download generated test cases as JSON files (in web UI).
- **Dynamic Goal Inference**: Automatically infer the goal of your prompt if not provided.

## Installation

```bash
pip install logus
```

For web interface support, install with the web extra:
```bash
pip install logus[web]
```

## Usage

### As a Library

```python
from logus.core import LLMModel, analyze_prompt, generate_test

prompt = "You are an AI assistant that helps people find information..."

# Analyze a prompt
analysis = analyze_prompt(prompt, LLMModel.GPT_4)
print(f"Goal alignment: {analysis.overall_goal_alignment}/10")

# Generate a test case
test_case = generate_test(prompt, LLMModel.GPT_4)
```

### Command Line Interface

```bash
# Analyze a prompt
logus analyze "You are an AI assistant that helps people find information..."

# Generate a test case
logus test "You are an AI assistant that helps people find information..."

# See all available commands
logus --help
```

### Web Interface

To run the web interface:
```bash
logus-web  # If installed with web extras
# or
python -m logus.web
```

Then navigate to `http://localhost:8000` in your browser.

## API Keys

Logus requires API keys for the AI models you want to use:

- OpenAI API key for GPT models
- Anthropic API key for Claude models
- Groq API key for Mixtral models

Set these as environment variables:
```bash
export OPENAI_API_KEY=your_openai_api_key
export ANTHROPIC_API_KEY=your_anthropic_api_key
export GROQ_API_KEY=your_groq_api_key
```

## Contributing

We welcome contributions to Logus! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to get started.

## License

Logus is open-source software licensed under the MIT license. See the [LICENSE](LICENSE) file for more details.

## Support

If you encounter any issues or have questions, please file an issue on our [GitHub issue tracker](https://github.com/terraprompt/logus/issues).

## Citation

If you use Logus in your research, please cite it as follows:

```bibtex
@article{sarkar2024logus,
  title={Logus: An Advanced Tool for Crafting, Analyzing, and Perfecting AI Prompts},
  author={Sarkar, Dipankar},
  journal={arXiv preprint arXiv:2024.xxxxx},
  year={2024},
  url={https://github.com/terraprompt/logus},
  note={Software available from https://github.com/terraprompt/logus},
  abstract={Logus is an open-source software tool designed to facilitate the
    process of prompt engineering for large language models. It provides
    real-time analysis of prompts, supports multiple AI models, and offers
    features for test case generation and prompt execution. This tool aims to
    enhance the efficiency and effectiveness of prompt crafting in AI research
    and applications.}
}
```

For LaTeX users, you can use the following command to cite Logus:

```latex
\cite{sarkar2024logus}
```

---

Happy Prompt Engineering with Logus! 🚀
