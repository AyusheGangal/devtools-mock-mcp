#!/usr/bin/env python3
"""
Setup script for DevTools AI Mock MCP Server package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = [
    "fastmcp>=0.15.0",
    "httpx>=0.28.1"
]

setup(
    name="devtools-ai-mock-mcp-ayushe",
    version="0.1.0",
    author="Ayushe Gangal",
    author_email="ayushe17@gmail.com",
    description="A Model Context Protocol server that mocks DevTools AI functionality for development workflows",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ayushegangal/devtools-mock-mcp",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "devtools-ai-mock-mcp=devtools_ai_mock_mcp.fastmcp_server:main_cli",
            "devtools-ai-mock-mcp-proxy=devtools_ai_mock_mcp.proxy_server:main_cli",
            "devtools-ai-mock-mcp-http=devtools_ai_mock_mcp.fastmcp_server:main_http",
        ],
    },
    package_data={
        "devtools_ai_mock_mcp": ["*.py"],
    },
    include_package_data=True,
)
