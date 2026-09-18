# Contributing to AI-Powered Call Center Analytics

First off, thank you for considering contributing to this project! 🎉

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project adheres to a code of conduct. By participating, you are expected to uphold this code. Please be respectful and constructive in all interactions.

## How Can I Contribute?

### Reporting Bugs 🐛

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear descriptive title**
- **Exact steps to reproduce** the problem
- **Expected behavior** vs actual behavior
- **Screenshots** if applicable
- **Environment details** (OS, Python version, etc.)

### Suggesting Enhancements ✨

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear descriptive title**
- **Detailed description** of the proposed functionality
- **Rationale** - why this enhancement would be useful
- **Possible implementation** approach (optional)

### Pull Requests 🔀

- Fill in the required template
- Follow the coding standards
- Include appropriate test coverage
- Update documentation as needed
- Link related issues

## Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Demo-Call-Center.git
   cd Demo-Call-Center
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt -r dev-requirements.txt
   ```

4. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

## Coding Standards

### Python Style Guide

- Follow **PEP 8** style guidelines
- Use **type hints** where appropriate
- Maximum line length: **100 characters**
- Use **docstrings** for all public functions and classes

### Code Formatting

We use `black` and `isort` for code formatting:

```bash
# Format your code
make fmt

# Check formatting
make fmt-check

# Run linter
make lint
```

### Documentation

- Update README.md for user-facing changes
- Add docstrings for new functions/classes
- Update inline comments for complex logic
- Keep documentation clear and concise

## Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Example:**
```
feat(analysis): add sentiment analysis scoring

Implemented a new sentiment analysis feature that scores
calls based on customer satisfaction indicators.

Closes #123
```

## Pull Request Process

1. **Update documentation** - Ensure README and docstrings are current
2. **Add tests** - Include tests for new functionality
3. **Run tests** - Ensure all tests pass
4. **Format code** - Run `make fmt` before committing
5. **Update CHANGELOG** - Add entry describing changes
6. **Create PR** - Use the PR template and link issues
7. **Code review** - Address feedback from reviewers
8. **Merge** - Maintainers will merge after approval

### PR Checklist

- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] All tests passing
- [ ] No merge conflicts

## Testing

Run tests with:

```bash
pytest tests/
```

Check coverage:

```bash
pytest --cov=src tests/
```

## Questions?

Feel free to open an issue with the `question` label or reach out to the maintainers.

---

**Happy Contributing! 🚀**

*Built with ❤️ by Shrijay Mankar*
