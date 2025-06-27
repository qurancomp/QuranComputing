#!/usr/bin/env python3
"""
Test script to verify form submissions are working correctly
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
    from forms_manager_turso import TursoFormsManager
    print(colored("✅ Turso modules imported successfully", "green"))
except Exception as e:
    print(colored(f"❌ Error importing Turso modules: {e}", "red"))
    sys.exit(1)

def test_database_connection():
    """Test database connection and table existence"""
    print(colored("\n🔍 Testing database connection...", "cyan"))
    
    try:
        # Initialize database with credentials from environment
        database_url = os.environ.get('TURSO_DATABASE_URL')
        auth_token = os.environ.get('TURSO_AUTH_TOKEN')
        
        if not database_url or not auth_token:
            print(colored("❌ Missing Turso credentials in environment", "red"))
            return None
            
        print(colored(f"🔗 Using database URL: {database_url}", "cyan"))
        print(colored(f"🔑 Using auth token: {auth_token[:10]}...{auth_token[-10:]}", "cyan"))
        
        db = TursoDatabase(database_url=database_url, auth_token=auth_token)
        print(colored("✅ Database initialized successfully", "green"))
        
        # Test connection
        db.test_connection()
        print(colored("✅ Database connection test passed", "green"))
        
        # Check if tables exist
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
                    count = result['results'][0]['rows'][0][0]
                    print(colored(f"✅ Table '{table}' exists with {count} records", "green"))
                else:
                    print(colored(f"❌ Table '{table}' query failed", "red"))
            except Exception as e:
                print(colored(f"❌ Error checking table '{table}': {e}", "red"))
        
        return db
        
    except Exception as e:
        print(colored(f"❌ Database connection failed: {e}", "red"))
        return None

def test_form_submissions(db):
    """Test form submissions"""
    print(colored("\n📝 Testing form submissions...", "cyan"))
    
    try:
        forms_manager = TursoFormsManager(db)
        print(colored("✅ Forms manager initialized successfully", "green"))
        
        # Test Bank of Ideas submission
        print(colored("\n💡 Testing Bank of Ideas submission...", "blue"))
        bank_data = {
            'email': 'test@example.com',
            'submitter_name': 'Test User',
            'title_degrees': 'PhD Computer Science',
            'project_title': 'Test Project',
            'project_nature': 'Computing',
            'project_nature_other': '',
            'project_type': 'Applied Research',
            'project_type_other': '',
            'brief_description': 'This is a test project description',
            'specialization_area': 'AI and Machine Learning',
            'objectives': 'Test objectives',
            'benefits': 'Test benefits',
            'web_links': '',
            'additional_notes': 'Test submission'
        }
        
        result = forms_manager.submit_bank_of_ideas(1, bank_data)
        if result['success']:
            print(colored("✅ Bank of Ideas submission successful", "green"))
        else:
            print(colored(f"❌ Bank of Ideas submission failed: {result.get('error')}", "red"))
        
        # Test Research Database submission
        print(colored("\n🔬 Testing Research Database submission...", "blue"))
        research_data = {
            'research_type': 'Journal Article',
            'title': 'Test Research Paper',
            'journal_conference': 'Test Journal',
            'publisher': 'Test Publisher',
            'publication_year': 2024,
            'keywords': 'test, research, paper',
            'abstract': 'This is a test abstract',
            'doi_link': 'https://doi.org/test',
            'field_of_study': 'Computer Science',
            'language': 'English',
            'additional_notes': 'Test research submission'
        }
        
        result = forms_manager.submit_research_database(1, research_data)
        if result['success']:
            print(colored("✅ Research Database submission successful", "green"))
        else:
            print(colored(f"❌ Research Database submission failed: {result.get('error')}", "red"))
        
        # Test Member Nomination submission
        print(colored("\n👥 Testing Member Nomination submission...", "blue"))
        nomination_data = {
            'nominee_full_name': 'Test Nominee',
            'nominee_email': 'nominee@example.com',
            'nominee_place_of_work': 'Test University',
            'nominee_specialization': 'Computer Science',
            'nominee_country': 'Test Country',
            'nominee_phone': '+1234567890',
            'nominee_address': 'Test Address',
            'nominee_url_link': 'https://example.com',
            'nominee_qualifications': 'PhD in Computer Science',
            'nominating_member_name': 'Test Nominator',
            'nominator_email': 'nominator@example.com',
            'nomination_reason': 'Test nomination reason',
            'additional_comments': 'Test nomination'
        }
        
        result = forms_manager.submit_member_nomination(1, nomination_data)
        if result['success']:
            print(colored("✅ Member Nomination submission successful", "green"))
        else:
            print(colored(f"❌ Member Nomination submission failed: {result.get('error')}", "red"))
        
        # Check final record counts
        print(colored("\n📊 Final record counts:", "cyan"))
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
                    count = result['results'][0]['rows'][0][0]
                    print(colored(f"📋 Table '{table}': {count} records", "blue"))
            except Exception as e:
                print(colored(f"❌ Error counting records in '{table}': {e}", "red"))
        
    except Exception as e:
        print(colored(f"❌ Form submission test failed: {e}", "red"))

def main():
    """Main test function"""
    print(colored("🧪 Starting form submission tests...", "yellow"))
    
    # Test database connection
    db = test_database_connection()
    if not db:
        print(colored("❌ Database tests failed, exiting", "red"))
        return
    
    # Test form submissions
    test_form_submissions(db)
    
    print(colored("\n✅ All tests completed!", "green"))

if __name__ == "__main__":
    main() 