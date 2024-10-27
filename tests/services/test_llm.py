"""Tests for LLM service."""

from ai_architect_planner.services.llm import (
    analyze_project_requirements,
    suggest_technology_stack,
    generate_architecture_doc
)
from ai_architect_planner.utils.type_definitions import ProjectDetails

def test_analyze_project_requirements():
    """Test project requirements analysis."""
    test_details = ProjectDetails(
        name="test-project",
        type="web",
        description="A test web application"
    )
    
    result = analyze_project_requirements(test_details)
    assert "architecture" in result
    assert "components" in result
    assert "security" in result
    assert "scalability" in result
    assert all(isinstance(v, list) for v in result.values())

def test_suggest_technology_stack():
    """Test technology stack suggestions."""
    result = suggest_technology_stack("web")
    assert "frontend" in result
    assert "backend" in result
    assert "devops" in result
    assert all(isinstance(v, list) for v in result.values())

def test_generate_architecture_doc():
    """Test architecture document generation."""
    test_details = ProjectDetails(
        name="test-project",
        type="web",
        description="A test web application"
    )
    
    result = generate_architecture_doc(test_details)
    assert isinstance(result, str)
    assert "# test-project - Architecture Document" in result
    assert "## Project Overview" in result
    assert "### System Architecture" in result
    assert "### Technology Stack" in result
