# Local-AI-Coding-Agent
Build your own free, offline AI coding environment using Ollama, Qwen, VS Code and LangGraph.

# ⚡ Local AI Coding Agent

**Build your own AI-powered coding environment using free, open-source and locally running AI models.**

Why pay for expensive AI coding subscriptions when you can experiment with local LLMs?

This repository provides a step-by-step guide to building a local AI development environment using Ollama, Qwen2.5-Coder, Visual Studio Code, GGUF quantization and LangGraph.

## 🚀 Features

- Local AI code generation
- VS Code integration
- AI-assisted debugging
- Code review and testing workflows
- Multi-agent orchestration
- Local model inference
- No mandatory paid API subscriptions

## 🧠 Technology Stack

| Technology | Purpose |
|---|---|
| Ollama | Local model runtime |
| Qwen2.5-Coder 7B | Coding model |
| GGUF / IQ3_XXS | Model quantization |
| Visual Studio Code | Development environment |
| Continue | IDE integration |
| Python | Agent development |
| LangGraph | Multi-agent orchestration |

## 📚 Installation Guide

Follow the tutorials in order:

1. [Install Ollama](docs/01-install-ollama.md)
2. [Download Qwen2.5-Coder](docs/02-download-qwen.md)
3. [IQ3_XXS Quantization](docs/03-iq3-xxs-quantization.md)
4. [Connect Ollama to VS Code](docs/04-vscode-integration.md)
5. [Build LangGraph Agents](docs/05-langgraph-agents.md)
6. [Testing and Debugging](docs/06-testing-debugging.md)

## 🏗️ Project Structure

```text
Local-AI-Coding-Agent/
├── README.md
├── docs/
├── agents/
├── requirements.txt
├── .env.example
├── .gitignore
└── LICENSE
```

## 💻 Hardware

The initial configuration targets Windows PCs with 16 GB RAM.

Performance depends on the CPU, available memory, model quantization and context length.

## ⚠️ Important

This project is a work in progress. Some features are experimental. A local coding model does not guarantee the same capabilities as a frontier cloud model.

## 🎯 Goal

Build an accessible local AI development environment capable of assisting developers with planning, coding, debugging, testing and multi-agent workflows.

**Build locally. Code freely. Experiment without limits imposed by API subscriptions.**

## 📜 License

MIT License. See the LICENSE file for details.

Check individual model and dependency licenses before redistribution or commercial use.