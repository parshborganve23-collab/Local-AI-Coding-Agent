# 03 — IQ3_XXS Quantization and GGUF Import

## Overview

GGUF is a model file format commonly used by llama.cpp and supported by Ollama.

IQ3_XXS is a low-bit quantization format that reduces model storage and memory requirements, with a trade-off in model quality.

**Important:** Ollama does not convert an existing model into IQ3_XXS simply by importing it. You must download an already quantized GGUF file.

## 1. Find a compatible model

Example model repository:

https://huggingface.co/mradermacher/Qwen2.5-Coder-7B-i1-GGUF

Check the repository's available files and select an IQ3_XXS GGUF file.

Check:
- Model architecture is Qwen2.5-Coder 7B.
- It is the intended instruction-tuned variant.
- The file is GGUF.
- Quantization is IQ3_XXS.
- The model license permits your intended use.

## 2. Prepare the folder

Open PowerShell:

```powershell
mkdir C:\LocalAI\Qwen-IQ3
cd C:\LocalAI\Qwen-IQ3
```

## 3. Install Hugging Face CLI

```powershell
py -m pip install -U huggingface_hub
```

Verify:

```powershell
hf --help
```

## 4. Download the GGUF file

Use the exact repository filename from Hugging Face.

Example command pattern:

```powershell
hf download mradermacher/Qwen2.5-Coder-7B-i1-GGUF "EXACT_IQ3_XXS_FILENAME.gguf" --local-dir .
```

Replace the placeholder with the actual filename.

Do not assume every repository has the same naming convention.

## 5. Verify the downloaded file

```powershell
Get-ChildItem *.gguf
```

Check its SHA-256 hash:

```powershell
Get-FileHash .\EXACT_IQ3_XXS_FILENAME.gguf -Algorithm SHA256
```

Compare the result with a trusted checksum if the repository publishes one.

## 6. Create an Ollama Modelfile

Create a file named:

`Modelfile`

Add:

```text
FROM ./EXACT_IQ3_XXS_FILENAME.gguf

PARAMETER num_ctx 4096
PARAMETER temperature 0.2
```

Replace the filename with your actual downloaded file.

## 7. Import into Ollama

Run from the same folder:

```powershell
ollama create qwen-coder-iq3 -f Modelfile
```

Wait for the import to finish.

## 8. Run the quantized model

```powershell
ollama run qwen-coder-iq3
```

Test it:

```text
Create a responsive React landing page with a navigation bar and pricing section.
```

## 9. Verify the imported model

Run:

```powershell
ollama show qwen-coder-iq3
```

Also check:

```powershell
ollama list
```

Ollama imports the GGUF weights; it does not quantize them again during this process.

## 10. Connect it to VS Code

In your Continue configuration, select:

```yaml
model: qwen-coder-iq3
```

Keep the Ollama provider and local API address configured.

Restart or reload the model configuration.

## 11. IQ3_XXS trade-offs

| Advantage | Trade-off |
|---|---|
| Smaller model file | Lower precision |
| Reduced memory requirements | Possible quality loss |
| Easier local deployment | Not guaranteed to be faster |
| Suitable for experimentation | May struggle with complex code |

## 12. Troubleshooting

### Model import fails

- Confirm the file is a valid GGUF model.
- Confirm that the architecture is supported by your Ollama version.
- Check that the Modelfile points to the correct filename.
- Check available disk space.

### Model does not run

- Check `ollama list`.
- Check `ollama ps`.
- Reduce context length.
- Close other memory-intensive applications.

## Next Tutorial

[04 — Connect Ollama to Visual Studio Code](04-vscode-integration.md)

## References

- Ollama GGUF Import: https://docs.ollama.com/import
- Qwen2.5-Coder GGUF: https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct-GGUF
- GGUF Quantization Repository: https://huggingface.co/mradermacher/Qwen2.5-Coder-7B-i1-GGUF
- Hugging Face CLI: https://huggingface.co/docs/huggingface_hub/guides/cli