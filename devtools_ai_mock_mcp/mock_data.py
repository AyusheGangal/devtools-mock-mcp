"""
Mock data for DevTools AI MCP Server

This module contains mock data representing the workflows, toolchains, tools,
and commands available in the MathWorks development environment.
"""

# Mock workflows available in the system
WORKFLOWS = {
    "Development Environment Setup": {
        "description": "Set up development environments, sandboxes, and workspaces",
        "common_tasks": [
            "Create new sandbox",
            "Set up development environment",
            "Configure workspace",
            "Initialize project structure"
        ],
        "toolchains": [
            "MATLAB Build Tools",
            "Source Control Tools",
            "Environment Setup Tools"
        ]
    },
    "Testing and Validation": {
        "description": "Run tests, validate code, and ensure quality",
        "common_tasks": [
            "Run unit tests",
            "Execute integration tests",
            "Validate code quality",
            "Generate test reports"
        ],
        "toolchains": [
            "Testing Framework",
            "Quality Assurance Tools",
            "MATLAB Test Tools"
        ]
    },
    "Deployment and Release": {
        "description": "Deploy applications and manage releases",
        "common_tasks": [
            "Deploy to staging",
            "Create release packages",
            "Publish applications",
            "Manage versions"
        ],
        "toolchains": [
            "Deployment Tools",
            "Release Management",
            "Package Management"
        ]
    },
    "Debugging and Troubleshooting": {
        "description": "Debug issues and troubleshoot problems",
        "common_tasks": [
            "Debug applications",
            "Analyze logs",
            "Profile performance",
            "Fix runtime issues"
        ],
        "toolchains": [
            "Debugging Tools",
            "Analysis Tools",
            "Profiling Tools"
        ]
    },
    "General Development": {
        "description": "General development tasks and utilities",
        "common_tasks": [
            "Code compilation",
            "Documentation generation",
            "File management",
            "General utilities"
        ],
        "toolchains": [
            "Development Utilities",
            "MATLAB Build Tools",
            "Documentation Tools"
        ]
    }
}

# Mock toolchains available in the system
TOOLCHAINS = {
    "MATLAB Build Tools": {
        "description": "Tools for building and compiling MATLAB applications",
        "tools": [
            "mw_build",
            "mw_compile",
            "mw_package",
            "mw_create_sandbox"
        ]
    },
    "Source Control Tools": {
        "description": "Version control and source code management tools",
        "tools": [
            "mw_git",
            "mw_branch",
            "mw_merge",
            "mw_commit"
        ]
    },
    "Environment Setup Tools": {
        "description": "Tools for setting up development environments",
        "tools": [
            "mw_create_sandbox",
            "mw_setup_env",
            "mw_configure",
            "mw_init_workspace"
        ]
    },
    "Testing Framework": {
        "description": "Comprehensive testing tools and frameworks",
        "tools": [
            "mw_test",
            "mw_unit_test",
            "mw_integration_test",
            "mw_test_report"
        ]
    },
    "Quality Assurance Tools": {
        "description": "Code quality and analysis tools",
        "tools": [
            "mw_lint",
            "mw_analyze",
            "mw_quality_check",
            "mw_code_review"
        ]
    },
    "MATLAB Test Tools": {
        "description": "MATLAB-specific testing utilities",
        "tools": [
            "mw_matlab_test",
            "mw_simulink_test",
            "mw_test_coverage",
            "mw_test_harness"
        ]
    },
    "Deployment Tools": {
        "description": "Application deployment and distribution tools",
        "tools": [
            "mw_deploy",
            "mw_distribute",
            "mw_publish",
            "mw_stage"
        ]
    },
    "Release Management": {
        "description": "Release planning and management tools",
        "tools": [
            "mw_release",
            "mw_version",
            "mw_tag",
            "mw_package_release"
        ]
    },
    "Package Management": {
        "description": "Package creation and management tools",
        "tools": [
            "mw_create_package",
            "mw_install_package",
            "mw_update_package",
            "mw_list_packages"
        ]
    },
    "Debugging Tools": {
        "description": "Debugging and diagnostic tools",
        "tools": [
            "mw_debug",
            "mw_trace",
            "mw_breakpoint",
            "mw_inspect"
        ]
    },
    "Analysis Tools": {
        "description": "Code and performance analysis tools",
        "tools": [
            "mw_analyze",
            "mw_profile",
            "mw_metrics",
            "mw_dependency_check"
        ]
    },
    "Profiling Tools": {
        "description": "Performance profiling and optimization tools",
        "tools": [
            "mw_profile",
            "mw_benchmark",
            "mw_memory_check",
            "mw_performance_test"
        ]
    },
    "Development Utilities": {
        "description": "General development utilities and helpers",
        "tools": [
            "mw_help",
            "mw_info",
            "mw_clean",
            "mw_utilities"
        ]
    },
    "Documentation Tools": {
        "description": "Documentation generation and management tools",
        "tools": [
            "mw_doc_gen",
            "mw_help_gen",
            "mw_api_doc",
            "mw_user_guide"
        ]
    }
}

