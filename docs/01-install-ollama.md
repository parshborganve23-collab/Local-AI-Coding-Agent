# 01 — Install Ollama on Windows

## Overview

Ollama allows you to download and run open-source language models locally on your computer.

In this tutorial, we will install Ollama on Windows and verify that its local API is working.

## 1. Download Ollama

Official website:

https://ollama.com/download

1. Select Windows.
2. Download the installer.
3. Run the installer.
4. Complete the installation.

## 2. Verify Installation

Open Windows PowerShell.

Run:

```powershell
ollama --version
```

If installed correctly, PowerShell will display the Ollama version.

## 3. Check Whether Ollama Is Running

Run:

```powershell
ollama list
```

This displays the models installed on your computer.

To check running models:

```powershell
ollama ps
```

## 4. Check the Local API

Ollama exposes a local HTTP API, normally on port 11434.

Run:

```powershell
Invoke-RestMethod http://localhost:11434
```

Expected response:

```text
Ollama is running
```

## 5. Test Model Generation

After downloading a model, you can test its generation API.

Example:

```powershell
$body = @{
    model = "qwen2.5-coder:7b"
    prompt = "Write a Python program to add two numbers."
    stream = $false
} | ConvertTo-Json

Invoke-RestMethod `
    -Uri "http://localhost:11434/api/generate" `
    -Method Post `
    -ContentType "application/json" `
    -Body $body
```

The model should return a generated response.

## 6. Useful Ollama Commands

| Command | Purpose |
|---|---|
| `ollama --version` | Check version |
| `ollama list` | List downloaded models |
| `ollama ps` | Show running models |
| `ollama pull MODEL` | Download a model |
| `ollama run MODEL` | Run a model |
| `ollama stop MODEL` | Stop a running model |
| `ollama show MODEL` | Inspect a model |
| `ollama rm MODEL` | Remove a model |

## Troubleshooting

### Ollama command not recognized

Restart PowerShell after installation. If the command is still unavailable, verify that Ollama is installed and its executable is available in PATH.

### Connection refused on port 11434

Make sure Ollama is running. Start the Ollama application or run:

```powershell
ollama serve
```

If another Ollama server is already running, do not start a second instance.

### Model downloads fail

Check your internet connection and available disk space.

## Important

- Initial installation and model downloads require internet.
- Model inference can run offline after the required model files are downloaded.
- Local inference uses your computer's CPU, RAM and GPU resources.
- Ollama does not automatically provide IDE agent functionality. That will be configured in a later tutorial.

## Next Tutorial

[02 — Download and Run Qwen2.5-Coder 7B](02-download-qwen.md)