# Quick Test Commands

## Test the Improved Error Message

### Windows CMD:
```cmd
python -m httpie POST https://httpbin.org/post "data:={\"bad json\"}"
```

### Windows PowerShell:
```powershell
python -m httpie POST https://httpbin.org/post "data:={\"bad json\"}"
```

### What you should see:
```
http: error: 'data:={"bad json"}': Invalid JSON provided in request body.
Check your quotes, commas, and brackets.
Example:
  data:='{"name": "John"}'
```

### Verify Exit Code (PowerShell):
```powershell
python -m httpie POST https://httpbin.org/post "data:={\"bad json\"}"
$LASTEXITCODE  # Should show 1
```

### Verify Exit Code (CMD):
```cmd
python -m httpie POST https://httpbin.org/post "data:={\"bad json\"}"
echo %ERRORLEVEL%  # Should show 1
```

### Test Valid JSON (should work normally):
```cmd
python -m httpie POST https://httpbin.org/post "data:={\"name\": \"John\", \"age\": 30}"
```

