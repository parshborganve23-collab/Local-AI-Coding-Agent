# 05 — Build a Local Multi-Agent Coding System with LangGraph

## Overview

LangGraph is a framework for building stateful AI agent workflows.

In this tutorial, we will create four specialist agents that communicate through a shared workflow.

### Agent Architecture

| Agent | Responsibility |
|---|---|
| Planner | Analyses requirements and creates a plan |
| Developer | Generates the implementation |
| Reviewer | Reviews implementation and identifies issues |
| Tester | Creates test cases and testing recommendations |

All agents use the same local Ollama model.

## 1. Requirements

- Python 3.11+
- Ollama installed
- Qwen2.5-Coder 7B downloaded
- VS Code
- LangGraph
- LangChain Ollama integration

## 2. Install Dependencies

Open PowerShell inside the repository.

```powershell
python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
```

## 3. Start Ollama

```powershell
ollama run qwen2.5-coder:7b
```

Keep Ollama available while running the Python application.

## 4. Configure Environment

Create a `.env` file in the project root:

```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=qwen2.5-coder:7b
```

Do not commit your personal `.env` file.

## 5. Create the Agent Workflow

The implementation uses four sequential nodes:

```text
USER TASK
    |
    v
PLANNER AGENT
    |
    v
DEVELOPER AGENT
    |
    v
REVIEWER AGENT
    |
    v
TESTER AGENT
    |
    v
FINAL REPORT
```

Each node receives the shared project state and returns its own result.

## 6. Run the Application

From the repository root:

```powershell
python agents/main.py
```

Enter a programming task when prompted.

The workflow will generate:
- An implementation plan.
- A proposed code implementation.
- A code review.
- A test plan and suggested test cases.

## 7. Important Limitations

This initial implementation is a sequential multi-agent prototype.

It does not yet:
- Automatically modify your VS Code project.
- Execute terminal commands.
- Run generated tests.
- Automatically repair failed tests.
- Guarantee that generated code is correct.

These capabilities require additional file-system, execution and approval tools.

## 8. Future Improvements

- Add file-reading and file-writing tools.
- Add controlled terminal execution.
- Integrate pytest.
- Add conditional review and repair loops.
- Add Git integration.
- Add human approval checkpoints.

## Next Tutorial

[06 — Testing, Debugging and Verification](06-testing-debugging.md)