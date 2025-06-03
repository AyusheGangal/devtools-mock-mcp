#!/usr/bin/env python3
"""
DevTools AI Mock MCP Server - HTTP Transport

This server mocks the functionality of the dev-tools-ai-server as an MCP server
using HTTP transport with FastAPI.
"""

import asyncio
import json
import logging
import os
from typing import Any, Dict, List, Optional, Sequence
from mcp.server.models import InitializationOptions
import mcp.types as types
from mcp.server import NotificationOptions, Server
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from .mock_data import WORKFLOWS, TOOLCHAINS, TOOLS, COMMANDS

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("devtools-ai-mock-mcp")

# Create server instance
server = Server("devtools-ai-mock-mcp")

# Global session storage (in production, this would be a database)
sessions = {}

@server.list_tools()
async def handle_list_tools() -> List[types.Tool]:
    """List available tools for the DevTools AI workflow."""
    return [
        types.Tool(
            name="initiate_session",
            description="Start a new DevTools AI session with a user question",
            inputSchema={
                "type": "object",
                "properties": {
                    "question": {
                        "type": "string",
                        "description": "The user's development question or request"
                    }
                },
                "required": ["question"]
            }
        ),
        types.Tool(
            name="get_workflow",
            description="Get workflow options based on the user's question",
            inputSchema={
                "type": "object",
                "properties": {
                    "session_id": {
                        "type": "string",
                        "description": "Session ID from initiate_session"
                    }
                },
                "required": ["session_id"]
            }
        ),
        types.Tool(
            name="get_toolchain",
            description="Get toolchain options for the selected workflow",
            inputSchema={
                "type": "object",
                "properties": {
                    "session_id": {
                        "type": "string",
                        "description": "Session ID"
                    },
                    "selected_workflow": {
                        "type": "string",
                        "description": "The selected workflow name"
                    }
                },
                "required": ["session_id", "selected_workflow"]
            }
        ),
        types.Tool(
            name="get_tool",
            description="Get tool options for the selected toolchain",
            inputSchema={
                "type": "object",
                "properties": {
                    "session_id": {
                        "type": "string",
                        "description": "Session ID"
                    },
                    "selected_toolchain": {
                        "type": "string",
                        "description": "The selected toolchain name"
                    }
                },
                "required": ["session_id", "selected_toolchain"]
            }
        ),
        types.Tool(
            name="generate_command",
            description="Generate a CLI command for the selected tool",
            inputSchema={
                "type": "object",
                "properties": {
                    "session_id": {
                        "type": "string",
                        "description": "Session ID"
                    },
                    "selected_tool": {
                        "type": "string",
                        "description": "The selected tool name"
                    }
                },
                "required": ["session_id", "selected_tool"]
            }
        ),
        types.Tool(
            name="confirm_command",
            description="Handle user confirmation of the generated command",
            inputSchema={
                "type": "object",
                "properties": {
                    "session_id": {
                        "type": "string",
                        "description": "Session ID"
                    },
                    "user_response": {
                        "type": "string",
                        "description": "User's confirmation response"
                    }
                },
                "required": ["session_id", "user_response"]
            }
        ),
        types.Tool(
            name="get_session_status",
            description="Get the current status and history of a session",
            inputSchema={
                "type": "object",
                "properties": {
                    "session_id": {
                        "type": "string",
                        "description": "Session ID"
                    }
                },
                "required": ["session_id"]
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> List[types.TextContent]:
    """Handle tool calls for DevTools AI functionality."""
    
    if name == "initiate_session":
        return await initiate_session(arguments)
    elif name == "get_workflow":
        return await get_workflow(arguments)
    elif name == "get_toolchain":
        return await get_toolchain(arguments)
    elif name == "get_tool":
        return await get_tool(arguments)
    elif name == "generate_command":
        return await generate_command(arguments)
    elif name == "confirm_command":
        return await confirm_command(arguments)
    elif name == "get_session_status":
        return await get_session_status(arguments)
    else:
        raise ValueError(f"Unknown tool: {name}")

async def initiate_session(arguments: dict) -> List[types.TextContent]:
    """Start a new session with the user's question."""
    question = arguments.get("question", "")
    
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
    
    return [
        types.TextContent(
            type="text",
            text=f"Session initiated successfully!\n"
                 f"Session ID: {session_id}\n"
                 f"Question: {question}\n"
                 f"Ready to proceed with workflow selection."
        )
    ]

async def get_workflow(arguments: dict) -> List[types.TextContent]:
    """Get workflow options based on the user's question."""
    session_id = arguments.get("session_id", "")
    
    if session_id not in sessions:
        return [types.TextContent(type="text", text="Error: Invalid session ID")]
    
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
    
    return [
        types.TextContent(
            type="text",
            text=f"Workflow Selected: {selected_workflow}\n"
                 f"Description: {workflow_info.get('description', '')}\n"
                 f"Common tasks: {', '.join(workflow_info.get('common_tasks', []))}\n"
                 f"Ready to proceed with toolchain selection."
        )
    ]

async def get_toolchain(arguments: dict) -> List[types.TextContent]:
    """Get toolchain options for the selected workflow."""
    session_id = arguments.get("session_id", "")
    selected_workflow = arguments.get("selected_workflow", "")
    
    if session_id not in sessions:
        return [types.TextContent(type="text", text="Error: Invalid session ID")]
    
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
    
    return [
        types.TextContent(
            type="text",
            text=f"Toolchain Selected: {selected_toolchain}\n"
                 f"Description: {toolchain_info.get('description', '')}\n"
                 f"Available tools: {', '.join(toolchain_info.get('tools', []))}\n"
                 f"Ready to proceed with tool selection."
        )
    ]

async def get_tool(arguments: dict) -> List[types.TextContent]:
    """Get tool options for the selected toolchain."""
    session_id = arguments.get("session_id", "")
    selected_toolchain = arguments.get("selected_toolchain", "")
    
    if session_id not in sessions:
        return [types.TextContent(type="text", text="Error: Invalid session ID")]
    
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
    
    return [
        types.TextContent(
            type="text",
            text=f"Tool Selected: {selected_tool}\n"
                 f"Description: {tool_info.get('description', '')}\n"
                 f"Usage: {tool_info.get('usage', '')}\n"
                 f"Documentation: {tool_info.get('doc_url', 'N/A')}\n"
                 f"Ready to generate command."
        )
    ]

async def generate_command(arguments: dict) -> List[types.TextContent]:
    """Generate a CLI command for the selected tool."""
    session_id = arguments.get("session_id", "")
    selected_tool = arguments.get("selected_tool", "")
    
    if session_id not in sessions:
        return [types.TextContent(type="text", text="Error: Invalid session ID")]
    
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
    
    return [
        types.TextContent(
            type="text",
            text=f"Generated Command: {command}\n"
                 f"Justification: {justification}\n"
                 f"Please confirm if this command is correct, or provide feedback for adjustments."
        )
    ]

async def confirm_command(arguments: dict) -> List[types.TextContent]:
    """Handle user confirmation of the generated command."""
    session_id = arguments.get("session_id", "")
    user_response = arguments.get("user_response", "").lower()
    
    if session_id not in sessions:
        return [types.TextContent(type="text", text="Error: Invalid session ID")]
    
    session = sessions[session_id]
    generated_command = session.get("generated_command", {})
    
    if not generated_command:
        return [types.TextContent(type="text", text="Error: No command generated yet")]
    
    # Simple confirmation logic
    if any(word in user_response for word in ["yes", "ok", "correct", "good", "approve", "confirm"]):
        # Command approved
        return [
            types.TextContent(
                type="text",
                text=f"Command approved! ✅\n"
                     f"Final command: {generated_command['command']}\n"
                     f"You can now copy and execute this command in your terminal.\n"
                     f"Session completed successfully."
            )
        ]
    elif any(word in user_response for word in ["no", "wrong", "incorrect", "change"]):
        # Command needs modification
        error_type = "command"  # Default to regenerating command
        
        # Determine what needs to be changed based on user feedback
        if any(word in user_response for word in ["workflow", "different task"]):
            error_type = "workflow"
            session["cursor"] = 0
        elif any(word in user_response for word in ["toolchain", "different tool"]):
            error_type = "toolchain"
            session["cursor"] = 1
        elif any(word in user_response for word in ["tool", "specific tool"]):
            error_type = "tool"
            session["cursor"] = 2
        else:
            session["cursor"] = 3  # Regenerate command
        
        return [
            types.TextContent(
                type="text",
                text=f"I understand you'd like to make changes. Let me adjust the {error_type} selection.\n"
                     f"Please provide more specific feedback about what you'd like to change."
            )
        ]
    else:
        # Unclear response, ask for clarification
        return [
            types.TextContent(
                type="text",
                text=f"I'm not sure about your response. Please clearly indicate:\n"
                     f"- 'yes' or 'approve' to confirm the command\n"
                     f"- 'no' or 'change' to modify the command\n"
                     f"- Provide specific feedback about what needs to be changed"
            )
        ]

async def get_session_status(arguments: dict) -> List[types.TextContent]:
    """Get the current status and history of a session."""
    session_id = arguments.get("session_id", "")
    
    if session_id not in sessions:
        return [types.TextContent(type="text", text="Error: Invalid session ID")]
    
    session = sessions[session_id]
    
    status_text = f"Session Status for {session_id}:\n"
    status_text += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    status_text += f"Original Question: {session['question']}\n"
    status_text += f"Current Step: {session['step']}/4\n"
    status_text += f"Current Cursor: {session['cursor']}\n"
    status_text += f"\nSelections Made:\n"
    status_text += f"  Workflow: {session.get('selected_workflow', 'Not selected')}\n"
    status_text += f"  Toolchain: {session.get('selected_toolchain', 'Not selected')}\n"
    status_text += f"  Tool: {session.get('selected_tool', 'Not selected')}\n"
    
    if session.get('generated_command'):
        status_text += f"\nGenerated Command:\n"
        status_text += f"  Command: {session['generated_command']['command']}\n"
        status_text += f"  Justification: {session['generated_command']['justification']}\n"
    
    return [types.TextContent(type="text", text=status_text)]

# Create FastAPI app at module level
app = FastAPI(title="DevTools AI Mock MCP Server", version="0.1.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "server": "devtools-ai-mock-mcp"}

# Tool endpoints
@app.post("/tools/list")
async def list_tools():
    tools = await handle_list_tools()
    return {"tools": [tool.model_dump() for tool in tools]}

@app.post("/tools/call")
async def call_tool(request: dict):
    name = request.get("name")
    arguments = request.get("arguments", {})
    
    if not name:
        raise HTTPException(status_code=400, detail="Tool name is required")
    
    try:
        result = await handle_call_tool(name, arguments)
        return {"result": [content.model_dump() for content in result]}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def main_cli():
    """CLI entry point for the package."""
    # Get host and port from environment variables or use defaults
    host = os.getenv("MCP_HOST", "127.0.0.1")
    port = int(os.getenv("MCP_PORT", "3000"))
    
    logger.info(f"Starting DevTools AI Mock MCP server on http://{host}:{port}")
    uvicorn.run(app, host=host, port=port, log_level="info")

if __name__ == "__main__":
    main_cli()
