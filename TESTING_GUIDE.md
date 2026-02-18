# Testing Guide for Malformed JSON Error Improvement

This guide shows you how to test the improved error message for malformed JSON in HTTPie.

## Prerequisites

1. **Install dependencies** (if not already installed):
   ```bash
   pip install -e ".[test]"
   ```
   Or if you prefer to install manually:
   ```bash
   pip install pytest pytest-httpbin responses pytest-mock werkzeug
   ```

## Method 1: Run the Unit Test

Run the specific test we added:

```bash
# Run just the malformed JSON test
pytest tests/test_json.py::test_malformed_json_error -v

# Or run all JSON tests
pytest tests/test_json.py -v
```

Expected output should show the test passing:
```
tests/test_json.py::test_malformed_json_error PASSED
```

## Method 2: Test Manually with HTTPie CLI

### Test 1: Malformed JSON (should show friendly error)

```bash
# This should show the new friendly error message
python -m httpie POST https://httpbin.org/post data:='{"bad json"}'
```

**Expected output:**
```
usage: http [--json] [--form] [--multipart] [--boundary BOUNDARY] ...
http: error: 'data:={"bad json"}': Invalid JSON provided in request body.
Check your quotes, commas, and brackets.
Example:
  data:='{"name": "John"}'
```

**Verify exit code is non-zero:**
```bash
python -m httpie POST https://httpbin.org/post data:='{"bad json"}'
echo $?  # On Linux/Mac, should print 1
# On Windows PowerShell:
$LASTEXITCODE  # Should be 1
```

### Test 2: Valid JSON (should work normally)

```bash
# This should work without errors
python -m httpie POST https://httpbin.org/post data:='{"name": "John", "age": 30}'
```

**Expected:** Request should be sent successfully (or show normal HTTP response).

### Test 3: Other malformed JSON examples

Try these to see the error message:

```bash
# Missing closing brace
python -m httpie POST https://httpbin.org/post data:='{"name": "John"'

# Missing quotes
python -m httpie POST https://httpbin.org/post data:='{name: "John"}'

# Trailing comma
python -m httpie POST https://httpbin.org/post data:='{"name": "John",}'
```

## Method 3: Test with Python Script

Create a test script to verify the error handling:

```python
#!/usr/bin/env python
"""Test malformed JSON error handling."""

import sys
sys.path.insert(0, '.')

from httpie.cli.exceptions import ParseError
from httpie.cli.requestitems import load_json
from httpie.cli.argtypes import KeyValueArg

# Test malformed JSON
arg = KeyValueArg(
    key='data',
    value='{"bad json"}',
    sep=':=',
    orig='data:={"bad json"}'
)

try:
    load_json(arg, '{"bad json"}')
    print("ERROR: Should have raised ParseError")
    sys.exit(1)
except ParseError as e:
    print("✓ Error caught correctly!")
    print(f"\nError message:\n{str(e)}\n")
    
    # Verify message contains expected parts
    msg = str(e)
    checks = [
        'Invalid JSON provided in request body',
        'Check your quotes, commas, and brackets',
        'Example:'
    ]
    
    for check in checks:
        if check in msg:
            print(f"✓ Contains: {check}")
        else:
            print(f"✗ Missing: {check}")
            sys.exit(1)
    
    print("\n✓ All checks passed!")
```

Run it:
```bash
python test_script.py
```

## Method 4: Run All Tests

To make sure nothing broke:

```bash
# Run all tests
pytest

# Run just the JSON-related tests
pytest tests/test_json.py -v

# Run with coverage (if pytest-cov is installed)
pytest --cov=httpie tests/test_json.py
```

## Expected Behavior Summary

✅ **Malformed JSON**: Shows friendly error message, exits with code 1  
✅ **Valid JSON**: Works normally, no errors  
✅ **Exit Code**: Non-zero (1) on JSON parse errors  
✅ **Error Message**: Contains all required elements:
   - "Invalid JSON provided in request body"
   - "Check your quotes, commas, and brackets"
   - Example showing correct syntax

## Troubleshooting

If tests fail:
1. Make sure dependencies are installed: `pip install -e ".[test]"`
2. Make sure you're in the project root directory
3. Check Python version: `python --version` (should be 3.7+)
4. Try running with verbose output: `pytest -vv tests/test_json.py::test_malformed_json_error`

