#!/usr/bin/env python3
"""
DevTools AI Mock MCP Server - FastMCP Implementation

This server mocks the functionality of the dev-tools-ai-server as an MCP server
using FastMCP for simplified API and automatic transport handling.
"""

import logging
from typing import Dict

from fastmcp import FastMCP

try:
    from .mock_data import WORKFLOWS, TOOLCHAINS, TOOLS, COMMANDS
except ImportError:
    # Handle direct execution case
    import sys
    import os
    sys.path.append(os.path.dirname(__file__))
    from mock_data import WORKFLOWS, TOOLCHAINS, TOOLS, COMMANDS

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("devtools-ai-mock-mcp")

# Global session storage (in production, this would be a database)
sessions: Dict[str, Dict] = {}

# Create the FastMCP server
mcp = FastMCP(
    name="devtools-ai-mock-mcp",
    instructions="""
    This server provides a mock implementation of DevTools AI functionality.
    Start with initiate_session, then use get_workflow, get_toolchain, get_tool,
    generate_command, and confirm_command to complete the workflow.
    """
)

@mcp.tool()
def initiate_session(question: str) -> str:
    """Start a new DevTools AI session with a user question.
    
    Args:
        question: The user's development question or request
        
    Returns:
        Session information including session ID
    """
    # Generate a simple session ID
    session_id = f"session_{len(sessions) + 1}"
    
    # Initialize session data
    sessions[session_id] = {
        "question": question,
        "step": 0,
        "cursor": 0,
        "history": [question],
        "conversation_history": [],
        "selected_workflow": None,
        "selected_toolchain": None,
        "selected_tool": None,
        "generated_command": None,
        "processed_references": []
    }
    
    logger.info(f"Created new session {session_id} with question: {question}")
    
    return (f"Session initiated successfully!\n"
            f"Session ID: {session_id}\n"
            f"Question: {question}\n"
            f"Ready to proceed with workflow selection.")

@mcp.tool()
def get_workflow(session_id: str) -> str:
    """Get workflow options based on the user's question.
    
    Args:
        session_id: Session ID from initiate_session
        
    Returns:
        Selected workflow information
    """
    if session_id not in sessions:
        return "Error: Invalid session ID"
    
    session = sessions[session_id]
    question = session["question"].lower()
    
    # Simple keyword-based workflow selection logic
    selected_workflow = None
    
    if any(keyword in question for keyword in ["sandbox", "build", "environment"]):
        selected_workflow = "Development Environment Setup"
    elif any(keyword in question for keyword in ["test", "testing", "verify"]):
        selected_workflow = "Testing and Validation"
    elif any(keyword in question for keyword in ["deploy", "release", "publish"]):
        selected_workflow = "Deployment and Release"
    elif any(keyword in question for keyword in ["debug", "troubleshoot", "fix", "error"]):
        selected_workflow = "Debugging and Troubleshooting"
    else:
        selected_workflow = "General Development"
    
    # Update session
    session["selected_workflow"] = selected_workflow
    session["step"] = 1
    session["cursor"] = 1
    
    workflow_info = WORKFLOWS.get(selected_workflow, {})
    
    return (f"Workflow Selected: {selected_workflow}\n"
            f"Description: {workflow_info.get('description', '')}\n"
            f"Common tasks: {', '.join(workflow_info.get('common_tasks', []))}\n"
            f"Ready to proceed with toolchain selection.")

