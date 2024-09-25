# Logus: Craft, Analyze, and Perfect Your AI Prompts

![Logus Logo](https://via.placeholder.com/150?text=Logus)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

## Why Logus?
In the rapidly evolving field of AI and large language models, crafting effective prompts has become a crucial skill. Logus is born out of the need for a sophisticated, user-friendly tool that empowers developers, researchers, and AI enthusiasts to:

- Analyze and refine prompts in real-time
- Generate and manage test cases
- Execute prompts across multiple AI models
- Visualize and understand prompt effectiveness

Whether you're a seasoned prompt engineer or just starting your journey with AI, Logus provides the tools you need to elevate your prompt crafting skills.

## What is Logus?

Logus is an advanced prompt engineering tool that combines a powerful backend API with an intuitive frontend. Key features include:

- **Real-time Prompt Analysis**: Get instant feedback on your prompts' effectiveness and alignment with your goals.
- **Multi-model Support**: Test your prompts across various AI models, including GPT-4, Claude, and more.
- **Test Case Generation**: Automatically generate relevant test cases for your prompts.
- **Interactive Code Editor**: A feature-rich editor with syntax highlighting and real-time analysis feedback.
- **Execution Environment**: Run your prompts and see the results immediately.
- **Test Case Management**: Store and download generated test cases as JSON files.
- **Dynamic Goal Inference**: Automatically infer the goal of your prompt if not provided.

## How It Works

Logus consists of two main components:

1. **Backend API (Python + FastAPI)**: Handles prompt analysis, test generation, and execution across different AI models.
2. **Frontend Application (HTML + jQuery + Tailwind CSS)**: Provides a user-friendly interface for interacting with the API and visualizing results.

The application uses a modular architecture, allowing for easy extension and customization of both the backend models and frontend components.

## How to Use Logus

### Prerequisites

- Python (v3.8 or later)
- API keys for supported AI models (OpenAI, Anthropic, etc.)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/terraprompt/logus.git
   cd logus
   ```

2. Set up the backend:
   ```
   poetry install
   cp .env.example .env
   # Edit .env with your API keys
   ```

### Running Logus

1. Start the backend server:
   ```
   uvicorn main:app --reload
   ```

2. Open your browser and navigate to `http://localhost:8000/static/index.html` to start using Logus!

### Using Logus

1. **Set Your Goal (Optional)**: Begin by entering your prompt engineering goal in the provided text area. If left blank, Logus will attempt to infer the goal.
2. **Select a Model**: Choose the AI model you want to work with from the dropdown menu.
3. **Write Your Prompt**: Use the interactive code editor to write and refine your prompt.
4. **Analyze**: As you type, Logus will provide real-time analysis of your prompt's effectiveness.
5. **Generate Tests**: Click the "Generate Test" button to create relevant test cases for your prompt.
6. **View Analysis**: Click the "Analyze Prompt" button to get detailed analysis of your prompt.
7. **Download Tests**: Use the "Download Tests" button to save generated test cases as a JSON file.
8. **Refine**: Use the analysis feedback and test results to iteratively improve your prompt.

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