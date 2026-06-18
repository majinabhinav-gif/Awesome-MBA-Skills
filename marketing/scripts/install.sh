#!/bin/bash
# Install marketing-research skill for Claude Code
# Usage: ./install.sh [--project]

set -e

SKILL_NAME="marketing-research"
REPO_URL="https://raw.githubusercontent.com/ishwarjha/marketing-research-skill/main"

# Determine install location
if [ "$1" = "--project" ]; then
    INSTALL_DIR=".claude/skills/$SKILL_NAME"
    echo "Installing as project skill in $INSTALL_DIR"
else
    INSTALL_DIR="$HOME/.claude/skills/$SKILL_NAME"
    echo "Installing as personal skill in $INSTALL_DIR"
fi

# Create directory
mkdir -p "$INSTALL_DIR"

# Download SKILL.md
echo "Downloading SKILL.md..."
curl -sSL "$REPO_URL/$SKILL_NAME/SKILL.md" -o "$INSTALL_DIR/SKILL.md"

# Verify
if [ -f "$INSTALL_DIR/SKILL.md" ]; then
    echo ""
    echo "Installed successfully."
    echo "Location: $INSTALL_DIR/SKILL.md"
    echo ""
    echo "To use: start a Claude Code session and say 'research my product'"
    echo "To uninstall: rm -rf $INSTALL_DIR"
else
    echo "Installation failed. Please check your network connection and try again."
    exit 1
fi
