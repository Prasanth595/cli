# Exact Commands to Test

## Important: Use the Local Modified Code

You need to make sure you're using the modified code, not an installed version.

### Option 1: Install in Development Mode (Recommended)
```cmd
cd C:\Users\Krish\Downloads\new_http\httpie
pip install -e .
```

Then test with:
```cmd
python -m httpie POST https://httpbin.org/post "data:={\"bad json\"}"
```

### Option 2: Run from Project Directory with PYTHONPATH
```cmd
cd C:\Users\Krish\Downloads\new_http\httpie
set PYTHONPATH=%CD%
python -m httpie POST https://httpbin.org/post "data:={\"bad json\"}"
```

### Option 3: Use Python Script Directly
```cmd
cd C:\Users\Krish\Downloads\new_http\httpie
python -m httpie POST https://httpbin.org/post "data:={\"bad json\"}"
```

## Exact Command to Run

### Windows CMD:
```cmd
python -m httpie POST https://httpbin.org/post "data:={\"bad json\"}"
```

### Windows PowerShell:
```powershell
python -m httpie POST https://httpbin.org/post "data:={\"bad json\"}"
```

### Alternative (if quotes are tricky):
```cmd
python -m httpie POST https://httpbin.org/post data:='{"bad json"}'
```

## What You Should See

### ❌ OLD Error (before our changes):
```
http: error: 'data:={"bad json"}': Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
```

### ✅ NEW Error (after our changes):
```
http: error: 'data:={"bad json"}': Invalid JSON provided in request body.
Check your quotes, commas, and brackets.
Example:
  data:='{"name": "John"}'
```

## Verify You're Using Local Code

Check which version is being used:
```cmd
python -c "import httpie.cli.requestitems; print(httpie.cli.requestitems.__file__)"
```

Should show: `C:\Users\Krish\Downloads\new_http\httpie\httpie\cli\requestitems.py`

If it shows a different path (like in site-packages), you need to install in dev mode:
```cmd
pip install -e .
```

