"""Interactive console interface for AI Architect Planner."""

import typer
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.theme import Theme
from typing import Literal, Optional, Dict

custom_theme = Theme({
    "info": "cyan",
    "warning": "yellow",
    "error": "red",
    "success": "green",
    "prompt": "yellow",
})

ProjectType = Literal["web", "mobile", "desktop", "api", "other"]
VALID_PROJECT_TYPES = ["web", "mobile", "desktop", "api", "other"]

console = Console(theme=custom_theme)
app = typer.Typer(help="AI Architect Planner - Your Enterprise Architecture Assistant")

def collect_project_details() -> Dict[str, str]:
    """Collect project details through interactive prompts."""
    console.print(
        Panel.fit(
            "[success]Welcome to AI Architect Planner[/success]\n\n"
            "Let's gather some information about your project.",
            title="AI Architect Planner",
            border_style="blue",
        )
    )

    # Collect basic project information
    project_name = Prompt.ask("[prompt]What is your project name?[/prompt]")
    
    # Enforce valid project type selection
    while True:
        project_type = Prompt.ask(
            "[prompt]What type of project is this?[/prompt]",
            choices=VALID_PROJECT_TYPES,
            show_choices=True
        )
        if project_type in VALID_PROJECT_TYPES:
            break
        console.print("[error]Please select a valid project type from the list.[/error]")
    
    project_description = Prompt.ask("[prompt]Please describe your project briefly[/prompt]")
    
    # Display collected information
    console.print("\n[info]Project Details Summary:[/info]")
    console.print(f"Project Name: [success]{project_name}[/success]")
    console.print(f"Project Type: [success]{project_type}[/success]")
    console.print(f"Description: [success]{project_description}[/success]")
    
    return {
        "name": project_name,
        "type": project_type,
        "description": project_description
    }

def process_project_details(details: Dict[str, str]) -> None:
    """Process the collected project details."""
    # Future: Add more interactive steps here
    pass

def main() -> Optional[Dict[str, str]]:
    """Start the interactive AI Architect planning process."""
    try:
        project_details = collect_project_details()
        process_project_details(project_details)
        return project_details
        
    except KeyboardInterrupt:
        console.print("\n[warning]Process interrupted by user. Goodbye![/warning]")
        return None
    except Exception as e:
        console.print(f"\n[error]An error occurred: {str(e)}[/error]")
        return None

def run_cli() -> None:
    """Entry point for the CLI application."""
    main()

if __name__ == "__main__":  # pragma: no cover
    run_cli()
