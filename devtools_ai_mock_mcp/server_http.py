#!/usr/bin/env python3
"""
DevTools AI Mock MCP Server - HTTP Transport

This server provides HTTP transport for the DevTools AI Mock MCP server
using the official MCP FastAPI integration.
"""

import asyncio
import logging
import os
import uvicorn
from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions
import mcp.server.fastapi
from .server import server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("devtools-ai-mock-mcp-http")

def create_app():
    """Create the FastAPI app with MCP integration."""
    app = mcp.server.fastapi.create_app(
        server,
        InitializationOptions(
            server_name="devtools-ai-mock-mcp",
            server_version="0.1.0",
            capabilities=server.get_capabilities(
                notification_options=NotificationOptions(),
                experimental_capabilities={}
            )
        )
    )
    return app

def main_http():
    """Main function to run the HTTP MCP server."""
    # Get host and port from environment variables or use defaults
    host = os.getenv("MCP_HOST", "127.0.0.1")
    port = int(os.getenv("MCP_PORT", "3000"))
    
    logger.info(f"Starting DevTools AI Mock MCP server on http://{host}:{port}")
    
    # Create the app
    app = create_app()
    
    # Run the server
    uvicorn.run(
        app,
        host=host,
        port=port,
        log_level="info"
    )

if __name__ == "__main__":
    main_http()
