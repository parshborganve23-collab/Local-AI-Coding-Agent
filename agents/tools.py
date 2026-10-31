import subprocess
import sys
from pathlib import Path

from langchain_core.tools import tool

# Restrict operations to the repository directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent


def safe_path(file_path: str) -> Path:
    """Resolve a path and prevent access outside the project."""

    target = (PROJECT_ROOT / file_path).resolve()

    if not target.is_relative_to(PROJECT_ROOT):
        raise ValueError("Access outside project directory is prohibited.")

    return target


@tool
def read_file(file_path: str) -> str:
    """Read a text file inside the project."""

    target = safe_path(file_path)

    if not target.is_file():
        return "Error: File does not exist."

    if target.stat().st_size > 500_000:
        return "Error: File is too large to read."

    return target.read_text(encoding="utf-8")


@tool
def write_file(file_path: str, content: str) -> str:
    """Create or update a text file inside the project."""

    target = safe_path(file_path)

    if target.exists() and not target.is_file():
        return "Error: Target is not a regular file."

    if len(content) > 200_000:
        return "Error: Content exceeds the allowed size."

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")

    return f"Successfully wrote: {file_path}"


@tool
def run_pytest(test_path: str = "sample_project") -> str:
    """Run pytest on a project test directory or test file."""

    target = safe_path(test_path)

    if not target.exists():
        return "Error: Test path does not exist."

    if not (
        target.is_file() and target.name.startswith("test_")
        or target.is_dir()
    ):
        return "Error: Specify a test file or directory."

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "-q",
            str(target),
        ],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        timeout=60,
        shell=False,
    )

    output = result.stdout + result.stderr

    return (
        f"Exit code: {result.returncode}\n"
        f"Test output:\n{output[:12000]}"
    )


def get_tools():
    """Return tools available to the LangGraph agents."""

    return [
        read_file,
        write_file,
        run_pytest,
    ]