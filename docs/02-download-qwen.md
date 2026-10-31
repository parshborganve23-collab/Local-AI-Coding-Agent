# 02 — Download Qwen2.5-Coder 7B Using Ollama

## Overview

In this tutorial, we will download Qwen2.5-Coder 7B using Ollama and run it locally.

Qwen2.5-Coder is a coding-focused language model designed for programming tasks.

## 1. Download the Model

Open PowerShell.

Run:

```powershell
ollama pull qwen2.5-coder:7b
```

Wait for the download to finish.

## 2. Verify the Download

Run:

```powershell
ollama list
```

You should see:

```text
NAME                    ID              SIZE
qwen2.5-coder:7b        ...             ...
```

The exact size and model ID may vary by Ollama version.

## 3. Run the Model

Execute:

```powershell
ollama run qwen2.5-coder:7b
```

You can now communicate with the model directly through your terminal.

## 4. Test Code Generation

Enter this prompt:

```text
Create a responsive HTML landing page with a navigation bar,
hero section, pricing cards and footer.
```

The model should generate code in response.

## 5. Test Through the Ollama API

Open another PowerShell window.

Run:

```powershell
$body = @{
    model = "qwen2.5-coder:7b"
    prompt = "Write a Python function to check whether a number is prime."
    stream = $false
} | ConvertTo-Json

$response = Invoke-RestMethod `
    -Uri "http://localhost:11434/api/generate" `
    -Method Post `
    -ContentType "application/json" `
    -Body $body

$response.response
```

This demonstrates that another application can communicate with your local model through Ollama's HTTP API.

## 6. Inspect the Model

Run:

```powershell
ollama show qwen2.5-coder:7b
```

This displays model information, including its configuration and capabilities.

## 7. Check Running Model Resources

Run:

```powershell
ollama ps
```

This shows currently loaded models and their resource allocation.

## 8. Useful Commands

| Command | Function |
|---|---|
| `ollama pull qwen2.5-coder:7b` | Download model |
| `ollama run qwen2.5-coder:7b` | Start model |
| `ollama list` | List models |
| `ollama show qwen2.5-coder:7b` | Inspect model |
| `ollama ps` | Check loaded models |
| `ollama stop qwen2.5-coder:7b` | Stop model |

## Important: Quantization

The standard `qwen2.5-coder:7b` Ollama tag is not a guarantee that you are running IQ3_XXS.

We will cover importing a compatible GGUF quantized model separately.

## Offline Usage

After the model has been downloaded, you can run local inference without an internet connection.

The first download requires internet access.

## Next Tutorial

[03 — IQ3_XXS Quantization and GGUF Model Import](03-iq3-xxs-quantization.md)