"""
Turso Database Implementation for Cloud SQLite
Direct connections to cloud SQLite without file downloads/uploads
"""

import streamlit as st
import requests
import json
from typing import Optional, Dict, Any, List
from datetime import datetime, timedelta
import hashlib
import secrets
import bcrypt
import jwt
from termcolor import colored

class TursoDatabase:
    def __init__(self, database_url: str = None, auth_token: str = None):
        """Initialize Turso database connection"""
        # Get connection details from Streamlit secrets or parameters
        if hasattr(st, 'secrets') and 'turso' in st.secrets:
            self.database_url = st.secrets["turso"]["database_url"]
            self.auth_token = st.secrets["turso"]["auth_token"]
            print(colored("🔐 Using Turso credentials from Streamlit secrets", "green"))
            print(colored(f"🗄️ Database URL: {self.database_url}", "cyan"))
            print(colored(f"🔑 Auth token length: {len(self.auth_token) if self.auth_token else 0}", "cyan"))
        else:
            self.database_url = database_url
            self.auth_token = auth_token
            print(colored("⚠️ No Turso credentials in secrets, using parameters", "yellow"))
        
        if not self.database_url or not self.auth_token:
            error_msg = "❌ Missing Turso credentials! Please check your secrets configuration."
            print(colored(error_msg, "red"))
            raise ValueError(error_msg)
        
        self.headers = {
            "Authorization": f"Bearer {self.auth_token}",
            "Content-Type": "application/json"
        }
        
        print(colored(f"🗄️ Final Database URL: {self.database_url}", "cyan"))
        print(colored("🚀 Initializing database connection...", "blue"))
        self.init_database()
    
    def execute_sql(self, sql: str, params: List = None) -> Dict[str, Any]:
        """Execute SQL query directly on cloud SQLite"""
        try:
            payload = {
                "statements": [
                    {
                        "q": sql,
                        "params": params or []
                    }
                ]
            }
            
            print(colored(f"🔧 Executing SQL: {sql[:50]}...", "blue"))
            
            # Construct the proper API endpoint
            api_url = f"{self.database_url}/v2/pipeline"
            print(colored(f"🌐 API URL: {api_url}", "cyan"))
            
            response = requests.post(
                api_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            print(colored(f"📡 Response status: {response.status_code}", "blue"))
            
            if response.status_code != 200:
                print(colored(f"❌ HTTP Error: {response.status_code}", "red"))
                print(colored(f"Response headers: {dict(response.headers)}", "red"))
                print(colored(f"Response text: {response.text}", "red"))
            
            response.raise_for_status()
            
            result = response.json()
            print(colored("✅ SQL executed successfully", "green"))
            return result
            
        except Exception as e:
            print(colored(f"❌ SQL execution error: {e}", "red"))
            print(colored(f"Error type: {type(e).__name__}", "red"))
            if hasattr(e, 'response'):
                print(colored(f"Response status: {e.response.status_code}", "red"))
                print(colored(f"Response text: {e.response.text}", "red"))
            raise e
    
    def init_database(self):
        """Initialize database with all required tables"""
        print(colored("🔧 Initializing database tables...", "blue"))
        
        try:
            # Users table
            self.execute_sql('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    is_verified BOOLEAN DEFAULT FALSE,
                    verification_token TEXT,
                    reset_token TEXT,
                    reset_token_expires DATETIME,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Session tokens table
            self.execute_sql('''
                CREATE TABLE IF NOT EXISTS session_tokens (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    token TEXT UNIQUE NOT NULL,
                    expires_at DATETIME NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')
            
            # Membership applications table
            self.execute_sql('''
                CREATE TABLE IF NOT EXISTS membership_applications (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    first_name TEXT NOT NULL,
                    middle_name TEXT,
                    last_name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phone_number TEXT NOT NULL,
                    date_of_birth DATE,
                    gender TEXT,
                    nationality TEXT,
                    address TEXT,
                    city TEXT,
                    state_province TEXT,
                    country TEXT,
                    postal_code TEXT,
                    highest_degree TEXT NOT NULL,
                    field_of_study TEXT,
                    institution TEXT,
                    graduation_year INTEGER,
                    current_occupation TEXT,
                    organization TEXT,
                    position TEXT,
                    years_of_experience INTEGER DEFAULT 0,
                    primary_research_area TEXT,
                    secondary_research_area TEXT,
                    previous_publications TEXT,
                    current_research_projects TEXT,
                    programming_languages TEXT,
                    technical_skills TEXT,
                    software_proficiency TEXT,
                    membership_type TEXT DEFAULT 'individual',
                    how_did_you_hear TEXT,
                    motivation TEXT,
                    expected_contributions TEXT,
                    status TEXT DEFAULT 'Pending',
                    application_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                    reviewed_at DATETIME,
                    reviewed_by INTEGER,
                    FOREIGN KEY (user_id) REFERENCES users (id),
                    FOREIGN KEY (reviewed_by) REFERENCES users (id)
                )
            ''')
            
            # Bank of Ideas table
            self.execute_sql('''
                CREATE TABLE IF NOT EXISTS bank_of_ideas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    email TEXT NOT NULL,
                    submitter_name TEXT NOT NULL,
                    title_degrees TEXT NOT NULL,
                    project_title TEXT NOT NULL,
                    project_nature TEXT NOT NULL,
                    project_nature_other TEXT,
                    project_type TEXT NOT NULL,
                    project_type_other TEXT,
                    brief_description TEXT NOT NULL,
                    specialization_area TEXT NOT NULL,
                    objectives TEXT NOT NULL,
                    benefits TEXT NOT NULL,
                    web_links TEXT,
                    additional_notes TEXT,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')
            
            # Member nominations table
            self.execute_sql('''
                CREATE TABLE IF NOT EXISTS member_nominations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nominator_user_id INTEGER,
                    nominator_email TEXT NOT NULL,
                    nominee_full_name TEXT NOT NULL,
                    nominee_place_of_work TEXT NOT NULL,
                    nominee_country TEXT NOT NULL,
                    nominee_address TEXT,
                    nominee_phone TEXT NOT NULL,
                    nominee_url_link TEXT,
                    nominee_email TEXT NOT NULL,
                    nominee_specialization TEXT NOT NULL,
                    nominee_qualifications TEXT NOT NULL,
                    nominating_member_name TEXT NOT NULL,
                    status TEXT DEFAULT 'Pending',
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    reviewed_at DATETIME,
                    reviewed_by INTEGER,
                    FOREIGN KEY (nominator_user_id) REFERENCES users (id),
                    FOREIGN KEY (reviewed_by) REFERENCES users (id)
                )
            ''')
            
            # Research database table
            self.execute_sql('''
                CREATE TABLE IF NOT EXISTS research_database (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    publication_type TEXT NOT NULL,
                    paper_title TEXT NOT NULL,
                    conference_journal_book_title TEXT NOT NULL,
                    publisher_name TEXT NOT NULL,
                    publication_year TEXT NOT NULL,
                    keywords TEXT,
                    abstract TEXT,
                    paper_url TEXT,
                    article_classification TEXT,
                    article_second_classification TEXT,
                    article_third_classification TEXT,
                    status TEXT DEFAULT 'Pending',
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    reviewed_at DATETIME,
                    reviewed_by INTEGER,
                    FOREIGN KEY (user_id) REFERENCES users (id),
                    FOREIGN KEY (reviewed_by) REFERENCES users (id)
                )
            ''')
            
            # General suggestions table
            self.execute_sql('''
                CREATE TABLE IF NOT EXISTS general_suggestions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    email TEXT NOT NULL,
                    full_name TEXT NOT NULL,
                    suggestion_type TEXT NOT NULL,
                    suggestion_title TEXT NOT NULL,
                    suggestion_description TEXT NOT NULL,
                    priority_level TEXT,
                    implementation_timeline TEXT,
                    additional_comments TEXT,
                    status TEXT DEFAULT 'Pending',
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    reviewed_at DATETIME,
                    reviewed_by INTEGER,
                    FOREIGN KEY (user_id) REFERENCES users (id),
                    FOREIGN KEY (reviewed_by) REFERENCES users (id)
                )
            ''')
            
            print(colored("✅ Database tables initialized successfully", "green"))
            
        except Exception as e:
            print(colored(f"❌ Error initializing database: {e}", "red"))
            raise e
    
    # User management methods
    def create_user(self, email: str, password: str, first_name: str, last_name: str) -> Dict[str, Any]:
        """Create a new user"""
        try:
            # Check if user already exists
            result = self.execute_sql("SELECT id FROM users WHERE email = ?", [email])
            if result.get('results') and result['results'][0].get('rows'):
                return {'success': False, 'error': 'User already exists'}
            
            # Hash password
            password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            verification_token = secrets.token_urlsafe(32)
            
            # Insert user
            result = self.execute_sql('''
                INSERT INTO users (email, password_hash, first_name, last_name, verification_token)
                VALUES (?, ?, ?, ?, ?)
            ''', [email, password_hash, first_name, last_name, verification_token])
            
            # Get the inserted user ID from the result
            user_id = None
            if result.get('results') and result['results'][0].get('last_insert_rowid'):
                user_id = result['results'][0]['last_insert_rowid']
            
            print(colored("✅ User created successfully", "green"))
            return {'success': True, 'user_id': user_id, 'verification_token': verification_token}
            
        except Exception as e:
            print(colored(f"❌ Error creating user: {e}", "red"))
            return {'success': False, 'error': str(e)}
    
    def authenticate_user(self, email: str, password: str) -> Dict[str, Any]:
        """Authenticate user login"""
        try:
            # Get user data
            result = self.execute_sql(
                "SELECT id, password_hash, first_name, last_name, is_verified FROM users WHERE email = ?", 
                [email]
            )
            
            if not result.get('results') or not result['results'][0].get('rows'):
                return {'success': False, 'error': 'Invalid credentials'}
            
            user_data = result['results'][0]['rows'][0]
            user_id, password_hash, first_name, last_name, is_verified = user_data
            
            if not bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8')):
                return {'success': False, 'error': 'Invalid credentials'}
            
            # Generate session token
            token = secrets.token_urlsafe(32)
            expires_at = (datetime.now() + timedelta(days=30)).isoformat()
            
            self.execute_sql('''
                INSERT INTO session_tokens (user_id, token, expires_at)
                VALUES (?, ?, ?)
            ''', [user_id, token, expires_at])
            
            print(colored("✅ User authenticated successfully", "green"))
            return {
                'success': True,
                'user_id': user_id,
                'token': token,
                'first_name': first_name,
                'last_name': last_name,
                'is_verified': is_verified
            }
            
        except Exception as e:
            print(colored(f"❌ Error authenticating user: {e}", "red"))
            return {'success': False, 'error': str(e)}
    
    def get_user_by_token(self, token: str) -> Optional[Dict[str, Any]]:
        """Get user by session token"""
        try:
            result = self.execute_sql('''
                SELECT u.id, u.email, u.first_name, u.last_name, u.is_verified
                FROM users u
                JOIN session_tokens st ON u.id = st.user_id
                WHERE st.token = ? AND st.expires_at > ?
            ''', [token, datetime.now().isoformat()])
            
            if result.get('results') and result['results'][0].get('rows'):
                user_data = result['results'][0]['rows'][0]
                return {
                    'id': user_data[0],
                    'email': user_data[1],
                    'first_name': user_data[2],
                    'last_name': user_data[3],
                    'is_verified': user_data[4]
                }
            return None
            
        except Exception as e:
            print(colored(f"❌ Error getting user by token: {e}", "red"))
            return None

# Create alias for backward compatibility
Database = TursoDatabase 
