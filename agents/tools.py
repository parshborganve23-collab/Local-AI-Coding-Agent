"""
Local AI Coding Agent - Tool Registry

Future integrations:
- Project file reader
- Controlled file writer
- Pytest runner
- Approved terminal command executor
- Git status and diff tools

Do not expose unrestricted shell execution to the model.
"""

def available_tools():
    return [
        "project_file_reader",
        "controlled_file_writer",
        "pytest_runner",
        "approved_terminal_executor",
        "git_inspector",
    ]