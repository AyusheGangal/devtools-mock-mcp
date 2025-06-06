# DevTools AI Mock MCP Server - Installation Guide

## For End Users

### Install from Wheel Package (Recommended)

1. **Download the wheel** from [GitHub Releases](https://github.com/yourusername/devtools-mock-mcp/releases):
```bash
# Download devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
```

2. **Install the package**:
```bash
pip install devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
```

3. **Find the installed command path**:
```bash
which devtools-ai-mock-mcp-proxy
# Example output: /Library/Frameworks/Python.framework/Versions/3.11/bin/devtools-ai-mock-mcp-proxy
```

4. **Configure Claude Desktop**:

Add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "devtools-ai-mock": {
      "command": "/Library/Frameworks/Python.framework/Versions/3.11/bin/devtools-ai-mock-mcp-proxy"
    }
  }
}
```
**Note**: Replace the path with your actual command path from step 3.

### Alternative: Install from GitHub

```bash
pip install git+https://github.com/yourusername/devtools-mock-mcp.git
# Then find the command path as above
```

### Verification

Test that installation works:
```bash
# Test stdio mode (should wait for input)
devtools-ai-mock-mcp-proxy

# Test HTTP mode (should start server)
devtools-ai-mock-mcp-http
```

## Usage

1. Install using method above
2. Configure Claude Desktop with the **full path** to `devtools-ai-mock-mcp-proxy`
3. Restart Claude Desktop
4. Start using DevTools AI with questions like:
   - "I need to create a MATLAB sandbox from snapshot stable_build"
   - "Help me run unit tests for my MATLAB code"
   - "How do I deploy my application to production?"

## Requirements

- Python 3.8+
- fastmcp>=2.0.0 (automatically installed)
- httpx>=0.28.1 (automatically installed)

## Publishing to PyPI

To publish this package:

1. Create accounts on [PyPI](https://pypi.org/) and [TestPyPI](https://test.pypi.org/)
2. Install publishing tools:
   ```bash
   pip install twine
   ```
3. Upload to TestPyPI first:
   ```bash
   twine upload --repository testpypi dist/*
   ```
4. Test installation from TestPyPI:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ devtools-ai-mock-mcp
   ```
5. Upload to PyPI:
   ```bash
   twine upload dist/*
   ```
