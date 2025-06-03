# Distribution Guide for DevTools AI Mock MCP

## Option 1: GitLab Releases (Recommended for 100s of users)

### Setup:
1. Push your code to GitLab
2. Create a release in GitLab
3. Upload the wheel file as a release asset

### User Installation:
```bash
pip install https://gitlab.com/yourusername/devtools-mock-mcp/-/releases/v0.1.0/downloads/devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
```

### Claude Desktop Config:
```json
{
  "mcpServers": {
    "devtools-ai-mock": {
      "command": "devtools-ai-mock-mcp-ayushe",
      "args": [],
      "env": {}
    }
  }
}
```

### Pros for GitLab:
- ✅ Free hosting for releases
- ✅ Works with private repositories  
- ✅ Good for teams/organizations
- ✅ Built-in CI/CD for automation
- ✅ Handles hundreds of downloads easily
- ✅ Version management

## Option 2: GitHub Releases (Alternative)

Same process but using GitHub instead of GitLab.

### User Installation:
```bash
pip install https://github.com/yourusername/devtools-mock-mcp/releases/download/v0.1.0/devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
```

## Option 3: PyPI (For Public Distribution)

### Pros:
- ✅ Simplest user experience: `pip install devtools-ai-mock-mcp-ayushe`
- ✅ Professional distribution
- ✅ Unlimited scale

### Cons:
- ❌ Package is public
- ❌ Name must be unique globally

## Installation Instructions for Users:

### Step 1: Install Package
Choose one of the pip install commands above

### Step 2: Configure Claude Desktop
Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "devtools-ai-mock": {
      "command": "devtools-ai-mock-mcp-ayushe",
      "args": [],
      "env": {}
    }
  }
}
```

### Step 3: Restart Claude Desktop

### Step 4: Test
Ask Claude: "I need to create a MATLAB sandbox from snapshot stable_build"

## Bandwidth Considerations:

- **Wheel file size**: ~23KB (very small)
- **GitLab.com bandwidth**: Very generous for releases
- **100 users downloading**: ~2.3MB total (negligible)
- **500 users downloading**: ~11.5MB total (still tiny)

GitLab releases can easily handle this scale.
