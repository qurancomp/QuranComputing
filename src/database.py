import sqlite3
import hashlib
import secrets
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, List
import bcrypt
import jwt

class Database:
    def __init__(self, db_path: str = "quran_institute.db"):
        self.db_path = db_path
        self.init_database()
    
    def get_connection(self):
        return sqlite3.connect(self.db_path)
    
    def init_database(self):
        """Initialize database with all required tables"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Users table for authentication
        cursor.execute('''
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
        cursor.execute('''
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
        cursor.execute('''
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
        
        # Bank of Ideas (Research Project Suggestions) table
        cursor.execute('''
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
        
        # Member Nominations table
        cursor.execute('''
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
        
        # Research Database table
        cursor.execute('''
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
        
        # General Suggestions table
        cursor.execute('''
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
        
        # Research Authors table (for multi-author papers in research database)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS research_authors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                research_id INTEGER NOT NULL,
                author_name TEXT NOT NULL,
                author_email TEXT,
                author_affiliation TEXT,
                author_order INTEGER DEFAULT 1,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (research_id) REFERENCES research_database (id)
            )
        ''')
        
        # Form submissions log table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS form_submissions_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                form_type TEXT NOT NULL,
                submission_id INTEGER NOT NULL,
                user_id INTEGER,
                ip_address TEXT,
                user_agent TEXT,
                submission_data TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    # User management methods
    def create_user(self, email: str, password: str, first_name: str, last_name: str) -> Dict[str, Any]:
        """Create a new user"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            # Check if user already exists
            cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
            if cursor.fetchone():
                return {'success': False, 'error': 'User already exists'}
            
            # Hash password
            password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            
            # Generate verification token
            verification_token = secrets.token_urlsafe(32)
            
            # Insert user
            cursor.execute('''
                INSERT INTO users (email, password_hash, first_name, last_name, verification_token)
                VALUES (?, ?, ?, ?, ?)
            ''', (email, password_hash, first_name, last_name, verification_token))
            
            user_id = cursor.lastrowid
            conn.commit()
            conn.close()
            
            return {'success': True, 'user_id': user_id, 'verification_token': verification_token}
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def authenticate_user(self, email: str, password: str) -> Dict[str, Any]:
        """Authenticate user login"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute("SELECT id, password_hash, first_name, last_name, is_verified FROM users WHERE email = ?", (email,))
            user = cursor.fetchone()
            
            if not user:
                return {'success': False, 'error': 'Invalid credentials'}
            
            user_id, password_hash, first_name, last_name, is_verified = user
            
            if not bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8')):
                return {'success': False, 'error': 'Invalid credentials'}
            
            # Generate session token
            token = secrets.token_urlsafe(32)
            expires_at = datetime.now() + timedelta(days=30)
            
            cursor.execute('''
                INSERT INTO session_tokens (user_id, token, expires_at)
                VALUES (?, ?, ?)
            ''', (user_id, token, expires_at))
            
            conn.commit()
            conn.close()
            
            return {
                'success': True,
                'user_id': user_id,
                'token': token,
                'first_name': first_name,
                'last_name': last_name,
                'is_verified': is_verified
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_user_by_token(self, token: str) -> Optional[Dict[str, Any]]:
        """Get user by session token"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT u.id, u.email, u.first_name, u.last_name, u.is_verified
                FROM users u
                JOIN session_tokens st ON u.id = st.user_id
                WHERE st.token = ? AND st.expires_at > ?
            ''', (token, datetime.now()))
            
            user = cursor.fetchone()
            conn.close()
            
            if user:
                return {
                    'id': user[0],
                    'email': user[1],
                    'first_name': user[2],
                    'last_name': user[3],
                    'is_verified': user[4]
                }
            return None
            
        except Exception as e:
            return None

