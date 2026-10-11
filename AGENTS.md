# AGENTS.md

Context file for AI agents working on httpie.

**Dual Format**: This file combines Category A (Operations Manual) and Category B (Context Guide) for comprehensive agent guidance.

**Domain Detected:** Agent / Chatbot (Based on codebase patterns)

## Project Overview

httpie is a Python project using setuptools.

**Key Info:**
- **Primary Language:** Python
- **Build System:** setuptools
- **Test Framework:** pytest
- **Total Files:** 265
- **Test Files:** 104
- **AI Readiness Score:** 71/100 (AI-Native-Plus)

---

## 🚨 AI Policy & Operations

Extracted from CONTRIBUTING.md - operational constraints and procedures.

### Setup & Environment

- Creates an isolated Python virtual environment inside `./venv` (via the standard library [venv](https://docs.python.org/3/library/venv.html) tool);
- installs all dependencies and also installs HTTPie (in editable mode so that the `http` command will point to your working copy).
- and runs tests (It is the same as running `make install test`).



## 🤖 Agent/Chatbot Architecture

This is an AI agent or dialogue system project.

### Key Patterns Detected

- **Intent Handling:** The project processes user intents and maps them to actions
- **Entity Extraction:** Named entity recognition and slot filling for dialogue context
- **Conversation Management:** Multi-turn dialogue flows with context preservation
- **Tool Use:** Agent actions or skills that execute external operations

### Testing Agent Conversations

When writing tests for dialogue systems:

1. **Conversation Flows:** Test end-to-end dialogue paths, not individual components
2. **Intent Accuracy:** Verify correct intent detection for various phrasings
3. **Entity Extraction:** Test slot filling accuracy and edge cases
4. **Context Preservation:** Ensure multi-turn conversations maintain state correctly
5. **Action Execution:** Mock external actions and verify correct invocation
6. **Fallback Handling:** Test graceful degradation when confidence is low



### Detected Frameworks

| Framework | Version | Detection Type |
|-----------|---------|-----------------|
| pytest | unknown | Direct import |
| requests | unknown | Wrapped/Re-exported |
| unittest | unknown | Direct import |



## 🤖 AI Contribution Policy

- ✅ AI-assisted contributions have special rules

## Operational Constraints

- ⚠️ Coverage gates are monotonic (never lower baseline)

## Release Procedures

- Release workflow: .github/workflows/release.yml



## 🏗️ Architecture & Context Guide

This section provides architectural context and agent-understanding for the codebase.

### Prerequisites

- **Python:** 3.9+ (or applicable language version)
- **Package Manager:** pip or uv
- **Test Runner:** pytest



### Project Structure

```
httpie/
├── Makefile
├── setup.py
├── setup.cfg
├── httpie/             # Source code
├── tests/                # Test suite (104 files)
└── README.md             # Project documentation
```

### Architecture Overview

#### Key Components
- **Main Entry:** Standard layout
- **Test Suite:** 104 test files
- **Build Configuration:** Makefile, setup.py, setup.cfg

#### Design Principles

1. **Modularity** - Code organized by functionality with clear separation of concerns
2. **Testability** - Comprehensive test coverage across critical paths
3. **Clarity** - Explicit naming and structure for AI agent understanding
4. **Consistency** - Uniform patterns and conventions throughout codebase
5. **Maintainability** - Well-documented code with clear intent

### Directory Map

| Directory | Purpose |
|-----------|----------|
| `docs/` | Documentation |
| `tests/` | Test suite |


### Development Workflow

#### Initial Setup

```bash
git clone https://github.com/YOUR_ORG/httpie.git
cd httpie
pip install -e .
# or
uv sync --all-groups
```

#### Development Commands

**Running Tests:**
```bash
pytest                    # Run all tests
pytest tests/             # Run specific test directory
pytest -v                 # Verbose output with test names
pytest -x                 # Stop on first failure
coverage run -m pytest && coverage report  # With coverage report
```

#### Code Quality
```bash
ruff check .              # Lint with ruff
ruff format .             # Format code
mypy .                    # Type checking (if configured)
```

### Code Style & Conventions

- **Naming:** Use snake_case for functions and variables
- **Type Hints:** Yes (strongly encouraged)
- **Error Handling:** Yes - handle errors at boundaries; let exceptions propagate when another layer owns recovery
- **Logging:** No
- **Testing:** Yes - write tests alongside code changes

### Testing Strategy

**Framework:** pytest
**Test Files:** 104 found

Before committing:
1. Run the full test suite: `pytest`
2. Ensure all tests pass
3. Check type hints: `mypy .`
4. Format code: `ruff format .`

### Writing Documentation

When updating docs:
1. Always include explanatory text before code snippets
2. Describe *why* and *what* before showing *how*
3. Keep sections focused on a single concept
4. Use clear, concrete examples

### Contributing Guidelines

This project has a detailed contribution guide at **`CONTRIBUTING.md`**.

**Key Requirements:**
- **Performance Work**: Requires benchmarks and performance metrics in PR description

**Before submitting:**
1. Read `CONTRIBUTING.md` in full
2. Check recent merged PRs for patterns
3. Follow the specific requirements above

### Common Patterns

When contributing to this project:
1. Read existing code in the area you're modifying
2. Follow the established patterns and style
3. Write tests for new functionality
4. Use clear, descriptive variable and function names
5. Add docstrings for public APIs
6. Update tests when changing behavior

### What We Value

✅ Well-tested code with clear intent
✅ Consistent code style and naming conventions
✅ Code that is easy for AI agents to understand
✅ Clear, descriptive commit messages
✅ Modular, reusable components
✅ Comprehensive documentation

### What We Avoid

❌ Large functions doing multiple things
❌ Commented-out dead code
❌ Inconsistent naming or patterns
❌ Unclear error messages
❌ Unexplained magic numbers or strings
❌ Skipped tests or test TODOs

### AI Readiness Dimensions (Scoring)

This project is evaluated across 8 dimensions:

1. **Architecture** (0/100) - Code organization and modularity
2. **Testing** (15/100) - Test coverage and quality
3. **Dependencies** (12/100) - Dependency management
4. **Conventions** (6/100) - Consistent patterns
5. **Entry Points** (0/100) - Clear main/start locations
6. **Security** (15/100) - Input validation and error handling
7. **Build** (10/100) - Clear build/setup instructions
8. **Documentation** (8/100) - Code and project documentation

### Next Steps

Before making changes:
1. Read relevant source files to understand the existing code
2. Look at existing tests for similar functionality
3. Follow the patterns you see in the codebase
4. Write tests for your changes
5. Run `pytest` to verify nothing breaks
6. Run code quality checks: `ruff check . && mypy .`
7. Format your code: `ruff format .`

---

*Generated by Braxis - keeping AI agents in sync with your code*
