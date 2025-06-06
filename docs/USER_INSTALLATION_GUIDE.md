# User Installation Guide

This guide is for end users who want to install and use the DevTools AI Mock MCP Server with Claude Desktop.

## Prerequisites

- Claude Desktop installed on your system
- Python 3.8 or higher
- pip (Python package installer)

## Installation Steps

### Step 1: Download and Install the Wheel

1. **Download** the wheel package from [GitHub Releases](https://github.com/yourusername/devtools-mock-mcp/releases):
   - Look for `devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl`

2. **Install** using pip:
   ```bash
   pip install devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
   ```

3. **Verify installation**:
   ```bash
   which devtools-ai-mock-mcp-proxy
   ```
   This should return a path like:
   ```
   /Library/Frameworks/Python.framework/Versions/3.11/bin/devtools-ai-mock-mcp-proxy
   ```

### Step 2: Configure Claude Desktop

1. **Locate Claude Desktop config file**:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
   - **Linux**: `~/.config/Claude/claude_desktop_config.json`

2. **Add the server configuration** using the **full path** from Step 1:
   ```json
   {
     "mcpServers": {
       "devtools-ai-mock": {
         "command": "/Library/Frameworks/Python.framework/Versions/3.11/bin/devtools-ai-mock-mcp-proxy"
       }
     }
   }
   ```
   
   **Important**: Replace the path with your actual path from `which devtools-ai-mock-mcp-proxy`

### Step 3: Restart Claude Desktop

Close and reopen Claude Desktop completely to load the new server configuration.

### Step 4: Verify Installation

Look for the 🔨 hammer icon in Claude Desktop's input area, which indicates MCP tools are available.

## Usage

### Architecture Overview

The server uses a proxy architecture:
```
Claude Desktop (stdio) → Proxy → HTTP Server (FastMCP)
```

This allows you to benefit from modern FastMCP features while maintaining Claude Desktop compatibility.

### Example Questions

Try asking Claude these development questions:

- "I need to create a new MATLAB sandbox from snapshot stable_build"
- "How do I run unit tests for my MATLAB project?"
- "Help me deploy my application to staging environment"
- "I want to set up a development environment for testing"

### Expected Workflow

1. **Ask your question** - Claude will call `initiate_session`
2. **Workflow selection** - Server suggests appropriate workflow
3. **Toolchain recommendation** - Relevant toolchains are suggested
4. **Tool selection** - Specific tools are recommended
5. **Command generation** - Actual CLI commands are generated
6. **Confirmation** - You can approve or request changes

## Troubleshooting

### "Command not found" Error

If you see `spawn devtools-ai-mock-mcp-proxy ENOENT`:

1. **Check the command path**:
   ```bash
   which devtools-ai-mock-mcp-proxy
   ```

2. **Use the full path** in Claude Desktop config, not just the command name

3. **Verify installation**:
   ```bash
   pip list | grep devtools-ai-mock-mcp-ayushe
   ```

### Server Connection Issues

If the server doesn't connect:

1. **Test the proxy directly**:
   ```bash
   echo '{"jsonrpc":"2.0","method":"initialize","params":{},"id":1}' | devtools-ai-mock-mcp-proxy
   ```

2. **Check Python environment**:
   ```bash
   python3 -c "import fastmcp; print('FastMCP available')"
   ```

3. **Restart Claude Desktop** after configuration changes

### Commands Don't Work

Remember: This is a **mock server** for demonstration and development:

- Generated commands are examples, not real tools
- Use the patterns as guidance for actual development tools
- The server simulates DevTools AI workflows for testing purposes

## Advanced Usage

### Running Different Modes

The package provides three commands:

- **`devtools-ai-mock-mcp-proxy`** - For Claude Desktop (stdio → HTTP proxy)
- **`devtools-ai-mock-mcp-http`** - Direct HTTP server for development
- **`devtools-ai-mock-mcp`** - Direct stdio server

### Development Testing

Test the HTTP server directly:
```bash
devtools-ai-mock-mcp-http
# Server runs on http://127.0.0.1:8001/mcp
```

### Customization

The server includes rich mock data that can be extended by developers. See the [DISTRIBUTION_GUIDE.md](DISTRIBUTION_GUIDE.md) for information on customizing and rebuilding the package.
