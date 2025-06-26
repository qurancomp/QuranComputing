import json
import os
from termcolor import colored
from typing import Dict, Any

# Configuration
USER_PREFERENCES_FILE = "user_preferences.json"

class UserPreferences:
    """Manages user preferences and settings"""
    
    def __init__(self):
        self.preferences_file = USER_PREFERENCES_FILE
        self.default_preferences = {
            'language': 'ar',  # Default to Arabic
            'theme': 'dark',
            'notifications': True,
            'form_autosave': True,
            'last_selected_form': None,
            'ui_density': 'normal',
            'rtl_support': True
        }
        self.load_preferences()
        
    def load_preferences(self) -> Dict[str, Any]:
        """Load user preferences from file"""
        try:
            if os.path.exists(self.preferences_file):
                with open(self.preferences_file, 'r', encoding='utf-8') as f:
                    loaded_preferences = json.load(f)
                    # Merge with defaults to ensure all keys exist
                    self.preferences = {**self.default_preferences, **loaded_preferences}
                    print(colored(f"✅ User preferences loaded successfully", "green"))
            else:
                self.preferences = self.default_preferences.copy()
                print(colored(f"ℹ️ Creating new preferences file with defaults", "yellow"))
                self.save_preferences()
        except Exception as e:
            print(colored(f"❌ Error loading preferences: {e}", "red"))
            print(colored(f"Using default preferences", "yellow"))
            self.preferences = self.default_preferences.copy()
        
        return self.preferences
    
    def save_preferences(self) -> bool:
        """Save user preferences to file"""
        try:
            with open(self.preferences_file, 'w', encoding='utf-8') as f:
                json.dump(self.preferences, f, ensure_ascii=False, indent=2)
            print(colored(f"✅ User preferences saved successfully", "green"))
            return True
        except Exception as e:
            print(colored(f"❌ Error saving preferences: {e}", "red"))
            return False
    
    def get_preference(self, key: str, default=None):
        """Get a specific preference value"""
        return self.preferences.get(key, default)
    
    def set_preference(self, key: str, value: Any) -> bool:
        """Set a preference value and save"""
        try:
            self.preferences[key] = value
            return self.save_preferences()
        except Exception as e:
            print(colored(f"❌ Error setting preference {key}: {e}", "red"))
            return False
    
    def get_language(self) -> str:
        """Get current language preference"""
        return self.preferences.get('language', 'ar')
    
    def set_language(self, language: str) -> bool:
        """Set language preference"""
        if language in ['en', 'ar']:
            return self.set_preference('language', language)
        else:
            print(colored(f"❌ Invalid language: {language}. Use 'en' or 'ar'", "red"))
            return False
    
    def get_theme(self) -> str:
        """Get current theme preference"""
        return self.preferences.get('theme', 'dark')
    
    def set_theme(self, theme: str) -> bool:
        """Set theme preference"""
        return self.set_preference('theme', theme)
    
    def get_last_form(self) -> str:
        """Get last selected form"""
        return self.preferences.get('last_selected_form', None)
    
    def set_last_form(self, form_name: str) -> bool:
        """Set last selected form"""
        return self.set_preference('last_selected_form', form_name)
    
    def reset_to_defaults(self) -> bool:
        """Reset all preferences to defaults"""
        try:
            self.preferences = self.default_preferences.copy()
            return self.save_preferences()
        except Exception as e:
            print(colored(f"❌ Error resetting preferences: {e}", "red"))
            return False
    
    def export_preferences(self, filepath: str) -> bool:
        """Export preferences to a specific file"""
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.preferences, f, ensure_ascii=False, indent=2)
            print(colored(f"✅ Preferences exported to {filepath}", "green"))
            return True
        except Exception as e:
            print(colored(f"❌ Error exporting preferences: {e}", "red"))
            return False
    
    def import_preferences(self, filepath: str) -> bool:
        """Import preferences from a specific file"""
        try:
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    imported_preferences = json.load(f)
                    # Validate and merge with defaults
                    self.preferences = {**self.default_preferences, **imported_preferences}
                    self.save_preferences()
                    print(colored(f"✅ Preferences imported from {filepath}", "green"))
                    return True
            else:
                print(colored(f"❌ File not found: {filepath}", "red"))
                return False
        except Exception as e:
            print(colored(f"❌ Error importing preferences: {e}", "red"))
            return False 