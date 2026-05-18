# LeetCode Practice

Python solutions to LeetCode problems, each with its own unit test.

## Setup

```bash
pip install -r requirements.txt
```

## Running Tests

```bash
# Run all tests
pytest

# Run tests for a specific problem
pytest test_0001_two_sum.py -v
```

## File Naming

Each problem gets two files:

- `p{number}_{name}.py` — solution (e.g. `p0001_two_sum.py`)
- `test_p{number}_{name}.py` — unit tests (e.g. `test_p0001_two_sum.py`)
