#!/usr/bin/env python3
"""
Script to clean up duplicate email entries in membership_applications table
Keeps only the first (oldest) entry for each email address
"""

import os
import sys
from typing import Dict, Any

# Add the src directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

try:
    from termcolor import colored
except ImportError:
    def colored(text, color=None):
        return text

from database_turso import TursoDatabase

# CONSTANTS - Update these with your Turso credentials
TURSO_DATABASE_URL = os.getenv("TURSO_DATABASE_URL")
TURSO_AUTH_TOKEN = os.getenv("TURSO_AUTH_TOKEN")

def clean_duplicate_emails():
    """Remove duplicate email entries from membership_applications table"""
    print(colored("🧹 Starting duplicate email cleanup...", "blue"))
    
    if not TURSO_DATABASE_URL or not TURSO_AUTH_TOKEN:
        print(colored("❌ Missing Turso credentials. Please set TURSO_DATABASE_URL and TURSO_AUTH_TOKEN environment variables.", "red"))
        return False
    
    try:
        # Initialize database connection
        db = TursoDatabase(TURSO_DATABASE_URL, TURSO_AUTH_TOKEN)
        print(colored("✅ Connected to Turso database", "green"))
        
        # First, let's see what duplicates we have
        print(colored("🔍 Finding duplicate emails...", "blue"))
        duplicate_result = db.execute_sql("""
            SELECT email, COUNT(*) as count, GROUP_CONCAT(id) as ids
            FROM membership_applications 
            GROUP BY LOWER(email) 
            HAVING COUNT(*) > 1
            ORDER BY count DESC
        """)
        
        if (isinstance(duplicate_result, dict) and 
            duplicate_result.get('results') and 
            len(duplicate_result['results']) > 0 and 
            duplicate_result['results'][0].get('rows')):
            
            duplicate_rows = duplicate_result['results'][0]['rows']
            print(colored(f"📊 Found {len(duplicate_rows)} email addresses with duplicates:", "yellow"))
            
            for row in duplicate_rows:
                email, count, ids = row
                print(colored(f"  - {email}: {count} entries (IDs: {ids})", "yellow"))
            
            # For each duplicate email, keep only the first (lowest ID) entry
            for row in duplicate_rows:
                email, count, ids_str = row
                id_list = [int(id.strip()) for id in ids_str.split(',')]
                keep_id = min(id_list)  # Keep the oldest entry (lowest ID)
                delete_ids = [id for id in id_list if id != keep_id]
                
                print(colored(f"📧 Processing {email}:", "blue"))
                print(colored(f"  - Keeping ID {keep_id}", "green"))
                print(colored(f"  - Deleting IDs {delete_ids}", "red"))
                
                # Delete the duplicate entries
                for delete_id in delete_ids:
                    delete_result = db.execute_sql(
                        "DELETE FROM membership_applications WHERE id = ?",
                        [delete_id]
                    )
                    print(colored(f"  ✅ Deleted entry ID {delete_id}", "green"))
            
            print(colored(f"🎉 Cleanup completed! Removed {sum(len([int(id.strip()) for id in row[2].split(',')]) - 1 for row in duplicate_rows)} duplicate entries", "green"))
            
        else:
            print(colored("✅ No duplicate emails found!", "green"))
            
        return True
        
    except Exception as e:
        print(colored(f"❌ Error during cleanup: {e}", "red"))
        return False

def verify_cleanup():
    """Verify that duplicates have been removed"""
    print(colored("\n🔍 Verifying cleanup results...", "blue"))
    
    try:
        db = TursoDatabase(TURSO_DATABASE_URL, TURSO_AUTH_TOKEN)
        
        # Check for remaining duplicates
        duplicate_check = db.execute_sql("""
            SELECT email, COUNT(*) as count
            FROM membership_applications 
            GROUP BY LOWER(email) 
            HAVING COUNT(*) > 1
        """)
        
        if (isinstance(duplicate_check, dict) and 
            duplicate_check.get('results') and 
            len(duplicate_check['results']) > 0 and 
            duplicate_check['results'][0].get('rows')):
            
            remaining_duplicates = duplicate_check['results'][0]['rows']
            if remaining_duplicates:
                print(colored(f"⚠️ Warning: {len(remaining_duplicates)} email addresses still have duplicates", "yellow"))
                for email, count in remaining_duplicates:
                    print(colored(f"  - {email}: {count} entries", "yellow"))
            else:
                print(colored("✅ No duplicate emails remaining!", "green"))
        else:
            print(colored("✅ No duplicate emails remaining!", "green"))
            
        # Show total entries
        total_result = db.execute_sql("SELECT COUNT(*) as total FROM membership_applications")
        if (isinstance(total_result, dict) and 
            total_result.get('results') and 
            len(total_result['results']) > 0):
            total_count = total_result['results'][0]['rows'][0][0]
            print(colored(f"📊 Total membership applications: {total_count}", "blue"))
            
    except Exception as e:
        print(colored(f"❌ Error during verification: {e}", "red"))

if __name__ == "__main__":
    print(colored("🚀 Duplicate Email Cleanup Tool", "cyan"))
    print(colored("=" * 50, "cyan"))
    
    if clean_duplicate_emails():
        verify_cleanup()
    else:
        print(colored("❌ Cleanup failed", "red"))
        sys.exit(1)
    
    print(colored("\n✅ Process completed!", "green")) 