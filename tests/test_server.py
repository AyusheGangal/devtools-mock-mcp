#!/usr/bin/env python3
"""
Test script for DevTools AI Mock MCP Server
"""
import asyncio
import unittest
from devtools_ai_mock_mcp.server import (
    initiate_session, get_workflow, get_toolchain, 
    get_tool, generate_command, confirm_command, get_session_status
)

class TestDevToolsAIMockMCP(unittest.TestCase):
    """Test cases for the MCP server functionality."""
    
    async def test_initiate_session(self):
        """Test session initiation."""
        result = await initiate_session({
            "question": "I need to create a new MATLAB sandbox"
        })
        self.assertEqual(len(result), 1)
        self.assertIn("Session initiated successfully", result[0].text)
    
    async def test_workflow_selection(self):
        """Test workflow selection."""
        # First initiate a session
        await initiate_session({
            "question": "I need to create a new MATLAB sandbox"
        })
        
        # Then get workflow
        result = await get_workflow({"session_id": "session_1"})
        self.assertEqual(len(result), 1)
        self.assertIn("Workflow Selected", result[0].text)

if __name__ == "__main__":
    # Run async tests
    unittest.main()
