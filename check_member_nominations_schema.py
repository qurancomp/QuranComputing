#!/usr/bin/env python3
"""
Check and fix member_nominations table schema
"""

import os
import sys
import toml
from datetime import datetime

# Add src directory to Python path
sys.path.append('src')

try:
    from termcolor import colored
    print("✅ termcolor imported successfully")
except ImportError as e:
    print(f"❌ termcolor not available: {e}")
    def colored(text, color=None):
        return text

# Load secrets from secrets.toml for local testing
try:
    with open('secrets.toml', 'r') as f:
        secrets = toml.load(f)
    
    # Set environment variables for Turso
    os.environ['TURSO_DATABASE_URL'] = secrets['turso']['database_url']
    os.environ['TURSO_AUTH_TOKEN'] = secrets['turso']['auth_token']
    print(colored("✅ Turso credentials loaded from secrets.toml", "green"))
except Exception as e:
    print(colored(f"❌ Could not load secrets.toml: {e}", "red"))

try:
    from database_turso import TursoDatabase
    print(colored("✅ Turso modules imported successfully", "green"))
except Exception as e:
    print(colored(f"❌ Error importing Turso modules: {e}", "red"))
    sys.exit(1)

def check_and_fix_member_nominations():
    """Check and fix member_nominations table schema"""
    print(colored("\n🔍 Checking member_nominations table schema...", "cyan"))
    
    try:
        # Initialize database with credentials from environment
        database_url = os.environ.get('TURSO_DATABASE_URL')
        auth_token = os.environ.get('TURSO_AUTH_TOKEN')
        
        if not database_url or not auth_token:
            print(colored("❌ Missing Turso credentials in environment", "red"))
            return False
            
        db = TursoDatabase(database_url=database_url, auth_token=auth_token)
        print(colored("✅ Database connection established", "green"))
        
        # Get current table structure
        print(colored("\n📋 Current member_nominations table structure:", "blue"))
        result = db.execute_sql("PRAGMA table_info(member_nominations)")
        
        if db._is_valid_result(result):
            # Handle nested structure
            first_result = result['results'][0]
            if 'results' in first_result:
                columns_data = first_result['results']['rows']
            else:
                columns_data = first_result['rows']
            
            existing_columns = []
            for row in columns_data:
                column_name = row[1]  # column name is at index 1
                column_type = row[2]  # column type is at index 2
                existing_columns.append(column_name)
                print(colored(f"  - {column_name}: {column_type}", "cyan"))
        else:
            print(colored("❌ Could not get table structure", "red"))
            return False
        
        # Define required columns based on our form
        required_columns = {
            'nominee_address': 'TEXT',
            'nominee_url_link': 'TEXT'
        }
        
        # Check for missing columns and add them
        print(colored("\n🔧 Checking for missing columns...", "blue"))
        for column_name, column_type in required_columns.items():
            if column_name not in existing_columns:
                print(colored(f"⚠️ Missing column: {column_name}", "yellow"))
                try:
                    db.execute_sql(f"ALTER TABLE member_nominations ADD COLUMN {column_name} {column_type}")
                    print(colored(f"✅ Added {column_name} column", "green"))
                except Exception as e:
                    print(colored(f"❌ Error adding {column_name}: {e}", "red"))
            else:
                print(colored(f"✅ Column {column_name} exists", "green"))
        
        # Test member nomination submission
        print(colored("\n🧪 Testing member nomination submission...", "blue"))
        test_data = {
            'nominee_full_name': 'Test Nominee Fixed',
            'nominee_email': 'test-nominee-fixed@example.com',
            'nominee_place_of_work': 'Test University Fixed',
            'nominee_specialization': 'Computer Science Fixed',
            'nominee_country': 'Test Country Fixed',
            'nominee_phone': '+1234567890',
            'nominee_address': 'Test Address Fixed',
            'nominee_url_link': 'https://test-fixed.com',
            'nominee_qualifications': 'PhD in Computer Science Fixed',
            'nominating_member_name': 'Test Nominator Fixed',
            'nominator_email': 'test-nominator-fixed@example.com',
            'nomination_reason': 'Test nomination reason fixed',
            'additional_comments': 'Test nomination fixed'
        }
        
        try:
            # Import forms manager
            from forms_manager_turso import TursoFormsManager
            forms_manager = TursoFormsManager(db)
            
            result = forms_manager.submit_member_nomination(None, test_data)
            if result['success']:
                print(colored("✅ Member nomination test submission successful!", "green"))
            else:
                print(colored(f"❌ Member nomination test failed: {result.get('error')}", "red"))
        except Exception as e:
            print(colored(f"❌ Error testing member nomination: {e}", "red"))
        
        # Final count check
        print(colored("\n📊 Final member_nominations count:", "cyan"))
        try:
            result = db.execute_sql("SELECT COUNT(*) FROM member_nominations")
            if db._is_valid_result(result):
                # Handle nested structure
                first_result = result['results'][0]
                if 'results' in first_result:
                    count = first_result['results']['rows'][0][0]
                else:
                    count = first_result['rows'][0][0]
                print(colored(f"📋 member_nominations table: {count} records", "blue"))
            else:
                print(colored("⚠️ Could not get count for member_nominations", "yellow"))
        except Exception as e:
            print(colored(f"❌ Error counting records: {e}", "red"))
        
        print(colored("\n✅ Schema check completed!", "green"))
        return True
        
    except Exception as e:
        print(colored(f"❌ Schema check failed: {e}", "red"))
        return False

def main():
    """Main function"""
    print(colored("🔧 Starting member_nominations schema check...", "yellow"))
    
    success = check_and_fix_member_nominations()
    if success:
        print(colored("\n🎉 Schema check completed successfully!", "green"))
    else:
        print(colored("\n❌ Schema check failed!", "red"))

if __name__ == "__main__":
    main() 