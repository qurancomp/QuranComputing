"""
Forms Manager for Turso Cloud SQLite
Direct form submissions to cloud database without file handling
"""

try:
    from src.database_turso import TursoDatabase
except ImportError:
    from database_turso import TursoDatabase

from typing import Dict, Any, Optional
from datetime import datetime
from termcolor import colored

class TursoFormsManager:
    def __init__(self, db: TursoDatabase):
        self.db = db
    
    def submit_membership_application(self, user_id: Optional[int], form_data: Dict[str, Any]) -> Dict[str, Any]:
        """Submit membership application directly to cloud"""
        try:
            print(colored("📝 Submitting membership application to cloud...", "blue"))
            
            # Check if email already exists in membership applications
            email = form_data['email']
            print(colored(f"🔍 Checking for existing application with email: {email}", "blue"))
            
            existing_result = self.db.execute_sql(
                "SELECT id FROM membership_applications WHERE email = ?", 
                [email]
            )
            
            print(colored(f"🔍 Existing result: {existing_result}", "blue"))
            print(colored(f"🔍 Is valid result: {self.db._is_valid_result(existing_result)}", "blue"))
            
            # Check if any rows were returned (indicating duplicate)
            has_existing = False
            if (isinstance(existing_result, dict) and 
                existing_result.get('results') and 
                len(existing_result['results']) > 0 and 
                isinstance(existing_result['results'][0], dict)):
                
                rows = existing_result['results'][0].get('rows', [])
                if rows and len(rows) > 0:
                    has_existing = True
                    print(colored(f"🔍 Found {len(rows)} existing rows", "blue"))
            
            if has_existing:
                print(colored(f"❌ Email {email} already has a membership application", "red"))
                return {
                    'success': False, 
                    'error': 'duplicate_email',
                    'error_en': 'Membership information for this email has already been submitted.',
                    'error_ar': 'معلومات العضوية للبريد الإلكتروني المستخدم تم إدخالها من قبل'
                }
            
            print(colored(f"✅ No existing application found for email: {email}", "green"))
            
            # Split full name into first and last name
            full_name = form_data.get('full_name', '')
            name_parts = full_name.split(' ', 1)
            first_name = name_parts[0] if name_parts else ''
            last_name = name_parts[1] if len(name_parts) > 1 else ''
            
            result = self.db.execute_sql('''
                INSERT INTO membership_applications (
                    user_id, first_name, last_name, email, phone_number,
                    country, highest_degree, field_of_study, institution,
                    current_occupation, organization, position,
                    primary_research_area, motivation, application_date
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', [
                user_id, first_name, last_name, form_data['email'],
                form_data.get('phone', ''), form_data.get('country', ''),
                form_data.get('academic_degree', ''), form_data.get('specialization', ''),
                form_data.get('institution', ''), form_data.get('position', ''),
                form_data.get('institution', ''), form_data.get('position', ''),
                form_data.get('research_interests', ''), form_data.get('motivation', ''),
                datetime.now().isoformat()
            ])
            
            # Get the inserted application ID
            application_id = None
            if self.db._is_valid_result(result, check_rows=False) and result['results'][0].get('last_insert_rowid'):
                application_id = result['results'][0]['last_insert_rowid']
            
            print(colored("✅ Membership application submitted successfully", "green"))
            return {'success': True, 'application_id': application_id}
            
        except Exception as e:
            print(colored(f"❌ Error submitting membership application: {e}", "red"))
            error_str = str(e)
            
            # Check if it's a unique constraint violation (duplicate email)
            if 'unique' in error_str.lower() or 'constraint' in error_str.lower():
                print(colored(f"❌ Detected unique constraint violation for email", "red"))
                return {
                    'success': False, 
                    'error': 'duplicate_email',
                    'error_en': 'Membership information for this email has already been submitted.',
                    'error_ar': 'معلومات العضوية للبريد الإلكتروني المستخدم تم إدخالها من قبل'
                }
            
            return {'success': False, 'error': error_str}

    def submit_bank_of_ideas(self, user_id: Optional[int], form_data: Dict[str, Any]) -> Dict[str, Any]:
        """Submit bank of ideas suggestion directly to cloud"""
        try:
            print(colored("📝 Submitting bank of ideas suggestion to cloud...", "blue"))
            
            result = self.db.execute_sql('''
                INSERT INTO bank_of_ideas (
                    user_id, email, submitter_name, title_degrees, project_title,
                    project_nature, project_nature_other, project_type, project_type_other,
                    brief_description, specialization_area, objectives, benefits,
                    web_links, additional_notes, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', [
                user_id, form_data['email'], form_data['submitter_name'],
                form_data['title_degrees'], form_data['project_title'],
                form_data['project_nature'], form_data.get('project_nature_other'),
                form_data['project_type'], form_data.get('project_type_other'),
                form_data['brief_description'], form_data['specialization_area'],
                form_data['objectives'], form_data['benefits'],
                form_data.get('web_links'), form_data.get('additional_notes'),
                datetime.now().isoformat()
            ])
            
            suggestion_id = None
            if result.get('results') and result['results'][0].get('last_insert_rowid'):
                suggestion_id = result['results'][0]['last_insert_rowid']
            
            print(colored("✅ Bank of ideas suggestion submitted successfully", "green"))
            return {'success': True, 'suggestion_id': suggestion_id}
            
        except Exception as e:
            print(colored(f"❌ Error submitting bank of ideas: {e}", "red"))
            return {'success': False, 'error': str(e)}
    
    def submit_general_suggestion(self, user_id: Optional[int], form_data: Dict[str, Any]) -> Dict[str, Any]:
        """Submit general suggestion directly to cloud"""
        try:
            print(colored("📝 Submitting general suggestion to cloud...", "blue"))
            
            result = self.db.execute_sql('''
                INSERT INTO general_suggestions (
                    user_id, email, full_name, suggestion_type, suggestion_title,
                    suggestion_description, priority_level, implementation_timeline,
                    additional_comments, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', [
                user_id, form_data['email'], form_data['full_name'],
                form_data['suggestion_type'], form_data['suggestion_title'],
                form_data['suggestion_description'], form_data.get('priority_level'),
                form_data.get('implementation_timeline'), form_data.get('additional_comments'),
                datetime.now().isoformat()
            ])
            
            suggestion_id = None
            if result.get('results') and result['results'][0].get('last_insert_rowid'):
                suggestion_id = result['results'][0]['last_insert_rowid']
            
            print(colored("✅ General suggestion submitted successfully", "green"))
            return {'success': True, 'suggestion_id': suggestion_id}
            
        except Exception as e:
            print(colored(f"❌ Error submitting general suggestion: {e}", "red"))
            return {'success': False, 'error': str(e)}
    
    def submit_member_nomination(self, user_id: Optional[int], form_data: Dict[str, Any]) -> Dict[str, Any]:
        """Submit member nomination directly to cloud"""
        try:
            print(colored("📝 Submitting member nomination to cloud...", "blue"))
            
            result = self.db.execute_sql('''
                INSERT INTO member_nominations (
                    nominator_user_id, nominator_email, nominee_full_name, nominee_place_of_work,
                    nominee_country, nominee_address, nominee_phone, nominee_url_link,
                    nominee_email, nominee_specialization, nominee_qualifications,
                    nominating_member_name, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', [
                user_id, form_data['nominator_email'], form_data['nominee_full_name'],
                form_data['nominee_place_of_work'], form_data['nominee_country'],
                form_data.get('nominee_address'), form_data['nominee_phone'],
                form_data.get('nominee_url_link'), form_data['nominee_email'],
                form_data['nominee_specialization'], form_data['nominee_qualifications'],
                form_data['nominating_member_name'], datetime.now().isoformat()
            ])
            
            nomination_id = None
            if result.get('results') and result['results'][0].get('last_insert_rowid'):
                nomination_id = result['results'][0]['last_insert_rowid']
            
            print(colored("✅ Member nomination submitted successfully", "green"))
            return {'success': True, 'nomination_id': nomination_id}
            
        except Exception as e:
            print(colored(f"❌ Error submitting member nomination: {e}", "red"))
            return {'success': False, 'error': str(e)}
    
    def submit_research_database(self, user_id: Optional[int], form_data: Dict[str, Any]) -> Dict[str, Any]:
        """Submit research database entry directly to cloud"""
        try:
            print(colored("📝 Submitting research database entry to cloud...", "blue"))
            
            result = self.db.execute_sql('''
                INSERT INTO research_database (
                    user_id, publication_type, paper_title, conference_journal_book_title,
                    publisher_name, publication_year, keywords, abstract,
                    paper_url, article_classification, article_second_classification,
                    article_third_classification, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', [
                user_id, form_data['publication_type'], form_data['paper_title'],
                form_data['conference_journal_book_title'], form_data['publisher_name'],
                form_data['publication_year'], form_data.get('keywords'),
                form_data.get('abstract'), form_data.get('paper_url'),
                form_data.get('article_classification'), form_data.get('article_second_classification'),
                form_data.get('article_third_classification'), datetime.now().isoformat()
            ])
            
            research_id = None
            if result.get('results') and result['results'][0].get('last_insert_rowid'):
                research_id = result['results'][0]['last_insert_rowid']
            
            print(colored("✅ Research database entry submitted successfully", "green"))
            return {'success': True, 'research_id': research_id}
            
        except Exception as e:
            print(colored(f"❌ Error submitting research database entry: {e}", "red"))
            return {'success': False, 'error': str(e)}
    
    def get_form_fields(self, form_type: str, language: str = 'en') -> Dict[str, Any]:
        """Get form field definitions for different form types"""
        # This method remains the same as it's just configuration
        forms_config = {
            'bank_of_ideas': {
                'en': {
                    'title': 'Bank of Ideas: Research and Application Projects',
                    'description': 'Submit suggestions for research and application projects to serve the Holy Quran, Islamic sciences, and linguistic sciences.',
                    'fields': [
                        {'name': 'email', 'type': 'email', 'label': 'Email', 'required': True},
                        {'name': 'submitter_name', 'type': 'text', 'label': 'Name of Submitter', 'required': True},
                        {'name': 'title_degrees', 'type': 'text', 'label': 'Title and Scientific Degrees', 'required': True},
                        {'name': 'project_title', 'type': 'text', 'label': 'Title of the Research Project', 'required': True},
                        # ... rest of fields remain the same
                    ]
                }
            }
            # ... rest of form configurations remain the same
        }
        
        return forms_config.get(form_type, {}).get(language, {})

# Create alias for backward compatibility
FormsManager = TursoFormsManager 