@mcp.tool()
def get_toolchain(session_id: str, selected_workflow: str) -> str:
    """Get toolchain options for the selected workflow.
    
    Args:
        session_id: Session ID
        selected_workflow: The selected workflow name
        
    Returns:
        Selected toolchain information
    """
    if session_id not in sessions:
        return "Error: Invalid session ID"
    
    session = sessions[session_id]
    question = session["question"].lower()
    
    # Get toolchains for the workflow
    workflow_toolchains = WORKFLOWS.get(selected_workflow, {}).get("toolchains", [])
    
    # Simple keyword-based toolchain selection
    selected_toolchain = None
    
    if any(keyword in question for keyword in ["matlab", "simulink"]):
        selected_toolchain = next((tc for tc in workflow_toolchains if "MATLAB" in tc), workflow_toolchains[0] if workflow_toolchains else "MATLAB Build Tools")
    elif any(keyword in question for keyword in ["git", "version", "source"]):
        selected_toolchain = next((tc for tc in workflow_toolchains if "Source" in tc), "Source Control Tools")
    elif any(keyword in question for keyword in ["test", "unit", "integration"]):
        selected_toolchain = next((tc for tc in workflow_toolchains if "Test" in tc), "Testing Framework")
    else:
        selected_toolchain = workflow_toolchains[0] if workflow_toolchains else "General Development Tools"
    
    # Update session
    session["selected_toolchain"] = selected_toolchain
    session["step"] = 2
    session["cursor"] = 2
    
    toolchain_info = TOOLCHAINS.get(selected_toolchain, {})
    
    return (f"Toolchain Selected: {selected_toolchain}\n"
            f"Description: {toolchain_info.get('description', '')}\n"
            f"Available tools: {', '.join(toolchain_info.get('tools', []))}\n"
            f"Ready to proceed with tool selection.")

@mcp.tool()
def get_tool(session_id: str, selected_toolchain: str) -> str:
    """Get tool options for the selected toolchain.
    
    Args:
        session_id: Session ID
        selected_toolchain: The selected toolchain name
        
    Returns:
        Selected tool information
    """
    if session_id not in sessions:
        return "Error: Invalid session ID"
    
    session = sessions[session_id]
    question = session["question"].lower()
    
    # Get tools for the toolchain
    toolchain_tools = TOOLCHAINS.get(selected_toolchain, {}).get("tools", [])
    
    # Simple keyword-based tool selection
    selected_tool = None
    
    if any(keyword in question for keyword in ["create", "new", "setup"]):
        selected_tool = next((tool for tool in toolchain_tools if "create" in tool.lower() or "new" in tool.lower()), toolchain_tools[0] if toolchain_tools else "mw_create_sandbox")
    elif any(keyword in question for keyword in ["build", "compile"]):
        selected_tool = next((tool for tool in toolchain_tools if "build" in tool.lower()), "mw_build")
    elif any(keyword in question for keyword in ["test", "run"]):
        selected_tool = next((tool for tool in toolchain_tools if "test" in tool.lower() or "run" in tool.lower()), "mw_test")
    else:
        selected_tool = toolchain_tools[0] if toolchain_tools else "mw_help"
    
    # Update session
    session["selected_tool"] = selected_tool
    session["step"] = 3
    session["cursor"] = 3
    
    tool_info = TOOLS.get(selected_tool, {})
    
    return (f"Tool Selected: {selected_tool}\n"
            f"Description: {tool_info.get('description', '')}\n"
            f"Usage: {tool_info.get('usage', '')}\n"
            f"Documentation: {tool_info.get('doc_url', 'N/A')}\n"
            f"Ready to generate command.")

@mcp.tool()
def generate_command(session_id: str, selected_tool: str) -> str:
    """Generate a CLI command for the selected tool.
    
    Args:
        session_id: Session ID
        selected_tool: The selected tool name
        
    Returns:
        Generated command with justification
    """
    if session_id not in sessions:
        return "Error: Invalid session ID"
    
    session = sessions[session_id]
    question = session["question"]
    
    # Get command templates for the tool
    tool_commands = COMMANDS.get(selected_tool, {})
    
    # Simple logic to generate command based on question
    command = None
    justification = ""
    
    if "snapshot" in question.lower():
        # Extract snapshot name if mentioned
        words = question.split()
        snapshot_name = None
        for i, word in enumerate(words):
            if word.lower() in ["snapshot", "named"] and i + 1 < len(words):
                snapshot_name = words[i + 1].replace(",", "").replace(".", "")
                break
        
        if snapshot_name:
            command = tool_commands.get("with_snapshot", f"{selected_tool} --snapshot {snapshot_name}")
            justification = f"Creating a sandbox from the specified snapshot '{snapshot_name}' as requested."
        else:
            command = tool_commands.get("default", f"{selected_tool}")
            justification = "Creating a standard sandbox environment."
    else:
        command = tool_commands.get("default", f"{selected_tool}")
        justification = f"Using the standard {selected_tool} command based on your request."
    
    # Update session
    session["generated_command"] = {
        "command": command,
        "justification": justification
    }
    session["step"] = 4
    session["cursor"] = 4
    
    return (f"Generated Command: {command}\n"
            f"Justification: {justification}\n"
            f"Please confirm if this command is correct, or provide feedback for adjustments.")

