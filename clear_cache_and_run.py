#!/usr/bin/env python3
"""
Clear Streamlit cache and run the app cleanly
"""

import os
import sys
import shutil
import subprocess
from termcolor import colored

def clear_streamlit_cache():
    """Clear all Streamlit cache directories"""
    print(colored("🧹 Clearing Streamlit cache...", "cyan"))
    
    # Common Streamlit cache locations
    cache_dirs = [
        os.path.expanduser("~/.streamlit"),
        os.path.join(os.getcwd(), ".streamlit"),
        os.path.join(os.getcwd(), "__pycache__"),
        os.path.join(os.getcwd(), "src", "__pycache__"),
    ]
    
    for cache_dir in cache_dirs:
        if os.path.exists(cache_dir):
            try:
                if cache_dir.endswith("__pycache__"):
                    shutil.rmtree(cache_dir)
                    print(colored(f"✅ Removed {cache_dir}", "green"))
                else:
                    # Only clear cache files, not config
                    cache_file = os.path.join(cache_dir, "cache")
                    if os.path.exists(cache_file):
                        shutil.rmtree(cache_file)
                        print(colored(f"✅ Cleared cache in {cache_dir}", "green"))
            except Exception as e:
                print(colored(f"⚠️ Could not clear {cache_dir}: {e}", "yellow"))

def run_streamlit():
    """Run the Streamlit app"""
    print(colored("🚀 Starting Streamlit app...", "blue"))
    
    try:
        subprocess.run([
            "streamlit", "run", "src/main.py", 
            "--server.headless", "false",
            "--server.port", "8501",
            "--server.address", "localhost"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(colored(f"❌ Error running Streamlit: {e}", "red"))
        return False
    except KeyboardInterrupt:
        print(colored("\n👋 Streamlit app stopped by user", "yellow"))
        return True
    
    return True

def main():
    """Main function"""
    print(colored("🔧 Streamlit App Cache Cleaner and Runner", "blue"))
    
    # Clear cache
    clear_streamlit_cache()
    
    # Run the app
    success = run_streamlit()
    
    if success:
        print(colored("✅ App session completed successfully", "green"))
    else:
        print(colored("❌ App session ended with errors", "red"))
        sys.exit(1)

if __name__ == "__main__":
    main() 