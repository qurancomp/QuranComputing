"""
Quran Institute Streamlit Application - Deployment Entry Point
Main application file for Streamlit Cloud deployment.

Note: Streamlit Cloud should be configured to run src/main.py directly.
This file is kept for local development compatibility.
"""

import sys
import os

# Add the src directory to the Python path for local development
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.insert(0, src_dir)

# Import and run the main application
from main import main

if __name__ == "__main__":
    main() 