# DevTools AI Mock MCP Server

A Model Context Protocol (MCP) server that mocks the functionality of the DevTools AI system for development workflows. This server provides a simulated environment for testing and development of AI-assisted development tools.

## Features

- **Workflow Management**: Simulates different development workflows (Environment Setup, Testing, Deployment, etc.)
- **Toolchain Selection**: Provides appropriate toolchains based on user requirements
- **Tool Recommendations**: Suggests specific tools within selected toolchains
- **Command Generation**: Generates CLI commands with justification
- **Session Management**: Tracks user sessions and conversation history
- **Interactive Confirmation**: Handles user feedback and command refinement

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd devtools-mock-mcp
```

2. Run the setup script:
```bash
python3 setup.py
```

Or install manually:
```bash
pip install -r requirements.txt
chmod +x server.py
```

## Usage

### Running the Server

```bash
python3 server.py
```

### Testing with MCP Inspector

```bash
npx @modelcontextprotocol/inspector python3 server.py
```

### Available Tools

The server provides the following MCP tools:

1. **initiate_session** - Start a new session with a user question
2. **get_workflow** - Get workflow recommendations based on the question
3. **get_toolchain** - Get toolchain options for the selected workflow
4. **get_tool** - Get tool options for the selected toolchain
5. **generate_command** - Generate CLI commands for the selected tool
6. **confirm_command** - Handle user confirmation and feedback
7. **get_session_status** - Get current session status and history

## Example Workflow

1. **Start a session**:
```json
{
  "tool": "initiate_session",
  "arguments": {
    "question": "I need to create a new MATLAB sandbox from a snapshot"
  }
}
```

2. **Get workflow recommendations**:
```json
{
  "tool": "get_workflow",
  "arguments": {
    "session_id": "session_1"
  }
}
```

3. **Get toolchain options**:
```json
{
  "tool": "get_toolchain",
  "arguments": {
    "session_id": "session_1",
    "selected_workflow": "Development Environment Setup"
  }
}
```

4. **Get tool recommendations**:
```json
{
  "tool": "get_tool",
  "arguments": {
    "session_id": "session_1",
    "selected_toolchain": "Environment Setup Tools"
  }
}
```

5. **Generate command**:
```json
{
  "tool": "generate_command",
  "arguments": {
    "session_id": "session_1",
    "selected_tool": "mw_create_sandbox"
  }
}
```

6. **Confirm command**:
```json
{
  "tool": "confirm_command",
  "arguments": {
    "session_id": "session_1",
    "user_response": "yes, that looks correct"
  }
}
```

## Mock Data

The server includes comprehensive mock data for:

- **5 Workflows**: Development Environment Setup, Testing and Validation, Deployment and Release, Debugging and Troubleshooting, General Development
- **14 Toolchains**: Various specialized toolchains for different development tasks
- **20+ Tools**: Mock development tools with descriptions and usage examples
- **Command Templates**: Pre-defined command patterns for different scenarios

## Architecture

### Core Components

- **server.py** - Main MCP server implementation
- **mock_data.py** - Mock data definitions for workflows, toolchains, and tools
- **setup.py** - Setup and installation script

### Session Management

Each session tracks:
- Original user question
- Current step in the workflow (0-4)
- Cursor position for navigation
- Selected workflow, toolchain, and tool
- Generated commands and justifications
- Conversation history

### Intelligence Features

- **Keyword-based Selection**: Uses simple NLP to match user questions to appropriate workflows
- **Context Awareness**: Considers previous selections when making recommendations
- **Command Customization**: Generates commands based on detected parameters in user questions
- **Feedback Processing**: Handles user confirmation and modification requests

## Development

### Project Structure

```
devtools-mock-mcp/
├── README.md          # This file
├── server.py          # Main MCP server
├── mock_data.py       # Mock data definitions
├── setup.py           # Setup script
├── requirements.txt   # Python dependencies
└── .git/             # Git repository
```

### Adding New Tools

1. Add tool definition to `TOOLS` in `mock_data.py`
2. Add command templates to `COMMANDS`
3. Update relevant toolchain definitions
4. Add keyword patterns for selection logic

### Testing

The server can be tested using the MCP Inspector or by implementing a simple MCP client. The session-based architecture allows for comprehensive testing of multi-step workflows.

## API Reference

### Tool Schemas

All tools follow standard MCP tool schemas with JSON Schema input validation. See the `handle_list_tools()` function in `server.py` for complete schema definitions.

### Response Formats

All tools return `List[types.TextContent]` with formatted text responses including:
- Status information
- Generated commands
- Explanations and justifications
- Next step instructions

## License

[License information would go here]

## Contributing

[Contributing guidelines would go here]

## Support

[Support information would go here]
