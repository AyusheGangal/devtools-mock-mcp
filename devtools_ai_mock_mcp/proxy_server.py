#!/usr/bin/env python3
"""
Proxy Server for DevTools AI Mock MCP

This proxy server bridges Claude Desktop (stdio) to the HTTP FastMCP server,
allowing Claude Desktop to connect to HTTP-based MCP servers.
"""

import subprocess
import sys
import time
import httpx
import asyncio
from fastmcp import FastMCP

# URL of the HTTP server to proxy to
HTTP_SERVER_URL = "http://127.0.0.1:8001/mcp"

async def ensure_http_server_running():
    """Ensure the HTTP server is running, start it if needed."""
    try:
        # Check if server is already running
        async with httpx.AsyncClient() as client:
            response = await client.get(HTTP_SERVER_URL.replace('/mcp', '/'))
            if response.status_code in [200, 404]:  # Server is responding
                return None
    except:
        pass
    
    # Server not running, start it
    import os
    server_script = os.path.join(os.path.dirname(__file__), "fastmcp_server.py")
    process = subprocess.Popen(
        [sys.executable, server_script],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    
    # Wait for server to start (max 30 seconds)
    for _ in range(60):  # 30 seconds with 0.5s intervals
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(HTTP_SERVER_URL.replace('/mcp', '/'))
                if response.status_code in [200, 404]:
                    print(f"HTTP server started successfully on {HTTP_SERVER_URL}", file=sys.stderr)
                    return process
        except:
            await asyncio.sleep(0.5)
    
    print("Failed to start HTTP server", file=sys.stderr)
    return process

async def main():
    """Main function to set up and run the proxy."""
    # Ensure HTTP server is running
    await ensure_http_server_running()
    
    # Wait a bit more to ensure server is fully ready
    await asyncio.sleep(2.0)
    
    # Create proxy server that forwards to HTTP server
    proxy = FastMCP.as_proxy(
        HTTP_SERVER_URL,
        name="devtools-ai-mock-mcp-proxy",
        instructions="Proxy server for DevTools AI Mock MCP (HTTP backend)"
    )
    
    # Run with stdio transport for Claude Desktop
    await proxy.run_async(transport="stdio")

def main_cli():
    """CLI entry point for the proxy server."""
    asyncio.run(main())

if __name__ == "__main__":
    main_cli()