@mcp.tool()
def confirm_command(session_id: str, user_response: str) -> str:
    """Handle user confirmation of the generated command.
    
    Args:
        session_id: Session ID
        user_response: User's confirmation response
        
    Returns:
        Confirmation result or feedback request
    """
    if session_id not in sessions:
        return "Error: Invalid session ID"
    
    session = sessions[session_id]
    generated_command = session.get("generated_command", {})
    
    if not generated_command:
        return "Error: No command generated yet"
    
    user_response_lower = user_response.lower()
    
    # Simple confirmation logic
    if any(word in user_response_lower for word in ["yes", "ok", "correct", "good", "approve", "confirm"]):
        # Command approved
        return (f"Command approved! ✅\n"
                f"Final command: {generated_command['command']}\n"
                f"You can now copy and execute this command in your terminal.\n"
                f"Session completed successfully.")
    elif any(word in user_response_lower for word in ["no", "wrong", "incorrect", "change"]):
        # Command needs modification
        error_type = "command"  # Default to regenerating command
        
        # Determine what needs to be changed based on user feedback
        if any(word in user_response_lower for word in ["workflow", "different task"]):
            error_type = "workflow"
            session["cursor"] = 0
        elif any(word in user_response_lower for word in ["toolchain", "different tool"]):
            error_type = "toolchain"
            session["cursor"] = 1
        elif any(word in user_response_lower for word in ["tool", "specific tool"]):
            error_type = "tool"
            session["cursor"] = 2
        else:
            session["cursor"] = 3  # Regenerate command
        
        return (f"I understand you'd like to make changes. Let me adjust the {error_type} selection.\n"
                f"Please provide more specific feedback about what you'd like to change.")
    else:
        # Unclear response, ask for clarification
        return ("I'm not sure about your response. Please clearly indicate:\n"
                "- 'yes' or 'approve' to confirm the command\n"
                "- 'no' or 'change' to modify the command\n"
                "- Provide specific feedback about what needs to be changed")

@mcp.tool()
def get_session_status(session_id: str) -> str:
    """Get the current status and history of a session.
    
    Args:
        session_id: Session ID
        
    Returns:
        Session status information
    """
    if session_id not in sessions:
        return "Error: Invalid session ID"
    
    session = sessions[session_id]
    
    status_text = f"Session Status for {session_id}:\n"
    status_text += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    status_text += f"Original Question: {session['question']}\n"
    status_text += f"Current Step: {session['step']}/4\n"
    status_text += f"Current Cursor: {session['cursor']}\n"
    status_text += "\nSelections Made:\n"
    status_text += f"  Workflow: {session.get('selected_workflow', 'Not selected')}\n"
    status_text += f"  Toolchain: {session.get('selected_toolchain', 'Not selected')}\n"
    status_text += f"  Tool: {session.get('selected_tool', 'Not selected')}\n"
    
    if session.get('generated_command'):
        status_text += "\nGenerated Command:\n"
        status_text += f"  Command: {session['generated_command']['command']}\n"
        status_text += f"  Justification: {session['generated_command']['justification']}\n"
    
    return status_text

def main_cli():
    """CLI entry point for stdio transport (Claude Desktop)."""
    mcp.run(transport="stdio")

def main_http():
    """CLI entry point for HTTP transport."""
    print("Starting HTTP server on http://127.0.0.1:8001/mcp")
    mcp.run(transport="streamable-http", port=8001)

if __name__ == "__main__":
    # Run with streamable HTTP transport when called directly
    main_http()
