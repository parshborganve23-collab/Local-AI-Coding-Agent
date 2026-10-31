# 06 — Automated Testing and Debugging

## Overview

This tutorial introduces automated testing and debugging for the Local AI Coding Agent.

The objective is to move from AI-generated test suggestions towards actual test execution and failure analysis.

## 1. Install Pytest

Activate your virtual environment:

```powershell
.venv\Scripts\activate
```

Install pytest:

```powershell
pip install pytest
```

Add this to `requirements.txt`:

```text
pytest
```

## 2. Create a Test Project

Create a folder:

```powershell
mkdir sample_project
```

Create `sample_project/calculator.py`:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

## 3. Create Automated Tests

Create:

`sample_project/test_calculator.py`

```python
import pytest

from calculator import add, subtract, multiply, divide


def test_add():
    assert add(5, 3) == 8


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(5, 3) == 15


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

## 4. Run the Tests

From the sample_project directory:

```powershell
cd sample_project
python -m pytest -v
```

Pytest will execute the test cases and report passed or failed tests.

## 5. Understand Test Results

Example successful output:

```text
test_calculator.py::test_add PASSED
test_calculator.py::test_subtract PASSED
test_calculator.py::test_multiply PASSED
test_calculator.py::test_divide PASSED
test_calculator.py::test_divide_by_zero PASSED

5 passed
```

The exact output may vary by pytest version.

## 6. Use Qwen for Failure Analysis

Copy the failed test output and ask your local model:

```text
Analyse this Python test failure.

Identify:
1. The cause of the failure.
2. The affected function.
3. The recommended fix.
4. Additional test cases.

Do not assume the suggested fix is correct.
```

## 7. Build an Automated Repair Workflow

A future agent workflow can follow this process:

```text
GENERATE CODE
     |
     v
RUN PYTEST
     |
     v
TESTS PASSED?
   /     \
 YES     NO
 |        |
 v        v
REPORT   ANALYSE ERROR
          |
          v
       SUGGEST FIX
          |
          v
       HUMAN REVIEW
          |
          v
       APPLY FIX
          |
          v
       RUN TESTS AGAIN
```

## 8. Safety Recommendations

- Run generated code in a dedicated project directory.
- Never execute untrusted code on your main system without isolation.
- Review modifications before accepting them.
- Do not expose unrestricted terminal access to an AI model.
- Use version control before automated modifications.
- Set a maximum number of repair attempts.

## 9. Future Improvements

- Integrate pytest with LangGraph.
- Add automated test-result parsing.
- Create a conditional repair node.
- Add human approval checkpoints.
- Track code changes using Git.
- Add isolated execution environments.

## Next Development Stage

Implement project file tools, controlled command execution and an automated debugging loop.