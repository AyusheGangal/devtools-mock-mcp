#!/usr/bin/env python3
"""
HTTP Server Launcher for Claude Desktop

This script starts the FastMCP server with HTTP transport and then
acts as a proxy between Claude Desktop (stdio) and the HTTP server.
"""

import asyncio
import json
import sys
import time
import httpx
from typing import Any, Dict
import subprocess
import signal
import os

# URL where the HTTP server will be running
HTTP_SERVER_URL = "http://127.0.0.1:8001/mcp"

async def start_http_server():
    """Start the HTTP server in background"""
    import subprocess
    import sys
    import os
    
    # Start the HTTP server
    server_script = os.path.join(os.path.dirname(__file__), "fastmcp_server.py")
    process = subprocess.Popen([sys.executable, server_script])
    
    # Wait for server to start
    max_attempts = 30
    for _ in range(max_attempts):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(HTTP_SERVER_URL.replace('/mcp', '/health'))
                if response.status_code in [200, 404]:  # 404 is OK, means server is up
                    return process
        except:
            await asyncio.sleep(0.5)
    
    return process

async def forward_request(request_data: Dict[str, Any]) -> Dict[str, Any]:
    """Forward request to HTTP server and return response"""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                HTTP_SERVER_URL,
                json=request_data,
                headers={"Content-Type": "application/json"},
                timeout=30.0
            )
            return response.json()
        except Exception as e:
            return {
                "jsonrpc": "2.0",
                "id": request_data.get("id"),
                "error": {
                    "code": -32603,
                    "message": f"HTTP server error: {str(e)}"
                }
            }

async def main():
    """Main stdio proxy loop"""
    # Start HTTP server
    server_process = await start_http_server()
    
    try:
        # Handle stdio communication
        while True:
            try:
                # Read from stdin
                line = await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)
                if not line:
                    break
                
                request_data = json.loads(line.strip())
                
                # Forward to HTTP server
                response = await forward_request(request_data)
                
                # Write response to stdout
                print(json.dumps(response))
                sys.stdout.flush()
                
            except json.JSONDecodeError:
                continue
            except Exception as e:
                error_response = {
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {
                        "code": -32700,
                        "message": f"Parse error: {str(e)}"
                    }
                }
                print(json.dumps(error_response))
                sys.stdout.flush()
    
    finally:
        # Clean up server process
        if server_process:
            server_process.terminate()
            server_process.wait()

if __name__ == "__main__":
    asyncio.run(main())
