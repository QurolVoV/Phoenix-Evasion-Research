# 🤝 Contributing to Phoenix Evasion Research

Thank you for your interest in contributing to the Phoenix Evasion Research Framework! Your contributions are invaluable to the success of this project.

**Last Updated:** November 2025

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Types of Contributions](#types-of-contributions)
- [Contribution Process](#contribution-process)
- [Coding Guidelines](#coding-guidelines)
- [Commit Message Convention](#commit-message-convention)
- [Pull Request Process](#pull-request-process)
- [Testing Standards](#testing-standards)
- [Documentation](#documentation)
- [Reporting Bugs](#reporting-bugs)
- [Feature Requests](#feature-requests)
- [Additional Help](#additional-help)

---

## 📜 Code of Conduct

### Our Commitment

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of:
- Background or identity
- Experience level
- Technical expertise
- Perspectives or opinions

### Expected Behavior

✅ Use respectful and inclusive language  
✅ Be open to criticism and feedback  
✅ Focus on what is best for the community  
✅ Show empathy toward other contributors  
✅ Respect privacy and data security  

### Unacceptable Behavior

❌ Harassment, bullying, or discrimination  
❌ Personal attacks or trolling  
❌ Public or private harassment  
❌ Spam or manipulation  
❌ Sharing private information without consent  

### Enforcement

Code of Conduct violations can be reported to: **redmoonstonee@gmail.com**

---

## 🚀 Getting Started

### 1. Setup Development Environment

```bash
# Clone repository
git clone https://github.com/QurolVoV/Phoenix-Evasion-Research.git
cd Phoenix-Evasion-Research

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or venv\Scripts\activate  # Windows

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
pip install pytest pytest-cov ruff black mypy  # Dev dependencies
```

### 2. Explore Project Structure

```
Phoenix-Evasion-Research/
├── src/
│   ├── phoenix_evasion_research.py    # Main entry point
│   ├── obfuscator.py                  # String obfuscation
│   ├── syscall_engine.py              # Syscall analysis
│   └── evasion_detector.py            # Evasion detection
├── tests/                              # Unit tests
│   ├── test_obfuscation.py
│   ├── test_syscall.py
│   ├── test_evasion.py
│   └── conftest.py
├── .github/workflows/
│   └── ci-cd.yml                      # CI/CD pipeline
├── requirements.txt
├── README.md
└── CONTRIBUTING.md
```

### 3. Verify Setup

```bash
# Run tests
pytest tests/ -v

# Check code quality
ruff check src/

# Verify imports
python -c "import sys; sys.path.insert(0, 'src'); from phoenix_evasion_research import *; print('✅ Setup OK')"
```

---

## 📝 Types of Contributions

### 1. 🐛 Bug Fixes

Fixing identified bugs or issues.

**Priority:** High  
**Steps:**
- Create an issue first (if not already existing)
- Reference the issue in your commit message
- Include test case for the bug

**Example:**
```bash
git checkout -b bugfix/fix-syscall-extraction
# ... make changes ...
git commit -m "Fix: correct SSN extraction in syscall engine (fixes #123)"
```

### 2. ✨ New Features

Adding new features or functionality.

**Priority:** Medium  
**Steps:**
- Discuss in GitHub Issues first
- Get approval before coding
- Follow existing architecture
- Include comprehensive tests

**Example:**
```bash
git checkout -b feature/add-x86-syscall-support
# ... implement feature ...
git commit -m "Feature: add x86 syscall support"
```

### 3. 📚 Documentation

Improving documentation, README, or docstrings.

**Priority:** Medium  
**Example:**
```bash
git checkout -b docs/improve-syscall-documentation
# ... update docs ...
git commit -m "Docs: improve syscall module documentation"
```

### 4. 🧪 Tests

Adding test coverage or improving test quality.

**Priority:** High  
**Goal:** Maintain ≥ 80% code coverage

**Example:**
```bash
git checkout -b test/add-obfuscator-edge-cases
# ... add tests ...
git commit -m "Test: add edge case tests for obfuscator"
```

### 5. ♻️ Refactoring

Improving code quality without changing functionality.

**Priority:** Low  
**Example:**
```bash
git checkout -b refactor/simplify-evasion-detection
# ... refactor code ...
git commit -m "Refactor: simplify evasion detection logic"
```

### 6. 📊 Performance

Optimizing performance or memory usage.

**Priority:** Medium  
**Include:** Benchmark results

**Example:**
```bash
git checkout -b perf/optimize-syscall-caching
# ... optimize ...
git commit -m "Perf: improve syscall caching efficiency (2x faster)"
```

---

## 🔄 Contribution Process

### Step 1: Fork Repository

```bash
# On GitHub, click the "Fork" button in the top-right
```

### Step 2: Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/Phoenix-Evasion-Research.git
cd Phoenix-Evasion-Research
git remote add upstream https://github.com/QurolVoV/Phoenix-Evasion-Research.git
```

### Step 3: Create Feature Branch

```bash
# Update local main
git fetch upstream
git checkout main
git merge upstream/main

# Create feature branch
git checkout -b feature/description-in-kebab-case
```

**Branch Naming Convention:**
- `feature/` - New feature
- `bugfix/` - Bug fix
- `docs/` - Documentation
- `test/` - Testing
- `refactor/` - Code refactoring
- `perf/` - Performance improvement

### Step 4: Make Changes

```bash
# Edit files, add functionality, etc.

# Format code
black src/ tests/

# Check code quality
ruff check src/ tests/ --fix

# Run type checking
mypy src/

# Run tests
pytest tests/ -v --cov=src/
```

### Step 5: Commit Changes

```bash
git add .
git commit -m "Type: short description (reference #issue)"
```

See [Commit Message Convention](#commit-message-convention) for details.

### Step 6: Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### Step 7: Create Pull Request

1. Open your GitHub repository
2. Click "New Pull Request"
3. Compare your fork with `upstream/main`
4. Fill in the PR template (see next section)
5. Submit the PR

---

## 💻 Coding Guidelines

### Python Style

We follow **PEP 8** with the following tools:
- **Black** - Code formatter
- **Ruff** - Linter
- **MyPy** - Type checker

### Format Your Code

```bash
# Auto-format
black src/ tests/

# Auto-fix linting issues
ruff check src/ tests/ --fix

# Type checking
mypy src/
```

### Code Structure

```python
"""Module docstring describing the module purpose."""

import os
import sys
from typing import Optional, Dict, List
from dataclasses import dataclass

# Constants (UPPER_SNAKE_CASE)
MAX_ITERATIONS = 500000
DEFAULT_TIMEOUT = 30

# Type hints for complex types
AnalysisResult = Dict[str, any]


@dataclass
class ConfigData:
    """Configuration data class with type hints."""
    target: str
    output_file: str
    timeout: int = DEFAULT_TIMEOUT


def main_function(target: str, config: Optional[ConfigData] = None) -> AnalysisResult:
    """
    Function with proper docstring.
    
    Args:
        target: The target to analyze
        config: Optional configuration object
        
    Returns:
        AnalysisResult dict with findings
        
    Raises:
        ValueError: If target is invalid
        
    Example:
        >>> result = main_function("test")
        >>> print(result['status'])
        'success'
    """
    if not target:
        raise ValueError("Target cannot be empty")
    
    return {"status": "success", "data": target}


if __name__ == "__main__":
    main_function("example")
```

### Best Practices

✅ **Type Hints Everywhere**
```python
def process_data(data: List[str]) -> Dict[str, int]:
    return {}
```

✅ **Docstrings for All Public Functions**
```python
def important_function(param: str) -> str:
    """Short description.
    
    Longer description if needed.
    
    Args:
        param: Parameter description
        
    Returns:
        Return value description
    """
```

✅ **Error Handling**
```python
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Failed: {e}")
    raise
```

✅ **Constants at Top**
```python
# Good
MAX_SIZE = 100
DEFAULT_TIMEOUT = 30

# Avoid magic numbers
if size > MAX_SIZE:  # Good
if size > 100:       # Bad
```

❌ **Avoid:**
- Global mutable state
- Bare except clauses
- Long functions (>50 lines)
- Overly complex logic

---

## 📝 Commit Message Convention

Format: `Type: description (references)`

### Types

- **Feature:** - New feature
- **Fix:** - Bug fix
- **Docs:** - Documentation changes
- **Test:** - Test additions/modifications
- **Refactor:** - Code refactoring
- **Perf:** - Performance improvements
- **Chore:** - Build, dependencies, tooling

### Examples

```bash
# Feature
git commit -m "Feature: add x86 syscall support"

# Bug fix with reference
git commit -m "Fix: correct SSN extraction in syscall engine (fixes #123)"

# Documentation
git commit -m "Docs: add syscall module usage examples"

# Test
git commit -m "Test: add edge case tests for obfuscator"

# Multiple changes
git commit -m "Refactor: simplify evasion detection logic

- Remove deprecated methods
- Improve code readability
- Update related tests"

# With breaking change
git commit -m "Feature: add new API endpoints

BREAKING CHANGE: Old endpoints removed (see migration guide)"
```

### Guidelines

- ✅ Use imperative mood ("add feature" not "added feature")
- ✅ Don't capitalize first letter after Type
- ✅ Use present tense
- ✅ Reference issues: "fixes #123"
- ✅ Keep first line ≤ 50 characters
- ✅ Wrap body at 72 characters

---

## 📤 Pull Request Process

### PR Template

When creating a PR, use this template:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation
- [ ] Other: _____

## Related Issue
Fixes #(issue number)

## Testing
- [ ] Unit tests added/updated
- [ ] Manual testing performed
- [ ] No new warnings

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Tests pass locally
- [ ] No breaking changes
- [ ] Ready for review
```

### PR Guidelines

1. **Scope:** One feature/fix per PR
2. **Size:** Ideally ≤ 400 lines of code
3. **Tests:** 100% test coverage for new code
4. **Documentation:** Update docs if needed
5. **Clean History:** Rebase and squash if necessary

### Review Process

1. Maintainer will review within 3-5 days
2. Feedback will be provided in PR comments
3. Make requested changes and push again
4. Approval from at least 1 maintainer
5. Merge to main branch

---

## 🧪 Testing Standards

### Test Coverage

- **Minimum:** 80% code coverage
- **Target:** ≥ 90%
- **Critical paths:** 100%

### Write Tests

```python
# tests/test_obfuscator.py
import pytest
from src.obfuscator import PhoenixObfuscator


class TestPhoenixObfuscator:
    """Tests for PhoenixObfuscator class."""
    
    @pytest.fixture
    def obfuscator(self):
        """Setup test obfuscator."""
        return PhoenixObfuscator()
    
    def test_encrypt_basic(self, obfuscator):
        """Test basic encryption."""
        plaintext = "test_data"
        password = "password"
        
        encrypted = obfuscator.encrypt(plaintext, password)
        
        assert encrypted != plaintext
        assert len(encrypted) > 0
    
    def test_decrypt_roundtrip(self, obfuscator):
        """Test encrypt/decrypt roundtrip."""
        plaintext = "test_data"
        password = "password"
        
        encrypted = obfuscator.encrypt(plaintext, password)
        decrypted = obfuscator.decrypt(encrypted, password)
        
        assert decrypted == plaintext
    
    def test_invalid_password_fails(self, obfuscator):
        """Test decryption with wrong password fails."""
        plaintext = "test_data"
        
        encrypted = obfuscator.encrypt(plaintext, "password1")
        
        with pytest.raises(ValueError):
            obfuscator.decrypt(encrypted, "password2")
```

### Run Tests

```bash
# All tests
pytest tests/ -v

# Specific test file
pytest tests/test_obfuscator.py -v

# With coverage
pytest tests/ --cov=src/ --cov-report=html

# Verbose with output
pytest tests/ -vv -s
```

---

## 📚 Documentation

### Docstring Format

Use Google-style docstrings:

```python
def analyze_evasion(target: str, config: Dict) -> Dict[str, any]:
    """Analyze target for evasion techniques.
    
    Comprehensive analysis of target using multiple
    evasion detection methods.
    
    Args:
        target: URL or IP address to analyze
        config: Configuration dictionary containing:
            - timeout: Request timeout in seconds
            - deep_scan: Enable deep scanning
            
    Returns:
        Dictionary with analysis results:
            - status: 'success' or 'failed'
            - findings: List of detected evasions
            - confidence: Confidence score (0-1)
            
    Raises:
        ValueError: If target format is invalid
        TimeoutError: If analysis exceeds timeout
        
    Example:
        >>> result = analyze_evasion("192.168.1.1", {"timeout": 30})
        >>> print(result['findings'])
        ['obfuscation', 'anti-debug']
    """
```

### README Updates

When adding features, update the README:
- Add feature to the features table
- Update usage examples
- Add troubleshooting if there are edge cases

### Changelog

Update CHANGELOG for:
- New features
- Bug fixes
- Breaking changes
- Dependencies updates

---

## 🐛 Reporting Bugs

### Before Reporting

1. Check if the bug has already been reported
2. Verify using the latest version
3. Gather complete information

### Creating a Bug Report

Use the GitHub Issues template:

```markdown
## Description
Clear description of the bug

## Steps to Reproduce
1. Step 1
2. Step 2
3. Expected result vs actual result

## Environment
- OS: Windows 11 / Ubuntu 20.04 / macOS
- Python: 3.10
- Branch: main / develop

## Logs
```
Error message or stack trace
```

## Screenshots
Attach if applicable
```

### Bug Report Best Practices

✅ Descriptive title  
✅ Clear reproduction steps  
✅ Expected vs actual behavior  
✅ Environment details  
✅ Error logs/stack trace  
✅ Minimal code example  

---

## 💡 Feature Requests

### Before Requesting

1. Check if the feature has already been proposed
2. Consider the use case
3. Compare with existing features

### Creating a Feature Request

```markdown
## Description
What problem does this solve?

## Proposed Solution
How should this be implemented?

## Alternatives
Other approaches considered?

## Additional Context
Screenshots, links, references?

## Priority
Low / Medium / High
```

---

## 📞 Additional Help

### Resources

- [GitHub Documentation](https://docs.github.com)
- [PEP 8 Style Guide](https://pep8.org)
- [Google Python Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- [Pytest Documentation](https://pytest.org)

### Questions?

- 💬 GitHub Discussions
- 📧 redmoonstonee@gmail.com
- 🔍 Search existing issues

### Getting Help

1. Check documentation
2. Search GitHub issues
3. Ask in Discussions
4. Email for urgent matters

---

## 🎉 Recognition

Contributors with significant contributions will:
- Be listed in README
- Be added to CONTRIBUTORS file
- Be recognized in releases
- Be featured in announcements

---

## 📋 Pre-Submission PR Checklist

- [ ] Branch created from latest `main`
- [ ] Code formatted with Black
- [ ] Linting passed with Ruff
- [ ] Type checking passed with MyPy
- [ ] All tests pass: `pytest tests/ -v`
- [ ] Coverage ≥ 80%: `pytest --cov=src/`
- [ ] Documentation updated
- [ ] Commit messages follow convention
- [ ] No breaking changes (or documented)
- [ ] PR description is complete and clear

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License, the same as this project.

---

## 🙏 Thank You!

Thank you for contributing to the Phoenix Evasion Research Framework!  
Your contributions help make cybersecurity research better for everyone.

**Happy Contributing! 🚀**

---

## Support Our Research 💖

If you find this project valuable and want to support our ongoing security research, consider making a donation.  
**Your support helps us maintain and improve this framework for the cybersecurity community.**

[![Donate Saweria](https://img.shields.io/badge/%F0%9F%92%96_Donate-Saweria-FF5E5B?style=for-the-badge&logo=ko-fi&logoColor=white)](https://saweria.co/WoodLabs)

Your support enables us to:
- Continue open-source security research
- Maintain and update the framework regularly
- Develop new defensive security features
- Support the cybersecurity community with free tools
- Conduct advanced threat intelligence research

**Thank you for supporting WoodLabs Security Research!**

---

<div align="center">

**Building Better Defenses Through Understanding Evasion**

For questions: [GitHub Issues](https://github.com/QurolVoV/Phoenix-Evasion-Research/issues)  
For discussions: [GitHub Discussions](https://github.com/QurolVoV/Phoenix-Evasion-Research/discussions)

Woodlabs Security Research © 2025

</div>
