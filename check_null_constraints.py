#!/usr/bin/env python3
"""
Check NOT NULL constraints in member_nominations table
"""

import os
import sys
import toml

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

def check_null_constraints():
    """Check NOT NULL constraints in member_nominations table"""
    print(colored("\n🔍 Checking NOT NULL constraints...", "cyan"))
    
    try:
        # Initialize database with credentials from environment
        database_url = os.environ.get('TURSO_DATABASE_URL')
        auth_token = os.environ.get('TURSO_AUTH_TOKEN')
        
        if not database_url or not auth_token:
            print(colored("❌ Missing Turso credentials in environment", "red"))
            return False
            
        db = TursoDatabase(database_url=database_url, auth_token=auth_token)
        print(colored("✅ Database connection established", "green"))
        
        # Get current table structure with constraints
        print(colored("\n📋 Member_nominations table NOT NULL constraints:", "blue"))
        result = db.execute_sql("PRAGMA table_info(member_nominations)")
        
        if db._is_valid_result(result):
            # Handle nested structure
            first_result = result['results'][0]
            if 'results' in first_result:
                columns_data = first_result['results']['rows']
            else:
                columns_data = first_result['rows']
            
            not_null_columns = []
            for row in columns_data:
                column_name = row[1]  # column name is at index 1
                column_type = row[2]  # column type is at index 2
                not_null = row[3]     # notnull is at index 3
                
                if not_null == 1:  # NOT NULL constraint
                    not_null_columns.append(column_name)
                    print(colored(f"  ⚠️ NOT NULL: {column_name} ({column_type})", "yellow"))
                else:
                    print(colored(f"  ✅ NULLABLE: {column_name} ({column_type})", "green"))
            
            print(colored(f"\n🚨 Required fields (NOT NULL): {not_null_columns}", "red"))
            
        else:
            print(colored("❌ Could not get table structure", "red"))
            return False
        
        return True
        
    except Exception as e:
        print(colored(f"❌ Check failed: {e}", "red"))
        return False

def main():
    """Main function"""
    print(colored("🔧 Starting NOT NULL constraints check...", "yellow"))
    
    success = check_null_constraints()
    if success:
        print(colored("\n🎉 Check completed successfully!", "green"))
    else:
        print(colored("\n❌ Check failed!", "red"))

if __name__ == "__main__":
    main() 