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
├── __main__.py        # Entry point
├── cli.py             # Main CLI
├── config.py          # Configuration settings
├── constants.py       # Shared constants
├── type_definitions.py # Type definitions
├── interaction.py     # User interface
├── project.py         # Project operations
└── llm.py            # AI service
```

### Module Overview

- **__main__.py**: Application entry point
- **cli.py**: Main application orchestration
- **config.py**: Project-wide configuration settings
- **constants.py**: Shared string constants and messages
- **type_definitions.py**: TypeScript-like type definitions
- **interaction.py**: User interaction handling
- **project.py**: File and directory operations
- **llm.py**: AI-powered analysis and recommendations

## 🧪 Testing

Run tests with coverage:
```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=ai_architect_planner

# Run specific test file
pytest tests/test_cli.py -v
```

### Test Structure

```
tests/
├── test_cli.py         # CLI tests
├── test_interaction.py # User interaction tests
├── test_llm.py        # AI service tests
└── test_project.py    # Project operation tests
```

## 📚 Generated Documentation

The tool generates a comprehensive `ARCHITECT.md` in your project containing:
- 📐 System Architecture
- 🔧 Technology Stack
- 🛠️ Implementation Guidelines
- 🔒 Security Considerations
- 📈 Scaling Strategies

## 🔄 Development Workflow

1. Make changes to relevant modules
2. Update tests as needed
3. Run test suite with coverage
4. Update documentation if necessary
5. Submit pull request

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---
Made with ❤️ by AI enthusiasts for AI developers
