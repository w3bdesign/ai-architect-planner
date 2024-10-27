"""User interaction and prompts."""

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from typing import Dict

console = Console()
VALID_PROJECT_TYPES = ["web", "mobile", "desktop", "api", "other"]

def collect_project_details() -> Dict[str, str]:
    """Collect project details through interactive prompts."""
    console.print(
        Panel.fit(
            "Welcome to AI Architect Planner\n\n"
            "Let's gather some information about your project.",
            title="AI Architect Planner",
        )
    )

    project_name = Prompt.ask("What is your project name?")
    
    while True:
        project_type = Prompt.ask(
            "What type of project is this?",
            choices=VALID_PROJECT_TYPES,
            show_choices=True
        )
        if project_type in VALID_PROJECT_TYPES:
            break
        console.print("Please select a valid project type from the list.")
    
    project_description = Prompt.ask("Please describe your project briefly")
    
    return {
        "name": project_name,
        "type": project_type,
        "description": project_description
    }

def show_success(project_dir: str, doc_path: str) -> None:
    """Show success messages."""
    console.print(f"Project structure created at {project_dir}")
    console.print(f"Architecture details saved to {doc_path}")

def show_error(message: str) -> None:
    """Show error message."""
    console.print(f"\nAn error occurred: {message}")

def show_interrupt() -> None:
    """Show interrupt message."""
    console.print("\nProcess interrupted by user. Goodbye!")