# Mock tools with their descriptions and usage
TOOLS = {
    "mw_create_sandbox": {
        "description": "Create a new development sandbox environment",
        "usage": "mw_create_sandbox [options] [snapshot_name]",
        "doc_url": "https://example.com/help/mw_create_sandbox",
        "examples": [
            "mw_create_sandbox",
            "mw_create_sandbox --snapshot my_snapshot",
            "mw_create_sandbox --clean --snapshot stable_build"
        ]
    },
    "mw_build": {
        "description": "Build and compile MATLAB applications",
        "usage": "mw_build [target] [options]",
        "doc_url": "https://example.com/help/mw_build",
        "examples": [
            "mw_build",
            "mw_build --target release",
            "mw_build --clean --parallel"
        ]
    },
    "mw_test": {
        "description": "Run tests for MATLAB applications",
        "usage": "mw_test [test_suite] [options]",
        "doc_url": "https://example.com/help/mw_test",
        "examples": [
            "mw_test",
            "mw_test --suite unit",
            "mw_test --coverage --report"
        ]
    },
    "mw_deploy": {
        "description": "Deploy applications to target environments",
        "usage": "mw_deploy [environment] [options]",
        "doc_url": "https://example.com/help/mw_deploy",
        "examples": [
            "mw_deploy staging",
            "mw_deploy production --validate",
            "mw_deploy --dry-run staging"
        ]
    },
    "mw_git": {
        "description": "Git operations integrated with MathWorks tools",
        "usage": "mw_git [git_command] [options]",
        "doc_url": "https://example.com/help/mw_git",
        "examples": [
            "mw_git status",
            "mw_git commit -m 'message'",
            "mw_git push origin main"
        ]
    },
    "mw_analyze": {
        "description": "Analyze code quality and performance",
        "usage": "mw_analyze [target] [options]",
        "doc_url": "https://example.com/help/mw_analyze",
        "examples": [
            "mw_analyze .",
            "mw_analyze --performance src/",
            "mw_analyze --quality --report"
        ]
    },
    "mw_help": {
        "description": "Get help for MathWorks tools",
        "usage": "mw_help [tool_name]",
        "doc_url": "https://example.com/help/mw_help",
        "examples": [
            "mw_help",
            "mw_help mw_build",
            "mw_help --list-tools"
        ]
    },
    "mw_compile": {
        "description": "Compile MATLAB code and dependencies",
        "usage": "mw_compile [source] [options]",
        "doc_url": "https://example.com/help/mw_compile",
        "examples": [
            "mw_compile main.m",
            "mw_compile --optimize src/",
            "mw_compile --target mex"
        ]
    },
    "mw_setup_env": {
        "description": "Set up development environment and paths",
        "usage": "mw_setup_env [profile] [options]",
        "doc_url": "https://example.com/help/mw_setup_env",
        "examples": [
            "mw_setup_env",
            "mw_setup_env --profile development",
            "mw_setup_env --reset --clean"
        ]
    },
    "mw_profile": {
        "description": "Profile application performance",
        "usage": "mw_profile [target] [options]",
        "doc_url": "https://example.com/help/mw_profile",
        "examples": [
            "mw_profile main.m",
            "mw_profile --memory --detailed",
            "mw_profile --benchmark tests/"
        ]
    },
    # Additional tools from toolchains
    "mw_package": {
        "description": "Package MATLAB applications for distribution",
        "usage": "mw_package [source] [options]",
        "doc_url": "https://example.com/help/mw_package",
        "examples": [
            "mw_package app/",
            "mw_package --format installer",
            "mw_package --output dist/"
        ]
    },
    "mw_branch": {
        "description": "Branch management for MathWorks repositories",
        "usage": "mw_branch [action] [branch_name]",
        "doc_url": "https://example.com/help/mw_branch",
        "examples": [
            "mw_branch create feature-branch",
            "mw_branch switch main",
            "mw_branch delete old-feature"
        ]
    },
    "mw_merge": {
        "description": "Merge branches in MathWorks repositories",
        "usage": "mw_merge [source_branch] [options]",
        "doc_url": "https://mathworks.com/help/mw_merge",
        "examples": [
            "mw_merge feature-branch",
            "mw_merge --no-ff feature-branch",
            "mw_merge --squash feature-branch"
        ]
    },
    "mw_commit": {
        "description": "Commit changes with MathWorks standards",
        "usage": "mw_commit [options] [message]",
        "doc_url": "https://example.com/help/mw_commit",
        "examples": [
            "mw_commit -m 'Fix bug in parser'",
            "mw_commit --amend",
            "mw_commit --staged -m 'Update documentation'"
        ]
    },
    "mw_configure": {
        "description": "Configure MathWorks development environment",
        "usage": "mw_configure [component] [options]",
        "doc_url": "https://example.com/help/mw_configure",
        "examples": [
            "mw_configure matlab",
            "mw_configure --reset-all",
            "mw_configure paths --add /custom/path"
        ]
    },
    "mw_init_workspace": {
        "description": "Initialize a new MathWorks workspace",
        "usage": "mw_init_workspace [workspace_name] [options]",
        "doc_url": "https://example.com/help/mw_init_workspace",
        "examples": [
            "mw_init_workspace myproject",
            "mw_init_workspace --template matlab-app",
            "mw_init_workspace --git-init myproject"
        ]
    },
    "mw_unit_test": {
        "description": "Run unit tests for MATLAB code",
        "usage": "mw_unit_test [test_path] [options]",
        "doc_url": "https://example.com/help/mw_unit_test",
        "examples": [
            "mw_unit_test tests/unit/",
            "mw_unit_test --coverage",
            "mw_unit_test --parallel --verbose"
        ]
    },
    "mw_integration_test": {
        "description": "Run integration tests",
        "usage": "mw_integration_test [test_suite] [options]",
        "doc_url": "https://example.com/help/mw_integration_test",
        "examples": [
            "mw_integration_test",
            "mw_integration_test --environment staging",
            "mw_integration_test --timeout 3600"
        ]
    },
    "mw_test_report": {
        "description": "Generate test reports and coverage",
        "usage": "mw_test_report [options]",
        "doc_url": "https://example.com/help/mw_test_report",
        "examples": [
            "mw_test_report",
            "mw_test_report --format html",
            "mw_test_report --output reports/"
        ]
    }
}

