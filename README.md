# 🏗️ AI Architect Planner

> 🤖 Your AI-powered companion for architecting enterprise-ready applications

## ✨ Features

🎯 **Smart Architecture Planning**
- Enterprise-grade application scaffolding
- Best practices implementation
- Technology stack optimization

🧠 **Multi-LLM Integration**
- Leverages multiple AI models
- Real-time documentation updates
- Intelligent decision making

🎨 **Interactive Console Interface**
- Rich-powered interactive prompts
- Guided project setup
- User-friendly experience
- Intelligent conversation flow

🏭 **Enterprise Ready**
- Production-grade setup
- Scalable architecture
- Security-first approach

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- Git

### Installation

1️⃣ Clone the repository:
```bash
git clone https://github.com/yourusername/ai-architect-planner.git
cd ai-architect-planner
```

2️⃣ Create and activate virtual environment:
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Unix/MacOS
source venv/bin/activate
```

3️⃣ Install dependencies:
```bash
# Install package with development dependencies (required for testing)
pip install -e ".[dev]"
```

## 💻 Usage

Start the interactive planning session:
```bash
python ai_architect_planner/cli.py
```

The interactive console will guide you through:
1. Project name selection
2. Project type selection (web, mobile, desktop, api, or other)
3. Project description and requirements gathering

The tool will then:
- Analyze your requirements
- Research optimal technologies
- Generate comprehensive architecture documentation
- Provide implementation guidelines

## 🧪 Testing

We follow Test-Driven Development (TDD) practices and maintain comprehensive test coverage. Our test suite includes:

### Test Categories

🔍 **CLI Tests**
- Basic CLI functionality and startup
- Interactive prompt validation
- Project type validation (web, mobile, desktop, api, other)
- Error handling and graceful exits
- Keyboard interrupt handling

### Running Tests

First, ensure you have installed the package with development dependencies:
```bash
pip install -e ".[dev]"
```

Then you can run the tests:

Run all tests:
```bash
pytest
```

Run tests with coverage report:
```bash
# Generate coverage report
pytest --cov=ai_architect_planner

# Generate detailed coverage report
pytest --cov=ai_architect_planner --cov-report=term-missing
```

Run specific test categories:
```bash
# Run only CLI tests
pytest tests/test_cli.py -v

# Run with detailed output
pytest -v

# Run tests matching specific pattern
pytest -k "test_cli" -v
```

### Test Structure

Tests are organized in the `tests/` directory:
- `test_cli.py`: Interactive CLI interface tests
- Additional test files will be added for new features

### Writing Tests

When contributing new features, please ensure:
1. All new features have corresponding tests
2. Tests use appropriate mocking for external dependencies
3. Error cases are properly tested
4. Tests are properly documented
5. Coverage is maintained above 90%

## 📚 Documentation

The tool generates a comprehensive `ARCHITECT.md` file containing:
- 📐 System Architecture
- 🔧 Technology Stack
- 🛠️ Implementation Guidelines
- 🔒 Security Considerations
- 📈 Scaling Strategies

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---
Made with ❤️ by AI enthusiasts for AI developers
