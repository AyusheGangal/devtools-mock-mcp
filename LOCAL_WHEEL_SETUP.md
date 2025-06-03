# Creating and Installing a Local Wheel File for MCP Server

This guide documents the steps taken to package an MCP server as a local wheel file and install it for use with Claude Desktop, **without publishing to PyPI**.

## Initial Project Structure

Started with basic MCP server files:
```
devtools-mock-mcp/
├── server.py          # Main MCP server code
├── mock_data.py       # Data definitions  
├── test_server.py     # Test script
├── requirements.txt   # Dependencies
└── README.md          # Documentation
```

## Step 1: Create Package Structure

Created a proper Python package structure:

```bash
mkdir devtools_ai_mock_mcp
```

Moved files into package directory:
```bash
cp server.py devtools_ai_mock_mcp/server.py
cp mock_data.py devtools_ai_mock_mcp/mock_data.py
```

Created package marker file:
```bash
# Create devtools_ai_mock_mcp/__init__.py
cat > devtools_ai_mock_mcp/__init__.py << EOF
"""
DevTools AI Mock MCP Server

A Model Context Protocol server that mocks the functionality of the DevTools AI system 
for MathWorks development workflows.
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"
EOF
```

## Step 2: Fix Import Statements

Updated relative imports in the package:
```python
# In devtools_ai_mock_mcp/server.py
# Changed from:
from mock_data import WORKFLOWS, TOOLCHAINS, TOOLS, COMMANDS

# To:
from .mock_data import WORKFLOWS, TOOLCHAINS, TOOLS, COMMANDS
```

## Step 3: Add CLI Entry Point

Added a CLI function to make the server executable:
```python
# Added to devtools_ai_mock_mcp/server.py
def main_cli():
    """CLI entry point for the package."""
    asyncio.run(main())

if __name__ == "__main__":
    main_cli()
```

## Step 4: Create setup.py

Created comprehensive setup configuration:
```python
#!/usr/bin/env python3
"""
Setup script for DevTools AI Mock MCP Server package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="devtools-ai-mock-mcp-ayushe",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Model Context Protocol server that mocks DevTools AI functionality for MathWorks development workflows",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/devtools-mock-mcp",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "devtools-ai-mock-mcp-ayushe=devtools_ai_mock_mcp.server:main_cli",
        ],
    },
    package_data={
        "devtools_ai_mock_mcp": ["*.py"],
    },
    include_package_data=True,
)
```

## Step 5: Create pyproject.toml (Modern Python Packaging)

```toml
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "devtools-ai-mock-mcp-ayushe"
version = "0.1.0"
description = "A Model Context Protocol server that mocks DevTools AI functionality for MathWorks development workflows"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers", 
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9", 
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]
dependencies = [
    "mcp>=0.9.0"
]

[project.scripts]
devtools-ai-mock-mcp-ayushe = "devtools_ai_mock_mcp.server:main_cli"

[project.urls]
Homepage = "https://github.com/yourusername/devtools-mock-mcp"
Repository = "https://github.com/yourusername/devtools-mock-mcp"
Issues = "https://github.com/yourusername/devtools-mock-mcp/issues"
```

## Step 6: Add Supporting Files

Created additional packaging files:

### LICENSE
```text
MIT License

Copyright (c) 2025 DevTools AI Mock MCP

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### MANIFEST.in
```text
include README.md
include requirements.txt
include LICENSE
recursive-include devtools_ai_mock_mcp *.py
```

### .gitignore
```text
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# macOS
.DS_Store
```

## Step 7: Clean Up Old Files

Removed duplicate files from root directory:
```bash
rm server.py mock_data.py test_server.py index.js package.json
rm -rf __pycache__ devtools_ai_mock_mcp.egg-info
```

## Step 8: Install Build Tools

```bash
pip install build
```

## Step 9: Build the Package

```bash
python3 -m build
```

This created:
```
dist/
├── devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
└── devtools_ai_mock_mcp_ayushe-0.1.0.tar.gz
```

## Step 10: Install Local Wheel

```bash
pip install dist/devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
```

This made the CLI command available:
```bash
which devtools-ai-mock-mcp-ayushe
# Output: /opt/homebrew/bin/devtools-ai-mock-mcp-ayushe
```

## Step 11: Update Claude Desktop Configuration

Updated `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "devtools-ai-mock": {
      "command": "devtools-ai-mock-mcp-ayushe",
      "args": [],
      "env": {}
    }
  }
}
```

## Step 12: Test Installation

```bash
# Verify package is installed
pip show devtools-ai-mock-mcp-ayushe

# Verify command exists
devtools-ai-mock-mcp-ayushe --help 2>/dev/null || echo "MCP server runs via stdio"
```

## Final Project Structure

```
devtools-mock-mcp/
├── devtools_ai_mock_mcp/          # Package directory
│   ├── __init__.py                # Package marker
│   ├── server.py                  # Main server code
│   └── mock_data.py               # Data module
├── tests/                         # Test directory
│   ├── __init__.py                
│   └── test_server.py             # Unit tests
├── dist/                          # Built packages (wheels/sdist)
│   ├── devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
│   └── devtools_ai_mock_mcp_ayushe-0.1.0.tar.gz
├── LICENSE                        # License file
├── README.md                      # Documentation
├── pyproject.toml                 # Modern Python config
├── setup.py                       # Legacy compatibility
├── requirements.txt               # Dependencies
├── MANIFEST.in                    # File inclusion rules
├── .gitignore                     # Git ignore
└── DISTRIBUTION_GUIDE.md          # Distribution guide
```

## Key Benefits of This Approach

1. **No PyPI needed** - Package works locally
2. **Professional packaging** - Follows Python standards
3. **Easy CLI command** - `devtools-ai-mock-mcp-ayushe` instead of long python paths
4. **Dependency management** - Automatically installs MCP library
5. **Reusable wheel** - Can share the .whl file with others
6. **Version management** - Proper versioning system

## Usage After Installation

Users can now:
1. Install the wheel file: `pip install path/to/wheel.whl`
2. Add the simple command to Claude config: `"command": "devtools-ai-mock-mcp-ayushe"`
3. Restart Claude Desktop
4. Start using the MCP tools

This approach provides a professional distribution method without requiring PyPI publication!
