# DevTools AI Mock MCP Server - Installation Guide

## Option 1: Install from PyPI (Recommended)

Once published to PyPI, users can install with:

```bash
pip install devtools-ai-mock-mcp
```

Then add to Claude Desktop config:

```json
{
  "mcpServers": {
    "devtools-ai-mock": {
      "command": "devtools-ai-mock-mcp",
      "args": [],
      "env": {}
    }
  }
}
```

## Option 2: Install from GitHub

```bash
pip install git+https://github.com/yourusername/devtools-mock-mcp.git
```

Then use the same Claude Desktop config as above.

## Option 3: Install from Local Wheel

If you have the wheel file:

```bash
pip install devtools_ai_mock_mcp-0.1.0-py3-none-any.whl
```

## Usage

1. Install the package using any method above
2. Add the configuration to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or equivalent on other platforms
3. Restart Claude Desktop
4. Start asking DevTools AI questions like:
   - "I need to create a MATLAB sandbox from snapshot stable_build"
   - "Help me run unit tests for my MATLAB code"
   - "How do I deploy my application to production?"

## Requirements

- Python 3.8+
- mcp>=0.9.0 (automatically installed)

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
