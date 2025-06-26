try:
    from src.database import Database
except ImportError:
    from database import Database
from typing import Dict, Any, Optional
from datetime import datetime
from termcolor import colored

class FormsManager:
    def __init__(self, db: Database):
        self.db = db
    
    def submit_membership_application(self, user_id: Optional[int], form_data: Dict[str, Any]) -> Dict[str, Any]:
        """Submit membership application"""
        conn = None
        try:
            print(colored("📝 Submitting membership application...", "blue"))
            conn = self.db.get_connection()
            cursor = conn.cursor()
            
            # Split full name into first and last name
            full_name = form_data.get('full_name', '')
            name_parts = full_name.split(' ', 1)
            first_name = name_parts[0] if name_parts else ''
            last_name = name_parts[1] if len(name_parts) > 1 else ''
            
            cursor.execute('''
                INSERT INTO membership_applications (
                    user_id, first_name, last_name, email, phone_number,
                    country, highest_degree, field_of_study, institution,
                    current_occupation, organization, position,
                    primary_research_area, motivation, application_date
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                user_id, first_name, last_name, form_data['email'],
                form_data.get('phone', ''), form_data.get('country', ''),
                form_data.get('academic_degree', ''), form_data.get('specialization', ''),
                form_data.get('institution', ''), form_data.get('position', ''),
                form_data.get('institution', ''), form_data.get('position', ''),
                form_data.get('research_interests', ''), form_data.get('motivation', ''),
                datetime.now()
            ))
            
            application_id = cursor.lastrowid
            self.db.commit_and_upload(conn)
            print(colored("✅ Membership application submitted successfully", "green"))
            
            return {'success': True, 'application_id': application_id}
            
        except Exception as e:
            print(colored(f"❌ Error submitting membership application: {e}", "red"))
            return {'success': False, 'error': str(e)}
        finally:
            if conn:
                self.db.close_connection(conn)

    def submit_bank_of_ideas(self, user_id: Optional[int], form_data: Dict[str, Any]) -> Dict[str, Any]:
        """Submit bank of ideas suggestion (Research Project Ideas)"""
        conn = None
        try:
            print(colored("📝 Submitting bank of ideas suggestion...", "blue"))
            conn = self.db.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO bank_of_ideas (
                    user_id, email, submitter_name, title_degrees, project_title,
                    project_nature, project_nature_other, project_type, project_type_other,
                    brief_description, specialization_area, objectives, benefits,
                    web_links, additional_notes, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                user_id, form_data['email'], form_data['submitter_name'],
                form_data['title_degrees'], form_data['project_title'],
                form_data['project_nature'], form_data.get('project_nature_other'),
                form_data['project_type'], form_data.get('project_type_other'),
                form_data['brief_description'], form_data['specialization_area'],
                form_data['objectives'], form_data['benefits'],
                form_data.get('web_links'), form_data.get('additional_notes'),
                datetime.now()
            ))
            
            suggestion_id = cursor.lastrowid
            self.db.commit_and_upload(conn)
            print(colored("✅ Bank of ideas suggestion submitted successfully", "green"))
            
            return {'success': True, 'suggestion_id': suggestion_id}
            
        except Exception as e:
            print(colored(f"❌ Error submitting bank of ideas: {e}", "red"))
            return {'success': False, 'error': str(e)}
        finally:
            if conn:
                self.db.close_connection(conn)
    
    def submit_general_suggestion(self, user_id: Optional[int], form_data: Dict[str, Any]) -> Dict[str, Any]:
        """Submit general suggestion"""
        conn = None
        try:
            print(colored("📝 Submitting general suggestion...", "blue"))
            conn = self.db.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO general_suggestions (
                    user_id, email, full_name, suggestion_type, suggestion_title,
                    suggestion_description, priority_level, implementation_timeline,
                    additional_comments, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                user_id, form_data['email'], form_data['full_name'],
                form_data['suggestion_type'], form_data['suggestion_title'],
                form_data['suggestion_description'], form_data.get('priority_level'),
                form_data.get('implementation_timeline'), form_data.get('additional_comments'),
                datetime.now()
            ))
            
            suggestion_id = cursor.lastrowid
            self.db.commit_and_upload(conn)
            print(colored("✅ General suggestion submitted successfully", "green"))
            
            return {'success': True, 'suggestion_id': suggestion_id}
            
        except Exception as e:
            print(colored(f"❌ Error submitting general suggestion: {e}", "red"))
            return {'success': False, 'error': str(e)}
        finally:
            if conn:
                self.db.close_connection(conn)
    
    def submit_member_nomination(self, user_id: Optional[int], form_data: Dict[str, Any]) -> Dict[str, Any]:
        """Submit member nomination"""
        conn = None
        try:
            print(colored("📝 Submitting member nomination...", "blue"))
            conn = self.db.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO member_nominations (
                    nominator_user_id, nominator_email, nominee_full_name, nominee_place_of_work,
                    nominee_country, nominee_address, nominee_phone, nominee_url_link,
                    nominee_email, nominee_specialization, nominee_qualifications,
                    nominating_member_name, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                user_id, form_data['nominator_email'], form_data['nominee_full_name'],
                form_data['nominee_place_of_work'], form_data['nominee_country'],
                form_data.get('nominee_address'), form_data['nominee_phone'],
                form_data.get('nominee_url_link'), form_data['nominee_email'],
                form_data['nominee_specialization'], form_data['nominee_qualifications'],
                form_data['nominating_member_name'], datetime.now()
            ))
            
            nomination_id = cursor.lastrowid
            self.db.commit_and_upload(conn)
            print(colored("✅ Member nomination submitted successfully", "green"))
            
            return {'success': True, 'nomination_id': nomination_id}
            
        except Exception as e:
            print(colored(f"❌ Error submitting member nomination: {e}", "red"))
            return {'success': False, 'error': str(e)}
        finally:
            if conn:
                self.db.close_connection(conn)
    
    def submit_research_database(self, user_id: Optional[int], form_data: Dict[str, Any]) -> Dict[str, Any]:
        """Submit research database entry"""
        conn = None
        try:
            print(colored("📝 Submitting research database entry...", "blue"))
            conn = self.db.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO research_database (
                    user_id, publication_type, paper_title, conference_journal_book_title,
                    publisher_name, publication_year, keywords, abstract,
                    paper_url, article_classification, article_second_classification,
                    article_third_classification, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                user_id, form_data['publication_type'], form_data['paper_title'],
                form_data['conference_journal_book_title'], form_data['publisher_name'],
                form_data['publication_year'], form_data.get('keywords'),
                form_data.get('abstract'), form_data.get('paper_url'),
                form_data.get('article_classification'), form_data.get('article_second_classification'),
                form_data.get('article_third_classification'), datetime.now()
            ))
            
            research_id = cursor.lastrowid
            self.db.commit_and_upload(conn)
            print(colored("✅ Research database entry submitted successfully", "green"))
            
            return {'success': True, 'research_id': research_id}
            
        except Exception as e:
            print(colored(f"❌ Error submitting research database entry: {e}", "red"))
            return {'success': False, 'error': str(e)}
        finally:
            if conn:
                self.db.close_connection(conn)
    
    def get_form_fields(self, form_type: str, language: str = 'en') -> Dict[str, Any]:
        """Get form field definitions for different form types"""
        
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
                        {'name': 'project_nature', 'type': 'select', 'label': 'Nature of the project', 'required': True,
                         'options': ['Computing', 'Religious', 'Linguistic', 'Other - Specify']},
                        {'name': 'project_nature_other', 'type': 'text', 'label': 'Other Nature (if selected)', 'required': False},
                        {'name': 'project_type', 'type': 'select', 'label': 'Type of the Project', 'required': True,
                         'options': ['Theoretical Research', 'Applied Research', 'Field Study', 'Other - Specify']},
                        {'name': 'project_type_other', 'type': 'text', 'label': 'Other Type (if selected)', 'required': False},
                        {'name': 'brief_description', 'type': 'textarea', 'label': 'Brief Description of Proposed Project', 'required': True},
                        {'name': 'specialization_area', 'type': 'text', 'label': 'Specialization area of the Research/Project', 'required': True},
                        {'name': 'objectives', 'type': 'textarea', 'label': 'Objectives/Goals of the Research/Project', 'required': True},
                        {'name': 'benefits', 'type': 'textarea', 'label': 'Benefits of the Research/Project', 'required': True},
                        {'name': 'web_links', 'type': 'textarea', 'label': 'Web links URLs', 'required': False},
                        {'name': 'additional_notes', 'type': 'textarea', 'label': 'Additional Notes', 'required': False}
                    ]
                },
                'ar': {
                    'title': 'مشروع بنك الأفكار: مقترحات لمشاريع بحثية وتطبيقية',
                    'description': 'تقديم مقترحات لمشاريع بحثية وتطبيقية لخدمة القرآن الكريم والعلوم الإسلامية واللغوية.',
                    'fields': [
                        {'name': 'email', 'type': 'email', 'label': 'البريد الإلكتروني', 'required': True},
                        {'name': 'submitter_name', 'type': 'text', 'label': 'اسم مقدم المقترح', 'required': True},
                        {'name': 'title_degrees', 'type': 'text', 'label': 'اللقب العلمي والتخصص', 'required': True},
                        {'name': 'project_title', 'type': 'text', 'label': 'عنوان المقترح أو المشروع', 'required': True},
                        {'name': 'project_nature', 'type': 'select', 'label': 'طبيعة البحث أو المشروع', 'required': True,
                         'options': ['حاسوبي', 'شرعي', 'لغوي', 'أخرى - اذكرها']},
                        {'name': 'project_nature_other', 'type': 'text', 'label': 'طبيعة أخرى (إذا تم اختيارها)', 'required': False},
                        {'name': 'project_type', 'type': 'select', 'label': 'نوع البحث أو المشروع', 'required': True,
                         'options': ['بحث نظري', 'بحث عملي تطبيقي', 'دراسة ميدانية', 'أخرى - اذكرها']},
                        {'name': 'project_type_other', 'type': 'text', 'label': 'نوع آخر (إذا تم اختياره)', 'required': False},
                        {'name': 'brief_description', 'type': 'textarea', 'label': 'نبذة قصيرة عن البحث', 'required': True},
                        {'name': 'specialization_area', 'type': 'text', 'label': 'مجال / تخصص البحث / المشروع المقترح', 'required': True},
                        {'name': 'objectives', 'type': 'textarea', 'label': 'أهداف البحث / المشروع', 'required': True},
                        {'name': 'benefits', 'type': 'textarea', 'label': 'ماهي فوائد البحث / المشروع', 'required': True},
                        {'name': 'web_links', 'type': 'textarea', 'label': 'روابط لموقع النت', 'required': False},
                        {'name': 'additional_notes', 'type': 'textarea', 'label': 'ملاحظات أخرى', 'required': False}
                    ]
                }
            },
            'member_nomination': {
                'en': {
                    'title': 'Member Nomination Form',
                    'description': 'Nomination form for Membership in International Computing Institute for Quran and Islamic Sciences.',
                    'fields': [
                        {'name': 'nominator_email', 'type': 'email', 'label': 'Email', 'required': True},
                        {'name': 'nominee_full_name', 'type': 'text', 'label': 'Nominee Full Name', 'required': True},
                        {'name': 'nominee_place_of_work', 'type': 'text', 'label': 'Nominee Place of Work', 'required': True},
                        {'name': 'nominee_country', 'type': 'text', 'label': 'Nominee Country of Residence', 'required': True},
                        {'name': 'nominee_address', 'type': 'text', 'label': 'Nominee Address', 'required': False},
                        {'name': 'nominee_phone', 'type': 'text', 'label': 'Nominee Phone Number including country code', 'required': True},
                        {'name': 'nominee_url_link', 'type': 'text', 'label': 'Nominee URL Link', 'required': False},
                        {'name': 'nominee_email', 'type': 'email', 'label': 'Nominee Email', 'required': True},
                        {'name': 'nominee_specialization', 'type': 'select', 'label': 'Religious / Computing / Linguist', 'required': True,
                         'options': ['Religious', 'Computing', 'Linguist']},
                        {'name': 'nominee_qualifications', 'type': 'textarea', 'label': 'Qualifications and scientific effort related to Quran Computing and Islamic Sciences and Arabic Language', 'required': True},
                        {'name': 'nominating_member_name', 'type': 'text', 'label': 'Name of Member who is nominating', 'required': True}
                    ]
                },
                'ar': {
                    'title': 'نموذج الترشيح للعضوية',
                    'description': 'نموذج الترشيح لعضوية المعهد العالمي لحوسبة القرآن والعلوم الإسلامية.',
                    'fields': [
                        {'name': 'nominator_email', 'type': 'email', 'label': 'البريد الإلكتروني', 'required': True},
                        {'name': 'nominee_full_name', 'type': 'text', 'label': 'إسم المترشّح كاملا', 'required': True},
                        {'name': 'nominee_place_of_work', 'type': 'text', 'label': 'جهة العمل للمترشح', 'required': True},
                        {'name': 'nominee_country', 'type': 'text', 'label': 'البلد للمترشح', 'required': True},
                        {'name': 'nominee_address', 'type': 'text', 'label': 'العنوان للمترشح', 'required': False},
                        {'name': 'nominee_phone', 'type': 'text', 'label': 'التلفون للمترشح مع الرقم الدولي', 'required': True},
                        {'name': 'nominee_url_link', 'type': 'text', 'label': 'الرابط للنت للمترشح', 'required': False},
                        {'name': 'nominee_email', 'type': 'email', 'label': 'البريد الإلكتروني للمترشح', 'required': True},
                        {'name': 'nominee_specialization', 'type': 'select', 'label': 'شرعي/ حاسوبي / لغوي', 'required': True,
                         'options': ['شرعي', 'حاسوبي', 'لغوي']},
                        {'name': 'nominee_qualifications', 'type': 'textarea', 'label': 'المؤهلات والجهود العلمية ذات العلاقة بحوسبة القرآن والعلوم الاسلامية واللغة العربية', 'required': True},
                        {'name': 'nominating_member_name', 'type': 'text', 'label': 'العضو الذي رشحه', 'required': True}
                    ]
                }
            },
            'research_database': {
                'en': {
                    'title': 'Researches and Researchers Database',
                    'description': 'Submit research papers and publications for the database of Quran computing and Islamic sciences research.',
                    'fields': [
                        {'name': 'publication_type', 'type': 'select', 'label': 'Publication Type', 'required': True,
                         'options': ["Journal's Article", 'Book', 'Book Chapter', 'Conference Paper', 'Other']},
                        {'name': 'paper_title', 'type': 'text', 'label': 'Title of the Paper / Article', 'required': True},
                        {'name': 'conference_journal_book_title', 'type': 'text', 'label': 'Title of the Conference / Journal / Book (for book chapter)', 'required': True},
                        {'name': 'publisher_name', 'type': 'text', 'label': "Publisher's Name", 'required': True},
                        {'name': 'publication_year', 'type': 'text', 'label': 'Publication Date (Year)', 'required': True},
                        {'name': 'keywords', 'type': 'text', 'label': 'Keywords', 'required': False},
                        {'name': 'abstract', 'type': 'textarea', 'label': 'Abstract', 'required': False},
                        {'name': 'paper_url', 'type': 'text', 'label': 'URL for the Paper / Article', 'required': False},
                        {'name': 'article_classification', 'type': 'text', 'label': 'Article Classification', 'required': False},
                        {'name': 'article_second_classification', 'type': 'text', 'label': 'Article Second Classification', 'required': False},
                        {'name': 'article_third_classification', 'type': 'text', 'label': 'Article Third Classification', 'required': False}
                    ]
                },
                'ar': {
                    'title': 'قاعدة بيانات الأبحاث والباحثين',
                    'description': 'تقديم الأبحاث والمنشورات لقاعدة بيانات أبحاث حوسبة القرآن والعلوم الإسلامية.',
                    'fields': [
                        {'name': 'publication_type', 'type': 'select', 'label': 'نوع البحث', 'required': True,
                         'options': ['بحث في مجلة', 'كتاب', 'فصل في كتاب', 'ورقة مؤتمر', 'أخرى']},
                        {'name': 'paper_title', 'type': 'text', 'label': 'اسم او عنوان البحث / الورقة', 'required': True},
                        {'name': 'conference_journal_book_title', 'type': 'text', 'label': 'عنوان المؤتمر / المجلة / الكتاب (فصل في كتاب)', 'required': True},
                        {'name': 'publisher_name', 'type': 'text', 'label': 'اسم جهة النشر', 'required': True},
                        {'name': 'publication_year', 'type': 'text', 'label': 'تاريخ سنة النشر', 'required': True},
                        {'name': 'keywords', 'type': 'text', 'label': 'الكلمات المفتاحية', 'required': False},
                        {'name': 'abstract', 'type': 'textarea', 'label': 'الملخص او الوصف للبحث او الورقة', 'required': False},
                        {'name': 'paper_url', 'type': 'text', 'label': 'رابط الورقة / البحث كاملاً', 'required': False},
                        {'name': 'article_classification', 'type': 'text', 'label': 'تصنيف موضوع البحث / الورقة', 'required': False},
                        {'name': 'article_second_classification', 'type': 'text', 'label': 'تصنيف ثاني', 'required': False},
                        {'name': 'article_third_classification', 'type': 'text', 'label': 'تصنيف ثالث', 'required': False}
                    ]
                }
            },
            'general_suggestion': {
                'en': {
                    'title': 'General Suggestions',
                    'description': 'Submit general suggestions and feedback for the institute.',
                    'fields': [
                        {'name': 'email', 'type': 'email', 'label': 'Email', 'required': True},
                        {'name': 'full_name', 'type': 'text', 'label': 'Full Name', 'required': True},
                        {'name': 'suggestion_type', 'type': 'select', 'label': 'Suggestion Type', 'required': True,
                         'options': ['Website Improvement', 'Research Collaboration', 'Educational Program', 'Technical Enhancement', 'Other']},
                        {'name': 'suggestion_title', 'type': 'text', 'label': 'Suggestion Title', 'required': True},
                        {'name': 'suggestion_description', 'type': 'textarea', 'label': 'Detailed Description', 'required': True},
                        {'name': 'priority_level', 'type': 'select', 'label': 'Priority Level', 'required': False,
                         'options': ['Low', 'Medium', 'High', 'Critical']},
                        {'name': 'implementation_timeline', 'type': 'text', 'label': 'Suggested Timeline', 'required': False},
                        {'name': 'additional_comments', 'type': 'textarea', 'label': 'Additional Comments', 'required': False}
                    ]
                },
                'ar': {
                    'title': 'الاقتراحات العامة',
                    'description': 'تقديم الاقتراحات العامة والملاحظات للمعهد.',
                    'fields': [
                        {'name': 'email', 'type': 'email', 'label': 'البريد الإلكتروني', 'required': True},
                        {'name': 'full_name', 'type': 'text', 'label': 'الاسم الكامل', 'required': True},
                        {'name': 'suggestion_type', 'type': 'select', 'label': 'نوع الاقتراح', 'required': True,
                         'options': ['تحسين الموقع', 'التعاون البحثي', 'البرنامج التعليمي', 'التحسين التقني', 'أخرى']},
                        {'name': 'suggestion_title', 'type': 'text', 'label': 'عنوان الاقتراح', 'required': True},
                        {'name': 'suggestion_description', 'type': 'textarea', 'label': 'الوصف التفصيلي', 'required': True},
                        {'name': 'priority_level', 'type': 'select', 'label': 'مستوى الأولوية', 'required': False,
                         'options': ['منخفض', 'متوسط', 'عالي', 'حرج']},
                        {'name': 'implementation_timeline', 'type': 'text', 'label': 'الجدول الزمني المقترح', 'required': False},
                        {'name': 'additional_comments', 'type': 'textarea', 'label': 'تعليقات إضافية', 'required': False}
                    ]
                }
            }
        }
        
        return forms_config.get(form_type, {}).get(language, {})

