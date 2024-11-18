# Requires PowerShell 7+
#Requires -Version 7.0

# Function to check Python version
function Test-PythonVersion {
    try {
        $pythonVersion = python -c "import sys; print(sys.version_info.major, sys.version_info.minor)"
        $version = $pythonVersion -split " "
        $major = [int]$version[0]
        $minor = [int]$version[1]
        
        if ($major -ge 3 -and $minor -ge 11) {
            Write-Host "✅ Python $major.$minor detected" -ForegroundColor Green
            return $true
        } else {
            Write-Host "❌ Python 3.11 or higher is required. Found version $major.$minor" -ForegroundColor Red
            return $false
        }
    } catch {
        Write-Host "❌ Python is not installed or not in PATH" -ForegroundColor Red
        return $false
    }
}

# Function to create and activate virtual environment
function Initialize-VirtualEnvironment {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Failed to create virtual environment" -ForegroundColor Red
        exit 1
    }
    
    Write-Host "✅ Virtual environment created" -ForegroundColor Green
    
    # Activate virtual environment
    Write-Host "Activating virtual environment..." -ForegroundColor Yellow
    & ./venv/Scripts/Activate.ps1
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Failed to activate virtual environment" -ForegroundColor Red
        exit 1
    }
    
    Write-Host "✅ Virtual environment activated" -ForegroundColor Green
}

# Function to install package in development mode
function Install-DevPackage {
    Write-Host "Installing package in development mode..." -ForegroundColor Yellow
    pip install -e ".[dev]"
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Failed to install package" -ForegroundColor Red
        exit 1
    }
    
    Write-Host "✅ Package installed successfully" -ForegroundColor Green
}

# Main execution
Write-Host "🚀 Starting setup process..." -ForegroundColor Cyan

# Check Python version
if (-not (Test-PythonVersion)) {
    Write-Host "Please install Python 3.11 or higher and try again" -ForegroundColor Red
    exit 1
}

# Create and activate virtual environment
Initialize-VirtualEnvironment

# Install package
Install-DevPackage

Write-Host "`n✨ Setup completed successfully!" -ForegroundColor Cyan
Write-Host "You can now start using the AI Architect Planner" -ForegroundColor Cyan
Write-Host "To begin, run: python -m ai_architect_planner" -ForegroundColor Cyan
