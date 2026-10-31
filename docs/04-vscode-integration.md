# 04 — Connect Ollama to Visual Studio Code

## Overview

In this tutorial, we will connect a locally running Ollama model to Visual Studio Code using Continue.

This enables local AI-assisted coding and, when supported and configured, agent workflows.

## 1. Install Visual Studio Code

Download:

https://code.visualstudio.com/

Install and launch VS Code.

## 2. Install Continue

Open the VS Code Extensions marketplace.

Search for:

`Continue`

Or install it from:

https://marketplace.visualstudio.com/items?itemName=Continue.continue

Open the Continue sidebar after installation.

## 3. Ensure Ollama is running

Open PowerShell:

```powershell
ollama list
```

Verify that your model exists.

For the standard model:

```powershell
ollama run qwen2.5-coder:7b
```

For the imported IQ3_XXS model:

```powershell
ollama run qwen-coder-iq3
```

You can use a separate terminal to keep the model loaded.

## 4. Configure Continue

Open the Continue configuration file using the extension's configuration interface.

Add a model configuration.

Example for the standard Qwen model:

```yaml
name: Local Qwen Coding
version: 1.0.0
schema: v1

models:
  - name: Qwen2.5-Coder 7B
    provider: ollama
    model: qwen2.5-coder:7b
    apiBase: http://localhost:11434
    roles:
      - chat
      - edit
      - apply
    defaultCompletionOptions:
      contextLength: 4096
      temperature: 0.2
```

For the imported IQ3_XXS model, change:

```yaml
model: qwen-coder-iq3
```

The model name must exactly match the name returned by:

```powershell
ollama list
```

## 5. Test the Connection

Open the Continue sidebar.

Ask:

```text
Explain the structure of my current project.
```

If the model responds, the local connection is working.

## 6. Use AI Chat

Try:

```text
Create a responsive landing page using HTML and CSS.
```

You can ask the model to generate code, explain functions and suggest improvements.

## 7. Use Edit Mode

Select code in your editor and ask Continue to modify it.

Example:

```text
Refactor this function and improve error handling.
```

Review the suggested changes before accepting them.

## 8. Enable Agent Mode

Open Continue's Agent mode.

Agent mode can use configured tools to interact with your workspace.

Depending on the extension version, model capabilities and available tools, an agent can:

- Read project files.
- Search through source code.
- Create new files.
- Edit existing files.
- Run terminal commands.
- Execute tests.
- Analyse errors.

Approve tool actions carefully.

## 9. Example Agent Prompt

Try:

```text
Inspect my project.

Create a responsive landing page with:
- Navigation bar
- Hero section
- Features section
- Pricing cards
- Footer

Use clean HTML, CSS and JavaScript.

Run the available checks and report any errors.
```

Review the generated files and run the application yourself.

## 10. Local API Troubleshooting

Check the Ollama API:

```powershell
Invoke-RestMethod http://localhost:11434
```

Check available models:

```powershell
ollama list
```

Check running models:

```powershell
ollama ps
```

If the connection fails:

1. Confirm Ollama is installed.
2. Confirm its local service is running.
3. Check the model name.
4. Verify the API address.
5. Reload the Continue configuration.

## Important Limitations

- Agent functionality depends on extension and model support.
- Not every model supports every tool-calling workflow reliably.
- A successful chat connection does not guarantee Agent mode will work.
- Review terminal commands before execution.
- Local inference can work offline after installation and downloads.

## Next Tutorial

[05 — Build a Multi-Agent Coding Workflow with LangGraph](05-langgraph-agents.md)

## References

- Continue Documentation: https://docs.continue.dev/
- Continue Models: https://docs.continue.dev/customize/models
- Continue Agent Mode: https://docs.continue.dev/ide-extensions/agent/overview
- Ollama: https://ollama.com/