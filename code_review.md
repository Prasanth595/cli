# Formal Code Review: HTTPie CLI

## 🔗 Repository

Fork: https://github.com/Bibosss/cli

## 🔍 Review Scope

### Reviewed Aspects:

-   [x] Code style (PEP8)
-   [x] Error handling
-   [x] Documentation
-   [x] Test coverage
-   [x] Security vulnerabilities
-   [x] Project structure

---

## 🛠 Tools Used

### ✅ `flake8`

-   Result: no major style issues found
-   Comment: code style is well-maintained and consistent

### ⚠️ `bandit`

-   Observations: use of `assert` found in production code
    -   Example: `httpie/models.py`
    -   **Recommendation:** replace `assert` with `if` + `raise Exception(...)` to ensure checks are not stripped in optimized mode

### ❌ `mypy`

-   Output: `Found 268 errors in 44 files`
-   Comment: many functions and modules lack type hints
-   **Recommendation:** progressively add `type hints` starting with:
    -   `httpie/client/dispatch/`
    -   `httpie/core.py`

---

## ✍️ Code Comments (TODO / FIXME)

**`httpie/models.py`:**

```python
# FIXME: Avoid using assert in production code; use if + raise instead.
```
