#!/usr/bin/env python3
"""
Database migration script to add missing columns and fix schema issues
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

def migrate_database():
    """Migrate database to add missing columns"""
    print(colored("\n🔧 Starting database migration...", "cyan"))
    
    try:
        # Initialize database with credentials from environment
        database_url = os.environ.get('TURSO_DATABASE_URL')
        auth_token = os.environ.get('TURSO_AUTH_TOKEN')
        
        if not database_url or not auth_token:
            print(colored("❌ Missing Turso credentials in environment", "red"))
            return False
            
        print(colored(f"🔗 Using database URL: {database_url}", "cyan"))
        
        db = TursoDatabase(database_url=database_url, auth_token=auth_token)
        print(colored("✅ Database connection established", "green"))
        
        # Migration 1: Add missing columns to bank_of_ideas if they don't exist
        print(colored("\n🔄 Migration 1: Checking bank_of_ideas table...", "blue"))
        try:
            # Try to add created_at column (will fail if it already exists)
            db.execute_sql("ALTER TABLE bank_of_ideas ADD COLUMN created_at DATETIME DEFAULT CURRENT_TIMESTAMP")
            print(colored("✅ Added created_at column to bank_of_ideas", "green"))
        except Exception as e:
            if "duplicate column name" in str(e).lower() or "already exists" in str(e).lower():
                print(colored("ℹ️ created_at column already exists in bank_of_ideas", "blue"))
            else:
                print(colored(f"⚠️ Error adding created_at to bank_of_ideas: {e}", "yellow"))
        
        # Migration 2: Check member_nominations table structure
        print(colored("\n🔄 Migration 2: Checking member_nominations table...", "blue"))
        try:
            # Get table structure
            result = db.execute_sql("PRAGMA table_info(member_nominations)")
            print(colored(f"Current member_nominations structure: {result}", "cyan"))
            
            # Try to add missing columns
            missing_columns = [
                ("nominee_full_name", "TEXT NOT NULL DEFAULT ''"),
                ("nominee_place_of_work", "TEXT NOT NULL DEFAULT ''"),
                ("nominee_country", "TEXT NOT NULL DEFAULT ''"),
                ("nominee_phone", "TEXT NOT NULL DEFAULT ''"),
                ("nominee_specialization", "TEXT NOT NULL DEFAULT ''"),
                ("nominee_qualifications", "TEXT NOT NULL DEFAULT ''"),
                ("nominating_member_name", "TEXT NOT NULL DEFAULT ''"),
                ("created_at", "DATETIME DEFAULT CURRENT_TIMESTAMP")
            ]
            
            for column_name, column_def in missing_columns:
                try:
                    db.execute_sql(f"ALTER TABLE member_nominations ADD COLUMN {column_name} {column_def}")
                    print(colored(f"✅ Added {column_name} column to member_nominations", "green"))
                except Exception as e:
                    if "duplicate column name" in str(e).lower() or "already exists" in str(e).lower():
                        print(colored(f"ℹ️ {column_name} column already exists in member_nominations", "blue"))
                    else:
                        print(colored(f"⚠️ Error adding {column_name} to member_nominations: {e}", "yellow"))
        
        except Exception as e:
            print(colored(f"❌ Error checking member_nominations: {e}", "red"))
        
        # Migration 3: Check research_database table foreign key constraint
        print(colored("\n🔄 Migration 3: Checking research_database table...", "blue"))
        try:
            # Try to add created_at column
            db.execute_sql("ALTER TABLE research_database ADD COLUMN created_at DATETIME DEFAULT CURRENT_TIMESTAMP")
            print(colored("✅ Added created_at column to research_database", "green"))
        except Exception as e:
            if "duplicate column name" in str(e).lower() or "already exists" in str(e).lower():
                print(colored("ℹ️ created_at column already exists in research_database", "blue"))
            else:
                print(colored(f"⚠️ Error adding created_at to research_database: {e}", "yellow"))
        
        # Migration 4: Check general_suggestions table
        print(colored("\n🔄 Migration 4: Checking general_suggestions table...", "blue"))
        try:
            db.execute_sql("ALTER TABLE general_suggestions ADD COLUMN created_at DATETIME DEFAULT CURRENT_TIMESTAMP")
            print(colored("✅ Added created_at column to general_suggestions", "green"))
        except Exception as e:
            if "duplicate column name" in str(e).lower() or "already exists" in str(e).lower():
                print(colored("ℹ️ created_at column already exists in general_suggestions", "blue"))
            else:
                print(colored(f"⚠️ Error adding created_at to general_suggestions: {e}", "yellow"))
        
        # Final check: Display current record counts
        print(colored("\n📊 Final record counts after migration:", "cyan"))
        tables_to_check = [
            'membership_applications',
            'bank_of_ideas', 
            'member_nominations',
            'research_database',
            'general_suggestions'
        ]
        
        for table in tables_to_check:
            try:
                result = db.execute_sql(f"SELECT COUNT(*) FROM {table}")
                if db._is_valid_result(result):
                    # Handle nested structure
                    first_result = result['results'][0]
                    if 'results' in first_result:
                        count = first_result['results']['rows'][0][0]
                    else:
                        count = first_result['rows'][0][0]
                    print(colored(f"📋 Table '{table}': {count} records", "blue"))
                else:
                    print(colored(f"⚠️ Could not get count for table '{table}'", "yellow"))
            except Exception as e:
                print(colored(f"❌ Error counting records in '{table}': {e}", "red"))
        
        print(colored("\n✅ Database migration completed!", "green"))
        return True
        
    except Exception as e:
        print(colored(f"❌ Migration failed: {e}", "red"))
        return False

def main():
    """Main migration function"""
    print(colored("🗄️ Starting database migration process...", "yellow"))
    
    success = migrate_database()
    if success:
        print(colored("\n🎉 Migration completed successfully!", "green"))
    else:
        print(colored("\n❌ Migration failed!", "red"))

if __name__ == "__main__":
    main() 