# Local Development & Wheel Setup Guide

This guide helps developers set up the DevTools AI Mock MCP Server for local development and testing using the FastMCP wheel-based architecture.

## Overview

This setup allows you to:
- Develop with the FastMCP framework and proxy architecture
- Build and test wheel packages locally
- Test the complete user installation experience
- Develop with streamable HTTP transport while maintaining Claude Desktop compatibility

## Prerequisites

- Python 3.8 or higher
- pip and build tools
- Git
- FastMCP framework

## Development Environment Setup

### 1. Clone and Setup Repository

```bash
git clone <repository-url>
cd devtools-mock-mcp
```

### 2. Install Development Dependencies

```bash
# Install FastMCP and build tools
pip install fastmcp build twine

# For development, you can also install in editable mode
pip install -e .
```

### 3. Development Architecture

The project uses a **proxy architecture**:

```
Claude Desktop (stdio) 
    ↓
proxy_server.py (stdio ↔ HTTP bridge)
    ↓
fastmcp_server.py (HTTP server with FastMCP)
```

### 4. Running for Development

**FastMCP HTTP Server** (for development/testing):
```bash
python3 devtools_ai_mock_mcp/fastmcp_server.py
# Runs on http://127.0.0.1:8001/mcp
```

**Proxy Server** (for Claude Desktop testing):
```bash
python3 devtools_ai_mock_mcp/proxy_server.py
# Starts HTTP server automatically and bridges to stdio
```

**Test with MCP Inspector**:
```bash
npx @modelcontextprotocol/inspector python3 devtools_ai_mock_mcp/fastmcp_server.py
```

## Building and Testing Wheels

### 1. Build the Wheel

```bash
# Clean previous builds
rm -rf dist/ build/ *.egg-info

# Build wheel
python -m build
```

This creates:
- `dist/devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl`
- `dist/devtools_ai_mock_mcp_ayushe-0.1.0.tar.gz`

### 2. Test Local Installation

```bash
# Install the wheel locally
pip install dist/devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl

# Verify console scripts
which devtools-ai-mock-mcp-proxy
which devtools-ai-mock-mcp-http
which devtools-ai-mock-mcp

# Test the commands
devtools-ai-mock-mcp-http &  # Should start HTTP server
echo '{"jsonrpc":"2.0","method":"initialize","params":{},"id":1}' | devtools-ai-mock-mcp-proxy
```

### 3. Test with Claude Desktop

1. **Install the wheel**:
   ```bash
   pip install dist/devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
   ```

2. **Get the command path**:
   ```bash
   which devtools-ai-mock-mcp-proxy
   # Example: /Library/Frameworks/Python.framework/Versions/3.11/bin/devtools-ai-mock-mcp-proxy
   ```

3. **Configure Claude Desktop** (`claude_desktop_config.json`):
   ```json
   {
     "mcpServers": {
       "devtools-ai-mock": {
         "command": "/Library/Frameworks/Python.framework/Versions/3.11/bin/devtools-ai-mock-mcp-proxy"
       }
     }
   }
   ```

4. **Restart Claude Desktop** and test

## Development Workflow

### Making Changes

1. **Edit source code** (primarily `fastmcp_server.py` and `proxy_server.py`)

2. **Test changes directly**:
   ```bash
   # Test HTTP server
   python3 devtools_ai_mock_mcp/fastmcp_server.py
   
   # Test proxy
   python3 devtools_ai_mock_mcp/proxy_server.py
   ```

3. **Rebuild and test wheel**:
   ```bash
   # Rebuild
   rm -rf dist/ build/ *.egg-info
   python -m build
   
   # Reinstall
   pip install --force-reinstall dist/devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
   
   # Test
   devtools-ai-mock-mcp-proxy
   ```

### Code Structure

**FastMCP Server** (`fastmcp_server.py`):
```python
from fastmcp import FastMCP

mcp = FastMCP(name="devtools-ai-mock-mcp")

@mcp.tool()
def initiate_session(question: str) -> str:
    """Start a new DevTools AI session."""
    # Clean decorator-based FastMCP implementation
```

**Proxy Server** (`proxy_server.py`):
```python
# Uses FastMCP.as_proxy() to bridge stdio ↔ HTTP
proxy = FastMCP.as_proxy(
    "http://127.0.0.1:8001/mcp",  # HTTP server
    name="devtools-ai-mock-mcp-proxy"
)
```

### Package Configuration

**Console Entry Points** (`pyproject.toml`):
```toml
[project.scripts]
devtools-ai-mock-mcp = "devtools_ai_mock_mcp.fastmcp_server:main_cli"
devtools-ai-mock-mcp-proxy = "devtools_ai_mock_mcp.proxy_server:main_cli"
devtools-ai-mock-mcp-http = "devtools_ai_mock_mcp.fastmcp_server:main_http"
```

**Dependencies**:
```toml
dependencies = [
    "fastmcp>=2.0.0",
    "httpx>=0.28.1"
]
```

## Testing in Different Environments

### Virtual Environment Testing

```bash
# Create clean test environment
python -m venv test_env
source test_env/bin/activate

# Install and test
pip install dist/devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
which devtools-ai-mock-mcp-proxy

# Test functionality
devtools-ai-mock-mcp-http &
curl http://127.0.0.1:8001/mcp

# Clean up
deactivate
rm -rf test_env
```

### Cross-Platform Testing

Test the wheel on different platforms:
- **macOS**: `/Library/Frameworks/Python.framework/Versions/3.11/bin/`
- **Linux**: `/usr/local/bin/` or `~/.local/bin/`
- **Windows**: `Scripts/` directory in Python installation

## Troubleshooting Development

### FastMCP Import Issues

```bash
# Install FastMCP
pip install fastmcp

# Verify installation
python3 -c "import fastmcp; print('FastMCP version:', fastmcp.__version__)"
```

### Proxy Connection Issues

```bash
# Test HTTP server directly
python3 devtools_ai_mock_mcp/fastmcp_server.py &
curl http://127.0.0.1:8001/mcp

# Test proxy without Claude
echo '{"jsonrpc":"2.0","method":"initialize","params":{},"id":1}' | python3 devtools_ai_mock_mcp/proxy_server.py
```

### Console Script Issues

```bash
# Check if scripts are installed
pip show -f devtools-ai-mock-mcp-ayushe | grep bin

# Reinstall if missing
pip install --force-reinstall dist/devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
```

## Version Management

### Updating Package Version

Update version in both:
- `pyproject.toml`: `version = "0.1.0"`
- `setup.py`: `version="0.1.0"`

### Release Preparation

1. **Update version numbers**
2. **Test in clean environment**
3. **Build final wheel**:
   ```bash
   rm -rf dist/ build/ *.egg-info
   python -m build
   ```
4. **Test wheel installation and console scripts**
5. **Test Claude Desktop integration**

## Next Steps

- **Distribution**: See [DISTRIBUTION_GUIDE.md](DISTRIBUTION_GUIDE.md)
- **User Instructions**: See [USER_INSTALLATION_GUIDE.md](USER_INSTALLATION_GUIDE.md)
- **FastMCP Documentation**: https://gofastmcp.com/

## Key Benefits of This Architecture

✅ **Modern FastMCP API**: Clean `@mcp.tool()` decorators  
✅ **Streamable HTTP**: Your server runs with HTTP transport  
✅ **Claude Compatibility**: Proxy bridges stdio ↔ HTTP automatically  
✅ **Easy Distribution**: Single wheel with console entry points  
✅ **Development Friendly**: Test HTTP server directly during development
