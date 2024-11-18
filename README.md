[![codecov](https://codecov.io/gh/w3bdesign/ai-architect-planner/graph/badge.svg?token=DOEIVG4KLQ)](https://codecov.io/gh/w3bdesign/ai-architect-planner)

# 🏗️ AI Architect Planner

> 🤖 Your AI-powered companion for architecting enterprise-ready applications

## ✨ Features

🎯 **Smart Architecture Planning**
- Enterprise-grade application scaffolding
- Best practices implementation
- Technology stack optimization
- Project structure generation

🧠 **AI-Powered Design**
- Architecture pattern recommendations
- Technology stack suggestions
- Security considerations
- Scalability strategies

🎨 **Interactive Experience**
- User-friendly CLI interface
- Guided project setup
- Detailed documentation generation
- Clear project organization

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- Git

### Installation

1️⃣ Clone the repository:
```bash
git clone https://github.com/w3bdesign/ai-architect-planner.git
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

3️⃣ Install in development mode:
```bash
pip install -e ".[dev]"
```

## 💻 Usage

Start the interactive planning session:
```bash
python -m ai_architect_planner
```

The tool will:
1. Guide you through project setup
2. Generate project structure
3. Create detailed architecture documentation
4. Provide technology recommendations

### Generated Project Structure

For each project, the tool creates:
```
your-project/
├── src/           # Source code
├── docs/          # Documentation
│   └── ARCHITECT.md  # Architecture document
└── tests/         # Test files
```

## 🏛️ Project Structure

```
ai_architect_planner/
├── core/          # Core functionality
│   ├── interaction.py  # User interaction
│   └── project.py      # Project operations
├── services/      # Service modules
│   └── llm.py         # AI service (mock)
├── utils/         # Utilities
│   ├── config.py          # Configuration
│   ├── constants.py       # Constants
│   └── type_definitions.py # Type hints
└── cli/           # CLI interface
    └── cli.py          # Main CLI
```

### Module Overview

#### Core
- **interaction.py**: User interaction handling
- **project.py**: Project structure operations

#### Services
- **llm.py**: AI service for architecture analysis (currently mocked)

#### Utils
- **config.py**: Project-wide configuration
- **constants.py**: Shared constants
- **type_definitions.py**: TypeScript-like type hints

#### CLI
- **cli.py**: Main CLI interface

## 🧪 Testing

The project uses pytest for testing and maintains code coverage through Codecov integration.

### Running Tests Locally

```bash
# Run all tests with coverage
pytest --cov=ai_architect_planner --cov-report=term

# Run specific test file
pytest tests/cli/test_cli.py -v
```

### Continuous Integration

Our GitHub Actions workflow automatically runs on push and pull requests to the main branch, performing:

1. **Environment Setup**
   - Python 3.11 setup
   - Installation of dependencies

2. **Code Quality**
   - Linting with Ruff
   - Format checking with Ruff (non-blocking)

3. **Testing**
   - Runs pytest with multiple coverage reports:
     - XML report for Codecov
     - HTML report for local viewing
     - Terminal output for immediate feedback
   - Generates JUnit XML test results

4. **Artifacts**
   - Uploads test results and coverage reports as artifacts
   - Pushes coverage data to Codecov for tracking

View the latest coverage reports on [Codecov](https://codecov.io/gh/w3bdesign/ai-architect-planner).

### Test Structure

```
tests/
├── cli/          # CLI tests
├── core/         # Core module tests
├── services/     # Service tests
└── utils/        # Utility tests
```

## 📚 Generated Documentation

The tool generates a comprehensive `ARCHITECT.md` in your project containing:
- 📐 System Architecture
- 🔧 Technology Stack
- 🛠️ Implementation Guidelines
- 🔒 Security Considerations
- 📈 Scaling Strategies

## 🔄 Development Workflow

1. Create feature branch
2. Make changes
3. Run tests and linting:
   ```bash
   # Run tests with coverage
   pytest --cov=ai_architect_planner --cov-report=term

   # Run Ruff for linting and formatting
   ruff check
   ruff format
   ```
4. Submit pull request

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---
Made with ❤️ by AI enthusiasts for AI developers