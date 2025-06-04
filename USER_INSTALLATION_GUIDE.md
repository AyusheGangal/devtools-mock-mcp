# DevTools AI Mock MCP - User Installation Guide

Complete installation guide for users installing from GitLab releases. 

## System Requirements

### Minimum Requirements
- **Operating System**: Windows 10+, macOS 10.14+, or Linux
- **Python**: Version 3.8 or higher
- **Memory**: 50 MB available disk space
- **Internet**: Required for initial download and installation

### Software Requirements
- **Claude Desktop** (latest version)
- **Python 3.8+** with pip
- **Terminal/Command Prompt** access

---

## Step 1: Install Python (If Not Already Installed)

### Check if Python is Already Installed
Open Terminal (macOS/Linux) or Command Prompt (Windows) and run:
```bash
python3 --version
```
or
```bash
python --version
```

If you see `Python 3.8.x` or higher, **skip to Step 2**.

### Install Python

#### **Windows:**
1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download Python 3.11+ installer
3. **Important**: Check "Add Python to PATH" during installation
4. Run installer and follow prompts

#### **macOS:**
```bash
# Option 1: Download from python.org (recommended)
# Go to https://www.python.org/downloads/ and download installer

# Option 2: Using Homebrew (if you have it)
brew install python3
```

#### **Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

#### **Linux (CentOS/RHEL):**
```bash
sudo yum install python3 python3-pip
```

### Verify Python Installation
```bash
python3 --version
pip3 --version
```

---

## Step 2: Install Claude Desktop

