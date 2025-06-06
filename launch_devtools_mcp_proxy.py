#!/usr/bin/env python3
"""
Universal launcher for devtools-ai-mock-mcp-proxy
Works regardless of Python environment
"""
import subprocess
import sys

if __name__ == "__main__":
    # Try to run the installed console script
    try:
        subprocess.run([sys.executable, "-m", "devtools_ai_mock_mcp.proxy_server"], check=True)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
