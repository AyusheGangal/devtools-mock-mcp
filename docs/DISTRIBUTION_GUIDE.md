# Distribution Guide

This guide explains how to build, package, and distribute the DevTools AI Mock MCP Server for both developers and end users.

## For Developers: Building the Package

### Prerequisites

- Python 3.8+
- build package: `pip install build`
- twine (for PyPI): `pip install twine`

### Local Development Setup

See [LOCAL_WHEEL_SETUP.md](LOCAL_WHEEL_SETUP.md) for development environment setup.

### Building the Wheel

1. **Clean previous builds**:
   ```bash
   rm -rf dist/ build/ *.egg-info
   ```

2. **Build the package**:
   ```bash
   python -m build
   ```

   This creates:
   - Source distribution: `dist/devtools_ai_mock_mcp_ayushe-0.1.0.tar.gz`
   - **Wheel distribution**: `dist/devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl`

3. **Verify the build**:
   ```bash
   # Check wheel contents
   python -m zipfile -l dist/devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
   
   # Test installation in clean environment
   pip install dist/devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
   which devtools-ai-mock-mcp-proxy
   ```

### Package Architecture

The built package includes:

- **FastMCP HTTP Server** (`fastmcp_server.py`) - Main server with streamable HTTP transport
- **Proxy Server** (`proxy_server.py`) - stdio ↔ HTTP bridge for Claude Desktop
- **Mock Data** (`mock_data.py`) - Comprehensive workflow/tool definitions
- **Console Entry Points**:
  - `devtools-ai-mock-mcp-proxy` - For Claude Desktop
  - `devtools-ai-mock-mcp-http` - For HTTP testing
  - `devtools-ai-mock-mcp` - For stdio testing

## Distribution Methods

### Method 1: GitHub Releases (Recommended)

1. **Create a GitHub release**:
   - Tag version: `v0.1.0`
   - Upload `devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl`

2. **Provide installation instructions**:
   ```bash
   # Download from releases
   pip install devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
   ```

3. **Claude Desktop config template**:
   ```json
   {
     "mcpServers": {
       "devtools-ai-mock": {
         "command": "/path/to/python/bin/devtools-ai-mock-mcp-proxy"
       }
     }
   }
   ```

### Method 2: PyPI Publication

1. **Test on TestPyPI**:
   ```bash
   twine upload --repository testpypi dist/*
   pip install --index-url https://test.pypi.org/simple/ devtools-ai-mock-mcp-ayushe
   ```

2. **Upload to PyPI**:
   ```bash
   twine upload dist/*
   ```

3. **Users install with**:
   ```bash
   pip install devtools-ai-mock-mcp-ayushe
   ```

### Method 3: Direct Distribution

For enterprise/internal use:
```bash
# Host wheel file internally
pip install https://internal-server.com/wheels/devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
```

## User Installation Workflow

### What Users Need to Do

1. **Install the wheel**:
   ```bash
   pip install devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
   ```

2. **Find command path**:
   ```bash
   which devtools-ai-mock-mcp-proxy
   # Example: /Library/Frameworks/Python.framework/Versions/3.11/bin/devtools-ai-mock-mcp-proxy
   ```

3. **Configure Claude Desktop** with **full path**:
   ```json
   {
     "mcpServers": {
       "devtools-ai-mock": {
         "command": "/Library/Frameworks/Python.framework/Versions/3.11/bin/devtools-ai-mock-mcp-proxy"
       }
     }
   }
   ```

4. **Restart Claude Desktop**

### Why Full Paths Are Required

Claude Desktop runs in an isolated environment and needs absolute paths to find console commands installed via pip.

## Testing Distribution

### Pre-Release Checklist

1. **Build verification**:
   ```bash
   python -m build
   pip install --force-reinstall dist/devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
   ```

2. **Console scripts test**:
   ```bash
   # Test all entry points
   devtools-ai-mock-mcp-proxy &
   devtools-ai-mock-mcp-http &
   echo '{"jsonrpc":"2.0","method":"initialize","params":{},"id":1}' | devtools-ai-mock-mcp
   ```

3. **Claude Desktop integration**:
   - Install package
   - Configure with full path
   - Test MCP tools availability (🔨 hammer icon)
   - Test actual tool calls

4. **Clean environment test**:
   ```bash
   # Test in fresh virtual environment
   python -m venv test_env
   source test_env/bin/activate
   pip install dist/devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
   which devtools-ai-mock-mcp-proxy
   ```

## Version Management

### Updating Versions

Update in these files:
- `pyproject.toml` - `version = "0.1.0"`
- `setup.py` - `version="0.1.0"`

### Release Workflow

1. Update version numbers
2. Update CHANGELOG.md
3. Build and test package
4. Create Git tag: `git tag v0.1.0`
5. Push tag: `git push origin v0.1.0`
6. Create GitHub release with wheel attachment
7. Update documentation links

## Package Dependencies

### Runtime Dependencies

- **fastmcp>=2.0.0** - Core MCP framework with proxy support
- **httpx>=0.28.1** - HTTP client for proxy communication

### Why FastMCP?

- **Modern API**: Clean `@mcp.tool()` decorators vs low-level handlers
- **Proxy Support**: Built-in `FastMCP.as_proxy()` for transport bridging
- **HTTP Transport**: Native streamable HTTP support
- **Auto Discovery**: Automatic tool/resource detection

## Troubleshooting Distribution

### Common Issues

1. **"Command not found"**:
   - User needs full path in Claude config
   - Check `which devtools-ai-mock-mcp-proxy`

2. **Import errors**:
   - FastMCP not installed: `pip install fastmcp`
   - Wrong Python environment

3. **Proxy connection fails**:
   - HTTP server startup issues
   - Port 8001 already in use
   - Permissions/firewall blocking

### Support Documentation

Provide users with:
- [USER_INSTALLATION_GUIDE.md](USER_INSTALLATION_GUIDE.md) - Step-by-step installation
- [INSTALLATION.md](INSTALLATION.md) - Technical installation details
- Troubleshooting section in README.md
- Example Claude Desktop configurations