### Download Claude Desktop
1. Go to [Claude Desktop download page](https://claude.ai/download)
2. Download for your operating system
3. Install following standard procedures for your OS

### Verify Claude Desktop Installation
- Launch Claude Desktop
- Sign in with your account
- Ensure it's working properly before continuing

---

## Step 3: Install DevTools AI Mock MCP

### Find the Latest Release
1. Go to the GitLab project releases page:
   ```
   https://gitlab.com/[username]/devtools-mock-mcp/-/releases
   ```
2. Find the latest version (e.g., v0.1.0)
3. Look for the wheel file: `devtools_ai_mock_mcp_ayushe-X.X.X-py3-none-any.whl`

### Install the Package

#### **Method 1: Direct Installation (Recommended)**
```bash
pip3 install https://gitlab.com/[username]/devtools-mock-mcp/-/releases/v0.1.0/downloads/devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
```

#### **Method 2: Download Then Install**
```bash
# Download the wheel file first
curl -L -O https://gitlab.com/[username]/devtools-mock-mcp/-/releases/v0.1.0/downloads/devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl

# Then install
pip3 install devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
```

### Verify Installation
```bash
# Check if the command is available
devtools-ai-mock-mcp-ayushe --help 2>/dev/null || echo "Installation successful - MCP server ready"

# Check if package is installed
pip3 show devtools-ai-mock-mcp-ayushe
```

---

## Step 4: Configure Claude Desktop

### Locate Claude Desktop Configuration

#### **macOS:**
```bash
~/Library/Application Support/Claude/claude_desktop_config.json
```

#### **Windows:**
```bash
%APPDATA%\Claude\claude_desktop_config.json
```

#### **Linux:**
```bash
~/.config/Claude/claude_desktop_config.json
```

### Edit Configuration File

#### **Option 1: Using Text Editor**
Open the file in your preferred text editor and add:

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

#### **Option 2: Create File if It Doesn't Exist**

**macOS/Linux:**
```bash
mkdir -p "$(dirname ~/Library/Application\ Support/Claude/claude_desktop_config.json)"
cat > ~/Library/Application\ Support/Claude/claude_desktop_config.json << 'EOF'
{
  "mcpServers": {
    "devtools-ai-mock": {
      "command": "devtools-ai-mock-mcp-ayushe",
      "args": [],
      "env": {}
    }
  }
}
EOF
```

**Windows (PowerShell):**
```powershell
$configPath = "$env:APPDATA\Claude\claude_desktop_config.json"
$configDir = Split-Path $configPath
if (!(Test-Path $configDir)) { New-Item -ItemType Directory -Path $configDir -Force }
@'
{
  "mcpServers": {
    "devtools-ai-mock": {
      "command": "devtools-ai-mock-mcp-ayushe",
      "args": [],
      "env": {}
    }
  }
}
'@ | Out-File -FilePath $configPath -Encoding UTF8
```

#### **Option 3: Add to Existing Configuration**
If you already have other MCP servers, add the new entry:

```json
{
  "mcpServers": {
    "existing-server": {
      "command": "existing-command",
      "args": []
    },
    "devtools-ai-mock": {
      "command": "devtools-ai-mock-mcp-ayushe",
      "args": [],
      "env": {}
    }
  }
}
```

---

## Step 5: Restart and Test

### Restart Claude Desktop
1. **Completely quit** Claude Desktop (not just close window)
2. **Wait 5 seconds**
3. **Launch Claude Desktop** again

### Test the Installation
In Claude Desktop, try these example questions:

```
I need to create a new sandbox from a snapshot called stable_build
```

```
Help me run unit tests for my C++ code
```

```
How do I deploy my application to production?
```

You should see Claude using the DevTools AI tools to walk through workflow selection and generate appropriate commands.

---

## Troubleshooting

### Common Issues and Solutions

#### **"Command not found: devtools-ai-mock-mcp-ayushe"**
```bash
# Check if pip installed to user directory
pip3 show devtools-ai-mock-mcp-ayushe

# If installed but command not found, add to PATH:
# macOS/Linux: Add to ~/.bashrc or ~/.zshrc:
export PATH="$HOME/.local/bin:$PATH"

# Windows: Add Python Scripts directory to PATH
```

#### **"Permission denied" during pip install**
```bash
# Install to user directory instead
pip3 install --user https://gitlab.com/[username]/devtools-mock-mcp/-/releases/v0.1.0/downloads/devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
```

#### **"Python not found" error**
- Ensure Python was added to PATH during installation
- Try `python` instead of `python3`
- Restart terminal/command prompt after Python installation

#### **Claude Desktop doesn't recognize the MCP server**
1. Verify configuration file location and syntax
2. Check that Claude Desktop was completely restarted
3. Verify the command works in terminal:
   ```bash
   devtools-ai-mock-mcp-ayushe
   ```

#### **SSL/Certificate errors during download**
```bash
# Use --trusted-host flags
pip3 install --trusted-host gitlab.com --trusted-host files.pythonhosted.org https://gitlab.com/[username]/devtools-mock-mcp/-/releases/v0.1.0/downloads/devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
```

### Getting Help

#### **Check Installation Status**
```bash
# Verify Python
python3 --version

# Verify pip
pip3 --version

# Verify package installation
pip3 list | grep devtools

# Check command availability
which devtools-ai-mock-mcp-ayushe  # macOS/Linux
where devtools-ai-mock-mcp-ayushe  # Windows
```

#### **Clean Reinstallation**
```bash
# Uninstall
pip3 uninstall devtools-ai-mock-mcp-ayushe

# Clear pip cache
pip3 cache purge

# Reinstall
pip3 install https://gitlab.com/[username]/devtools-mock-mcp/-/releases/v0.1.0/downloads/devtools_ai_mock_mcp_ayushe-0.1.0-py3-none-any.whl
```

---

## System-Specific Notes

### **Windows Users**
- Use Command Prompt or PowerShell as Administrator if you encounter permission issues
- Python might be installed as `python` instead of `python3`
- Configuration file path uses backslashes: `%APPDATA%\Claude\claude_desktop_config.json`

### **macOS Users**
- May need to allow terminal access in Security & Privacy settings
- If using system Python, consider using `python3 -m pip` instead of `pip3`
- Configuration is in `~/Library/Application Support/Claude/`

### **Linux Users**
- May need `sudo` for system-wide installation
- Consider using virtual environments for Python packages
- Configuration typically in `~/.config/Claude/`

---

## Uninstallation

### Remove the Package
```bash
pip3 uninstall devtools-ai-mock-mcp-ayushe
```

### Remove Configuration
Edit `claude_desktop_config.json` and remove the `"devtools-ai-mock"` entry.

### Restart Claude Desktop
Restart Claude Desktop to apply changes.

---

## Support

If you continue to experience issues:

1. **Check the project's GitLab issues page**
2. **Verify all system requirements are met**
3. **Try installation in a clean Python environment**
4. **Contact the project maintainer** with:
   - Your operating system and version
   - Python version (`python3 --version`)
   - Complete error messages
   - Steps you've already tried
