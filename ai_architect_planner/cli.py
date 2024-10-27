"""Interactive console interface for AI Architect Planner."""

import typer
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.theme import Theme

custom_theme = Theme({
    "info": "cyan",
    "warning": "yellow",
    "error": "red",
    "success": "green",
    "prompt": "yellow",
})

console = Console(theme=custom_theme)
app = typer.Typer(help="AI Architect Planner - Your Enterprise Architecture Assistant")

def collect_project_details():
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
    project_type = Prompt.ask(
        "[prompt]What type of project is this?[/prompt]",
        choices=["web", "mobile", "desktop", "api", "other"],
    )
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

@app.command()
def main():
    """Start the interactive AI Architect planning process."""
    try:
        project_details = collect_project_details()
        # Future: Add more interactive steps here
        
    except KeyboardInterrupt:
        console.print("\n[warning]Process interrupted by user. Goodbye![/warning]")
    except Exception as e:
        console.print(f"\n[error]An error occurred: {str(e)}[/error]")

if __name__ == "__main__":
    app()
