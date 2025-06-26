#!/usr/bin/env python3
"""
Simple script to run the Streamlit app
"""

import subprocess
import sys
from termcolor import colored

def main():
    """Run the Streamlit app"""
    print(colored("🚀 Starting Quran Institute Streamlit App...", "blue"))
    
    try:
        # Run the app
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "src/main.py",
            "--server.headless", "false"
        ])
    except KeyboardInterrupt:
        print(colored("\n👋 App stopped by user", "yellow"))
    except Exception as e:
        print(colored(f"❌ Error: {e}", "red"))

if __name__ == "__main__":
    main() 