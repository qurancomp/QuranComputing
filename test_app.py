#!/usr/bin/env python3
"""
Test script to verify Streamlit app functionality
"""

import os
import sys
from termcolor import colored

def test_imports():
    """Test that all required modules can be imported"""
    print(colored("🧪 Testing imports...", "cyan"))
    
    try:
        # Test core imports
        import streamlit as st
        print(colored("✅ Streamlit imported successfully", "green"))
        
        # Test custom module imports
        from src.content_manager import ContentManager
        print(colored("✅ ContentManager imported successfully", "green"))
        
        from src.forms_manager import FormsManager
        print(colored("✅ FormsManager imported successfully", "green"))
        
        from src.database import Database
        print(colored("✅ Database imported successfully", "green"))
        
        from src.ui_utils import get_text, apply_language_styles, get_language_direction
        print(colored("✅ UI utils imported successfully", "green"))
        
        return True
        
    except ImportError as e:
        print(colored(f"❌ Import error: {e}", "red"))
        return False

def test_content_manager():
    """Test ContentManager functionality"""
    print(colored("\n🧪 Testing ContentManager...", "cyan"))
    
    try:
        from src.content_manager import ContentManager
        cm = ContentManager()
        
        # Test English content
        home_en = cm.get_content("home", "en")
        print(colored(f"✅ English home content loaded: {home_en['title'][:50]}...", "green"))
        
        # Test Arabic content
        home_ar = cm.get_content("home", "ar")
        print(colored(f"✅ Arabic home content loaded: {home_ar['title'][:50]}...", "green"))
        
        return True
        
    except Exception as e:
        print(colored(f"❌ ContentManager error: {e}", "red"))
        return False

def test_ui_utils():
    """Test UI utils functionality"""
    print(colored("\n🧪 Testing UI utils...", "cyan"))
    
    try:
        from src.ui_utils import get_text, get_language_direction
        
        # Test English translations
        english_text = get_text("home", "en")
        print(colored(f"✅ English translation: {english_text}", "green"))
        
        # Test Arabic translations
        arabic_text = get_text("home", "ar")
        print(colored(f"✅ Arabic translation: {arabic_text}", "green"))
        
        # Test language direction
        en_dir = get_language_direction("en")
        ar_dir = get_language_direction("ar")
        print(colored(f"✅ Language directions - EN: {en_dir}, AR: {ar_dir}", "green"))
        
        return True
        
    except Exception as e:
        print(colored(f"❌ UI utils error: {e}", "red"))
        return False

def main():
    """Run all tests"""
    print(colored("🚀 Starting Streamlit app tests...", "blue"))
    
    tests = [
        test_imports,
        test_content_manager,
        test_ui_utils
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(colored(f"\n📊 Test Results: {passed}/{total} tests passed", "blue"))
    
    if passed == total:
        print(colored("🎉 All tests passed! The app should work correctly.", "green"))
        return True
    else:
        print(colored("❌ Some tests failed. Please check the errors above.", "red"))
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 