# Contributing to AgentHotspot MCP Server

Thank you for your interest in contributing to the AgentHotspot MCP Server! This document provides guidelines and information for contributors.

## 🌟 Ways to Contribute

- **Bug Reports:** Found a bug? Open an issue with detailed reproduction steps.
- **Feature Requests:** Have an idea? We'd love to hear it.
- **Code Contributions:** Submit PRs for bug fixes or new features.
- **Documentation:** Help improve our docs and examples.
- **Testing:** Help test new releases and report issues.

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- Git
- A GitHub account

### Setting Up the Development Environment

1. **Fork the repository**
   
   Click the "Fork" button on the GitHub repository page.

2. **Clone your fork**
   
   ```bash
   git clone https://github.com/YOUR_USERNAME/agenthotspot-mcp.git
   cd agenthotspot-mcp
   ```

3. **Create a virtual environment**
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**
   
   ```bash
   pip install -e ".[dev]"
   ```

5. **Create a feature branch**
   
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 📝 Development Workflow

### Code Style

We use [Ruff](https://github.com/astral-sh/ruff) for linting and formatting:

```bash
# Check code style
ruff check .

# Auto-fix issues
ruff check --fix .

# Format code
ruff format .
```

### Type Checking

We use [mypy](https://mypy-lang.org/) for static type checking:

```bash
mypy src/agenthotspot_mcp
```

### Running Tests

```bash
pytest
```

### Pre-commit Checklist

Before submitting a PR, ensure:

- [ ] All tests pass (`pytest`)
- [ ] Code is formatted (`ruff format .`)
- [ ] No linting errors (`ruff check .`)
- [ ] Type checks pass (`mypy src/agenthotspot_mcp`)
- [ ] Documentation is updated (if applicable)

## 📬 Submitting Changes

### Pull Request Process

1. **Update documentation** if you've changed APIs or added features
2. **Add tests** for new functionality
3. **Ensure CI passes** on your PR
4. **Write a clear PR description** explaining:
   - What changes you made
   - Why you made them
   - Any breaking changes

### Commit Message Guidelines

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(search): add pagination support for search results
fix(api): handle timeout errors gracefully
docs(readme): add Claude Desktop configuration example
```

## 🐛 Reporting Bugs

When reporting bugs, please include:

1. **Python version** (`python --version`)
2. **Package version** (`pip show agenthotspot-mcp`)
3. **Operating system**
4. **Minimal reproduction steps**
5. **Expected vs actual behavior**
6. **Error messages/stack traces**

## 💡 Feature Requests

When requesting features, please include:

1. **Use case:** What problem does this solve?
2. **Proposed solution:** How would you like it to work?
3. **Alternatives considered:** Other approaches you've thought about
4. **Additional context:** Screenshots, mockups, etc.

## 📜 Code of Conduct

### Our Pledge

We are committed to providing a friendly, safe, and welcoming environment for all contributors.

### Our Standards

- Be respectful and inclusive
- Be patient with newcomers
- Provide constructive feedback
- Focus on what's best for the community

### Enforcement

Instances of unacceptable behavior may be reported to [support@agenthotspot.com](mailto:support@agenthotspot.com).

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Thank You!

Every contribution, no matter how small, helps make this project better. Thank you for being part of the AgentHotspot community!

---

<p align="center">
  <a href="https://agenthotspot.com">
    <strong>AgentHotspot</strong>
  </a>
  — The marketplace for AI agent developers
</p>