# Mock command templates for different scenarios
COMMANDS = {
    "mw_create_sandbox": {
        "default": "mw_create_sandbox",
        "with_snapshot": "mw_create_sandbox --snapshot {snapshot_name}",
        "clean": "mw_create_sandbox --clean",
        "with_options": "mw_create_sandbox --snapshot {snapshot_name} --clean --verbose"
    },
    "mw_build": {
        "default": "mw_build",
        "release": "mw_build --target release",
        "debug": "mw_build --target debug",
        "clean": "mw_build --clean --parallel"
    },
    "mw_test": {
        "default": "mw_test",
        "unit": "mw_test --suite unit",
        "integration": "mw_test --suite integration",
        "coverage": "mw_test --coverage --report",
        "parallel": "mw_test --parallel --verbose"
    },
    "mw_deploy": {
        "default": "mw_deploy",
        "staging": "mw_deploy staging",
        "production": "mw_deploy production --validate",
        "dry_run": "mw_deploy --dry-run staging"
    },
    "mw_git": {
        "default": "mw_git status",
        "commit": "mw_git commit -m '{message}'",
        "push": "mw_git push origin {branch}",
        "pull": "mw_git pull origin {branch}"
    },
    "mw_analyze": {
        "default": "mw_analyze .",
        "performance": "mw_analyze --performance {target}",
        "quality": "mw_analyze --quality --report",
        "detailed": "mw_analyze --detailed --output reports/"
    },
    "mw_help": {
        "default": "mw_help",
        "tool_specific": "mw_help {tool_name}",
        "list_tools": "mw_help --list-tools",
        "verbose": "mw_help --verbose {tool_name}"
    },
    "mw_compile": {
        "default": "mw_compile {source}",
        "optimize": "mw_compile --optimize {source}",
        "mex": "mw_compile --target mex {source}",
        "parallel": "mw_compile --parallel {source}"
    },
    "mw_setup_env": {
        "default": "mw_setup_env",
        "profile": "mw_setup_env --profile {profile_name}",
        "reset": "mw_setup_env --reset --clean",
        "configure": "mw_setup_env --configure {component}"
    },
    "mw_profile": {
        "default": "mw_profile {target}",
        "memory": "mw_profile --memory --detailed {target}",
        "benchmark": "mw_profile --benchmark {target}",
        "report": "mw_profile --report --output {output_dir} {target}"
    }
}

# Additional mock data for enhanced functionality
ENVIRONMENTS = {
    "development": {
        "description": "Development environment for active coding",
        "tools": ["mw_create_sandbox", "mw_build", "mw_test", "mw_git"]
    },
    "testing": {
        "description": "Testing environment for validation",
        "tools": ["mw_test", "mw_unit_test", "mw_integration_test", "mw_test_report"]
    },
    "staging": {
        "description": "Staging environment for pre-production testing",
        "tools": ["mw_deploy", "mw_test", "mw_analyze"]
    },
    "production": {
        "description": "Production environment for live deployments",
        "tools": ["mw_deploy", "mw_release", "mw_package"]
    }
}

COMMON_PATTERNS = {
    "create_sandbox": ["create", "new", "sandbox", "environment", "setup"],
    "build_compile": ["build", "compile", "make", "package"],
    "test_validate": ["test", "check", "validate", "verify", "run"],
    "deploy_release": ["deploy", "release", "publish", "distribute"],
    "debug_analyze": ["debug", "analyze", "profile", "troubleshoot", "fix"],
    "git_version": ["git", "commit", "push", "pull", "branch", "merge"],
    "help_info": ["help", "info", "documentation", "guide", "how"]
}
