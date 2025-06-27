import streamlit as st
from typing import Dict, Any, List
import base64

# Language translations
TRANSLATIONS = {
    'en': {
        # Navigation
        'the_institute': 'The Institute',
        'mission': 'Mission',
        'board_of_directors': 'Board of Directors',
        'bylaws': 'Bylaws',
        'policy': 'Policy',
        'all_activities': 'All Activities',
        'info_about_activities': 'Info About Activities',
        'training_trainers': 'Training the Trainers',
        'magazines': 'Magazines',
        'members': 'Members',
        'projects': 'Projects',
        'news': 'News',
        'donation': 'Donation',
        'forms': 'Forms',
        'nomination_membership': 'Nomination for Membership',
        'researchers_database': 'Researches and Researchers Database',
        'database_contribution': 'Database Contribution',
        'suggestions': 'Suggestions',
        'general_suggestions': 'General Suggestions',
        'research_project_ideas': 'Research / Project Ideas',
        'sign_in': 'Sign In',
        'sign_up': 'Sign Up',
        'sign_out': 'Sign Out',
        'dashboard': 'Dashboard',
        'contact_us': 'Contact Us',
        
        # Navigation and UI
        'back_to_forms': 'Back to Forms',
        'select_form_message': 'Please select a form to fill out:',
        'apply_now': 'Apply Now',
        'submit_research': 'Submit Research',
        'nominate_member': 'Nominate Member',
        'submit_idea': 'Submit Idea',
        'fill_required_fields': 'Please fill in all required fields',
        
        # Form descriptions
        'membership_desc': 'Apply for institute membership',
        'research_desc': 'Submit research information to our database',
        'nomination_desc': 'Nominate someone for membership',
        'suggestions_desc': 'Submit suggestions for research and application projects',
        'membership_form_desc': 'Apply for membership in the International Computing Institute for Quran and Islamic Sciences.',
        'research_form_desc': 'Submit research information to our database.',
        'nomination_form_desc': 'Nominate someone for membership in the institute.',
        'suggestions_form_desc': 'Submit suggestions and feedback to help improve our institute.',
        'bank_of_ideas_desc': 'Submit suggestions for research and application projects to serve the Holy Quran, Islamic sciences, and linguistic sciences.',
        
        # Form field labels
        'full_name': 'Full Name',
        'current_institution': 'Current Institution', 
        'current_position': 'Current Position',
        'academic_degree': 'Academic Degree',
        'specialization': 'Specialization',
        'years_experience': 'Years of Experience',
        'research_interests': 'Research Interests',
        'motivation': 'Motivation for Joining',
        'cv_link': 'CV/Resume Link (optional)',
        'additional_info': 'Additional Information (optional)',
        'research_title': 'Research Title',
        'authors': 'Authors',
        'publication_year': 'Publication Year',
        'journal_conference': 'Journal/Conference',
        'abstract': 'Abstract',
        'keywords': 'Keywords (comma-separated)',
        'doi_link': 'DOI/Link',
        'research_type': 'Research Type',
        'field_of_study': 'Field of Study',
        'journal_article': 'Journal Article',
        'conference_paper': 'Conference Paper',
        'book': 'Book',
        'thesis': 'Thesis',
        'other': 'Other',
        'nominee_name': 'Nominee Full Name',
        'nominee_email': 'Nominee Email',
        'nominee_institution': 'Nominee Institution',
        'nominee_position': 'Nominee Position',
        'nominator_name': 'Your Name (Nominator)',
        'nominator_email': 'Your Email',
        'relationship': 'Relationship to Nominee',
        'nomination_reason': 'Reason for Nomination',
        'nominee_achievements': 'Nominee\'s Key Achievements',
        'supporting_documents': 'Supporting Documents (links)',
        'additional_comments': 'Additional Comments (optional)',
        'your_name': 'Your Name',
        'subject': 'Subject',
        'category': 'Category',
        'suggestion_feedback': 'Your Suggestion/Feedback',
        'priority': 'Priority',
        'contact_back': 'I would like to be contacted about this suggestion',
        'general': 'General',
        'website': 'Website',
        'research': 'Research',
        'events': 'Events',
        'membership': 'Membership',
        'low': 'Low',
        'medium': 'Medium',
        'high': 'High',
        'submitter_name': 'Name of Submitter',
        'title_degrees': 'Title and Scientific Degrees',
        'project_title': 'Title of the Research Project',
        'project_nature': 'Nature of the project',
        'project_nature_other': 'Other Nature (if selected)',
        'project_type': 'Type of the Project',
        'project_type_other': 'Other Type (if selected)',
        'brief_description': 'Brief Description of Proposed Project',
        'specialization_area': 'Specialization area of the Research/Project',
        'objectives': 'Objectives/Goals of the Research/Project',
        'benefits': 'Benefits of the Research/Project',
        'web_links': 'Web links URLs',
        'additional_notes': 'Additional Notes',
        'computing': 'Computing',
        'religious': 'Religious',
        'linguistic': 'Linguistic',
        'other_specify': 'Other - Specify',
        'theoretical_research': 'Theoretical Research',
        'applied_research': 'Applied Research',
        'field_study': 'Field Study',
        
        # Additional form fields
        'country': 'Country',
        'phone_number': 'Phone Number',
        'address_optional': 'Address (Optional)',
        'website_url_optional': 'Website/Profile URL (Optional)',
        'publisher': 'Publisher',
        
        # Common UI
        'welcome': 'Welcome',
        'home': 'Home',
        'about': 'About',
        'language': 'Language',
        'english': 'English',
        'arabic': 'Arabic',
        'submit': 'Submit',
        'cancel': 'Cancel',
        'save': 'Save',
        'edit': 'Edit',
        'delete': 'Delete',
        'search': 'Search',
        'filter': 'Filter',
        'loading': 'Loading...',
        'success': 'Success',
        'error': 'Error',
        'warning': 'Warning',
        'info': 'Information',
        'submit_application': 'Submit Application',
        'submit_nomination': 'Submit Nomination',
        'submit_suggestion': 'Submit Suggestion',
        
        # Authentication
        'email': 'Email',
        'password': 'Password',
        'confirm_password': 'Confirm Password',
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'login': 'Login',
        'register': 'Register',
        'forgot_password': 'Forgot Password',
        'reset_password': 'Reset Password',
        'verify_email': 'Verify Email',
        
        # Institute content
        'institute_name': 'International Computing Institute for Quran and Islamic Sciences',
        'institute_vision': 'A global leadership and reference in computing the Holy Quran, Islamic sciences and the Arabic language',
        'institute_mission': 'Establishing and developing a solid scientific reference for computing the Holy Quran, Islamic sciences and the Arabic language, and developing research, specialized scientific studies, computer programs and websites in this field, through distinguished and sustainable institutional work, and in cooperation and coordination with institutions and individuals specialized in computer, legal and linguistic fields; Which achieves an integrated vision and distinct outputs.',
        
        # Content sections
        'vision': 'Vision',
        'activities': 'Activities',
        'publications': 'Publications',
        'conferences': 'Conferences',
        'training': 'Training',
        'partnerships': 'Partnerships',
        
        # Forms
        'membership_application': 'Membership Application',
        'bank_of_ideas': 'Bank of Ideas: Research Project Suggestions',
        'member_nomination': 'Member Nomination Form',
        'researcher_profile': 'Researcher Database Profile',
        'data_contribution': 'Database Contribution Form',
        
        # Status messages
        'application_submitted': 'Your application has been submitted successfully!',
        'form_submitted': 'Your form has been submitted successfully!',
        'please_login': 'Please login to access this feature',
        'access_denied': 'Access denied',
        'page_not_found': 'Page not found',
        
        # Footer
        'footer_rights': 'All rights reserved',
    },
    'ar': {
        # Navigation
        'the_institute': 'المعهد',
        'mission': 'الرسالة',
        'board_of_directors': 'المجلس الإداري',
        'bylaws': 'اللوائح',
        'policy': 'السياسات',
        'all_activities': 'كل النشاطات',
        'info_about_activities': 'معلومات عن الأنشطة',
        'training_trainers': 'تدريب المدربين',
        'magazines': 'المجلات',
        'members': 'الأعضاء',
        'projects': 'المشاريع',
        'news': 'الأخبار',
        'donation': 'الدعم',
        'forms': 'نماذج',
        'nomination_membership': 'ترشيح للعضوية',
        'researchers_database': 'قاعدة بيانات الباحثين والأبحاث',
        'database_contribution': 'المساهمة بقاعدة البيانات',
        'suggestions': 'اقتراحات',
        'general_suggestions': 'الاقتراحات العامة',
        'research_project_ideas': 'أفكار البحوث والمشاريع',
        'sign_in': 'الدخول',
        'sign_up': 'التسجيل',
        'sign_out': 'الخروج',
        'dashboard': 'لوحة التحكم',
        'contact_us': 'اتصل بنا',
        
        # Navigation and UI
        'back_to_forms': 'العودة للنماذج',
        'select_form_message': 'يرجى اختيار نموذج للتعبئة:',
        'apply_now': 'تقدم الآن',
        'submit_research': 'إرسال البحث',
        'nominate_member': 'ترشيح عضو',
        'submit_idea': 'إرسال فكرة',
        'fill_required_fields': 'يرجى تعبئة جميع الحقول المطلوبة',
        
        # Form descriptions
        'membership_desc': 'تقدم بطلب للحصول على عضوية المعهد',
        'research_desc': 'إرسال معلومات البحث إلى قاعدة بياناتنا',
        'nomination_desc': 'ترشيح شخص للحصول على العضوية',
        'suggestions_desc': 'تقديم اقتراحات لمشاريع البحث والتطبيق',
                    'membership_form_desc': 'تقدم بطلب للحصول على عضوية في المعهد العالمي لحوسبة القرآن والعلوم الإسلامية.',
        'research_form_desc': 'إرسال معلومات البحث إلى قاعدة بياناتنا.',
        'nomination_form_desc': 'ترشيح شخص للحصول على العضوية في المعهد.',
        'suggestions_form_desc': 'تقديم اقتراحات وملاحظات لمساعدة في تحسين معهدنا.',
        'bank_of_ideas_desc': 'تقديم اقتراحات لمشاريع البحث والتطبيق لخدمة القرآن الكريم والعلوم الإسلامية واللغوية.',
        
        # Form field labels
        'full_name': 'الاسم الكامل',
        'current_institution': 'المؤسسة الحالية',
        'current_position': 'المنصب الحالي',
        'academic_degree': 'الدرجة الأكاديمية',
        'specialization': 'التخصص',
        'years_experience': 'سنوات الخبرة',
        'research_interests': 'اهتمامات البحث',
        'motivation': 'الدافع للانضمام',
        'cv_link': 'رابط السيرة الذاتية (اختياري)',
        'additional_info': 'معلومات إضافية (اختياري)',
        'research_title': 'عنوان البحث',
        'authors': 'المؤلفون',
        'publication_year': 'سنة النشر',
        'journal_conference': 'المجلة/المؤتمر',
        'abstract': 'الملخص',
        'keywords': 'الكلمات المفتاحية (مفصولة بفواصل)',
        'doi_link': 'رابط DOI',
        'research_type': 'نوع البحث',
        'field_of_study': 'مجال الدراسة',
        'journal_article': 'مقال في مجلة',
        'conference_paper': 'ورقة مؤتمر',
        'book': 'كتاب',
        'thesis': 'أطروحة',
        'other': 'أخرى',
        'nominee_name': 'اسم المرشح الكامل',
        'nominee_email': 'بريد المرشح الإلكتروني',
        'nominee_institution': 'مؤسسة المرشح',
        'nominee_position': 'منصب المرشح',
        'nominator_name': 'اسمك (المرشح)',
        'nominator_email': 'بريدك الإلكتروني',
        'relationship': 'العلاقة بالمرشح',
        'nomination_reason': 'سبب الترشيح',
        'nominee_achievements': 'إنجازات المرشح الرئيسية',
        'supporting_documents': 'الوثائق الداعمة (روابط)',
        'additional_comments': 'تعليقات إضافية (اختياري)',
        'your_name': 'اسمك',
        'subject': 'الموضوع',
        'category': 'التصنيف',
        'suggestion_feedback': 'اقتراحك/ملاحظاتك',
        'priority': 'الأولوية',
        'contact_back': 'أود أن يتم التواصل معي حول هذا الاقتراح',
        'general': 'عام',
        'website': 'الموقع الإلكتروني',
        'research': 'البحث',
        'events': 'الفعاليات',
        'membership': 'العضوية',
        'low': 'منخفض',
        'medium': 'متوسط',
        'high': 'عالي',
        'submitter_name': 'اسم مقدم الطلب',
        'title_degrees': 'اللقب والدرجات العلمية',
        'project_title': 'عنوان المشروع البحثي',
        'project_nature': 'طبيعة المشروع',
        'project_nature_other': 'طبيعة أخرى (إذا تم اختيارها)',
        'project_type': 'نوع المشروع',
        'project_type_other': 'نوع آخر (إذا تم اختياره)',
        'brief_description': 'وصف موجز للمشروع المقترح',
        'specialization_area': 'منطقة تخصص البحث/المشروع',
        'objectives': 'الأهداف/الغايات من البحث/المشروع',
        'benefits': 'فوائد البحث/المشروع',
        'web_links': 'روابط مواقع الويب',
        'additional_notes': 'ملاحظات إضافية',
        'computing': 'حاسوبي',
        'religious': 'ديني',
        'linguistic': 'لغوي',
        'other_specify': 'أخرى - حدد',
        'theoretical_research': 'بحث نظري',
        'applied_research': 'بحث تطبيقي',
        'field_study': 'دراسة ميدانية',
        
        # Additional form fields
        'country': 'البلد',
        'phone_number': 'رقم الهاتف',
        'address_optional': 'العنوان (اختياري)',
        'website_url_optional': 'رابط الموقع/الملف الشخصي (اختياري)',
        'publisher': 'الناشر',
        
        # Common UI
        'welcome': 'مرحباً',
        'home': 'الرئيسية',
        'about': 'حول',
        'language': 'اللغة',
        'english': 'English',
        'arabic': 'العربية',
        'submit': 'إرسال',
        'cancel': 'إلغاء',
        'save': 'حفظ',
        'edit': 'تعديل',
        'delete': 'حذف',
        'search': 'بحث',
        'filter': 'تصفية',
        'loading': 'جاري التحميل...',
        'success': 'نجح',
        'error': 'خطأ',
        'warning': 'تحذير',
        'info': 'معلومات',
        'submit_application': 'إرسال الطلب',
        'submit_nomination': 'إرسال الترشيح',
        'submit_suggestion': 'إرسال الاقتراح',
        
        # Authentication
        'email': 'البريد الإلكتروني',
        'password': 'كلمة المرور',
        'confirm_password': 'تأكيد كلمة المرور',
        'first_name': 'الاسم الأول',
        'last_name': 'اسم العائلة',
        'login': 'تسجيل الدخول',
        'register': 'التسجيل',
        'forgot_password': 'نسيت كلمة المرور',
        'reset_password': 'إعادة تعيين كلمة المرور',
        'verify_email': 'تحقق من البريد الإلكتروني',
        
        # Institute content
                    'institute_name': 'المعهد العالمي لحوسبة القرآن الكريم والعلوم الإسلامية',
        'institute_vision': 'ريادة وقيادة عالمية ومرجعية في حوسبة القرآن الكريم والعلوم الإسلامية واللغة العربية',
        'institute_mission': 'إنشاء وتطوير مرجعية علمية راسخة لحوسبة القرآن الكريم والعلوم الإسلامية واللغة العربية، وتطوير البحوث والدراسات العلمية المتخصصة والبرامج الحاسوبية والمواقع الإلكترونية في هذا المجال، من خلال عمل مؤسسي متميز ومستدام، وبالتعاون والتنسيق مع المؤسسات والأفراد المتخصصين في المجالات الحاسوبية والشرعية واللغوية؛ مما يحقق رؤية متكاملة ومخرجات متميزة.',
        
        # Content sections
        'vision': 'الرؤية',
        'objectives': 'الأهداف',
        'activities': 'الأنشطة',
        'publications': 'المنشورات',
        'conferences': 'المؤتمرات',
        'training': 'التدريب',
        'partnerships': 'الشراكات',
        
        # Forms
        'membership_application': 'طلب العضوية',
        'bank_of_ideas': 'بنك الأفكار: اقتراحات المشاريع البحثية',
        'member_nomination': 'نموذج ترشيح العضو',
        'researcher_profile': 'ملف الباحث في قاعدة البيانات',
        'data_contribution': 'نموذج المساهمة في قاعدة البيانات',
        
        # Status messages
        'application_submitted': 'تم إرسال طلبك بنجاح!',
        'form_submitted': 'تم إرسال النموذج بنجاح!',
        'please_login': 'يرجى تسجيل الدخول للوصول إلى هذه الميزة',
        'access_denied': 'تم رفض الوصول',
        'page_not_found': 'الصفحة غير موجودة',
        
        # Footer
        'footer_rights': 'جميع الحقوق محفوظة',
    }
}

def get_text(key: str, lang: str = 'en') -> str:
    """Get translated text for a given key and language"""
    return TRANSLATIONS.get(lang, {}).get(key, key)

def get_language_direction(lang: str) -> str:
    """Get text direction for language"""
    return 'rtl' if lang == 'ar' else 'ltr'

def get_text_alignment(lang: str) -> str:
    """Get text alignment for language"""
    return 'right' if lang == 'ar' else 'left'

def get_font_family(lang: str) -> str:
    """Get appropriate font family for language"""
    if lang == 'ar':
        return "'Sakkal Majalla', 'Amiri', 'Noto Sans Arabic', 'Arial Unicode MS', sans-serif"
    else:
        return "'Times New Roman', 'Times', serif"

def apply_language_styles(lang: str) -> str:
    """Generate CSS styles for language-specific formatting"""
    direction = get_language_direction(lang)
    alignment = get_text_alignment(lang)
    font_family = get_font_family(lang)
    
    return f"""
    <style>
    /* Global language-aware styling */
    .main-content {{
        direction: {direction};
        font-family: {font_family};
    }}
    
    /* Text alignment based on language */
    .language-content {{
        direction: {direction};
        text-align: {alignment};
        font-family: {font_family};
    }}
    
    /* Form inputs and text areas with language-specific alignment */
    .language-content input,
    .language-content textarea,
    .language-content select {{
        direction: {direction};
        text-align: {alignment};
        font-family: {font_family};
    }}
    
    .stTextInput > div > div > input {{
        direction: {direction};
        text-align: {alignment} !important;
        font-family: {font_family};
        font-size: {'1.3em' if lang == 'ar' else '1em'} !important;
    }}
    
    .stTextArea > div > div > textarea {{
        direction: {direction};
        text-align: {alignment} !important;
        font-family: {font_family};
        font-size: {'1.3em' if lang == 'ar' else '1em'} !important;
    }}
    
    .stSelectbox > div > div > select {{
        direction: {direction};
        text-align: {alignment} !important;
        font-family: {font_family};
        font-size: 0.8em !important;
    }}
    
    /* Form field labels - positioned above fields */
    .stTextInput > label,
    .stTextArea > label,
    .stSelectbox > label,
    .stNumberInput > label,
    .stDateInput > label {{
        text-align: {alignment} !important;
        font-family: {font_family};
        font-size: {'1.3em' if lang == 'ar' else '1em'} !important;
        display: block !important;
        width: 100% !important;
        margin-bottom: 5px !important;
    }}
    
    /* Additional label styling for better positioning */
    .stTextInput label,
    .stTextArea label,
    .stSelectbox label,
    .stNumberInput label,
    .stDateInput label {{
        text-align: {alignment} !important;
        font-family: {font_family};
        font-size: {'1.3em' if lang == 'ar' else '1em'} !important;
        display: block !important;
        width: 100% !important;
        margin-bottom: 5px !important;
    }}
    
    /* Main titles - center aligned */
    .main-title,
    .main-subtitle,
    h1 {{
        text-align: center !important;
        font-family: {font_family};
    }}
    
    /* Section headings - language-specific alignment */
    h2, h3, h4, h5, h6 {{
        text-align: {alignment} !important;
        font-family: {font_family};
    }}
    
    /* Regular content - language-specific alignment and subtle sizing */
    p, div, span, li {{
        text-align: {alignment};
        font-family: {font_family};
        font-size: {'1.1em' if lang == 'ar' else '1em'};
    }}
    
    /* Board member names - subtle size adjustment */
    .board-member-name {{
        font-size: {'1.2em' if lang == 'ar' else '0.95em'} !important;
        text-align: {alignment};
        font-family: {font_family};
    }}
    
    /* Board member position */
    .board-member-position {{
        font-size: {'1.1em' if lang == 'ar' else '0.9em'} !important;
        text-align: {alignment};
        font-family: {font_family};
    }}
    
    /* Button text - center aligned */
    .stButton > button {{
        text-align: center !important;
        font-family: {font_family};
    }}
    
    /* Language-specific content containers */
    .arabic-content {{
        direction: rtl;
        text-align: right;
        font-family: {font_family};
    }}
    
    .english-content {{
        direction: ltr;
        text-align: left;
        font-family: {font_family};
    }}
    
    /* Elegant spacing dividers */
    .elegant-divider {{
        height: 2px;
        background: linear-gradient(90deg, transparent, #e9ecef, transparent);
        margin: 15px 0;
        border-radius: 1px;
    }}
    
    /* Form containers */
    .form-container {{
        direction: {direction};
        text-align: {alignment};
        font-family: {font_family};
        padding: 20px;
        border-radius: 10px;
        background: #f8f9fa;
        margin: 10px 0;
    }}
    
    /* Content sections */
    .content-section {{
        direction: {direction};
        text-align: {alignment};
        font-family: {font_family};
        padding: 15px;
        margin: 10px 0;
        border-left: 4px solid #2E8B57;
        background: #f9f9f9;
    }}
    
    /* Footer styling */
    .app-footer {{
        direction: {direction};
        text-align: center;
        font-family: {font_family};
        background: linear-gradient(135deg, #2E8B57, #4682B4);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin-top: 30px;
    }}
    
    /* Contact email styling */
    .contact-email {{
        font-size: 1.3em !important;
        font-weight: bold;
        color: #2E8B57;
        text-align: {alignment};
        font-family: {font_family};
    }}
    
    /* Form containers for proper label alignment */
    .stForm {{
        direction: {direction};
    }}
    
    .stForm label {{
        text-align: {alignment} !important;
        display: block !important;
        width: 100% !important;
        font-family: {font_family};
        font-size: {'1.3em' if lang == 'ar' else '1em'} !important;
        margin-bottom: 5px !important;
    }}
    
    /* Override Streamlit's default alignment where needed */
    .stMarkdown > div > p {{
        text-align: {alignment};
    }}
    
    .stText > div {{
        text-align: {alignment};
    }}
    
    /* Streamlit header elements */
    .stMarkdown > div > h1 {{
        text-align: center !important;
        font-family: {font_family};
    }}
    
    .stMarkdown > div > h2,
    .stMarkdown > div > h3,
    .stMarkdown > div > h4,
    .stMarkdown > div > h5,
    .stMarkdown > div > h6 {{
        text-align: {alignment} !important;
        font-family: {font_family};
    }}
    </style>
    """

def create_language_selector(current_lang: str) -> str:
    """Create language selector buttons"""
    english_active = "background: #4169E1;" if current_lang == 'en' else ""
    arabic_active = "background: #4169E1;" if current_lang == 'ar' else ""
    
    return f"""
    <div style="text-align: center; margin: 10px 0;">
        <button class="language-button" style="{english_active}" onclick="window.location.href='?lang=en'">
            🇺🇸 English
        </button>
        <button class="language-button" style="{arabic_active}" onclick="window.location.href='?lang=ar'">
            🇸🇦 العربية
        </button>
    </div>
    """

def create_header(lang: str) -> str:
    """Create the main header with logo and title"""
    institute_name = get_text('institute_name', lang)
    vision = get_text('institute_vision', lang)
    
    logo_position = "left: 20px;" if lang == 'en' else "right: 20px;"
    
    return f"""
    <div class="islamic-gradient" style="position: relative;">
        <img src="data:image/jpeg;base64,{get_logo_base64()}" 
             style="position: absolute; top: 20px; {logo_position} width: 80px; height: 80px; border-radius: 10px;">
        <div class="centered-title" style="padding: 20px 120px;">
            <h1 style="margin: 0; font-size: 2.5em; text-align: center;">{institute_name}</h1>
            <h3 style="margin: 10px 0 0 0; font-size: 1.2em; text-align: center; opacity: 0.9;">{vision}</h3>
        </div>
    </div>
    """

def get_logo_base64() -> str:
    """Get base64 encoded logo"""
    try:
        with open('/home/ubuntu/quran_institute_app/logo.jpg', 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

def create_navigation_menu(lang: str, current_page: str = 'home') -> List[str]:
    """Create navigation menu items"""
    menu_items = [
        ('home', get_text('home', lang), '🏠'),
        ('institute', get_text('the_institute', lang), '🏛️'),
        ('activities', get_text('all_activities', lang), '📅'),
        ('members', get_text('members', lang), '👥'),
        ('projects', get_text('projects', lang), '🚀'),
        ('news', get_text('news', lang), '📰'),
        ('forms', get_text('forms', lang), '📝'),
        ('suggestions', get_text('suggestions', lang), '💡'),
        ('signin', get_text('sign_in', lang), '🔐'),
    ]
    
    return [f"{icon} {label}" for key, label, icon in menu_items]

def display_content_section(title: str, content: str, lang: str):
    """Display a content section with proper language formatting"""
    st.markdown(apply_language_styles(lang), unsafe_allow_html=True)
    st.markdown(f"""
    <div class="content-section">
        <h3>{title}</h3>
        <p>{content}</p>
    </div>
    """, unsafe_allow_html=True)

def create_form_container(lang: str):
    """Create a form container with proper language styling"""
    st.markdown(apply_language_styles(lang), unsafe_allow_html=True)
    return st.container()

def get_institute_objectives(lang: str) -> List[str]:
    """Get institute objectives in the specified language"""
    if lang == 'ar':
        return [
            "إنشاء مرجعية علمية رقمية للبيانات والمعلومات الحاسوبية المتعلقة بالقرآن الكريم والعلوم الإسلامية واللغة العربية وكل ما يتعلق بها.",
            "تكوين مظلة للباحثين والمهنيين المهتمين بحوسبة القرآن الكريم والعلوم الإسلامية واللغة العربية، للتنسيق في الجهود فيما بينهم.",
            "إقامة شراكات علمية بين المتخصصين من الأفراد والمؤسسات المعنية بحوسبة القرآن الكريم والعلوم الشرعية واللغة العربية والعلوم ذات الصلة.",
            "وضع معايير وضوابط للبيانات التي يتم التعامل معها في مجالات حوسبة القرآن الكريم والعلوم الإسلامية واللغة العربية للوصول إلى نتائج علمية صحيحة ودقيقة.",
            "تطوير وتدريب الباحثين والمهتمين بحوسبة القرآن الكريم والعلوم الإسلامية واللغة العربية، مع إعداد مواد تدريبية منهجية ونموذجية.",
            "فتح قنوات التواصل مع التخصصات المختلفة العلمية والشرعية والأدبية وغيرها لخدمة حوسبة القرآن الكريم والعلوم الإسلامية واللغة العربية.",
            "تشجيع البحث العلمي في مجالات حوسبة القرآن الكريم والعلوم الإسلامية واللغة العربية، وتوفير موضوعات البحث وأفكار التطوير والحلول التقنية.",
            "نشر المعرفة والتوعية العامة بنتائج البحوث في حوسبة القرآن الكريم والعلوم الإسلامية واللغة العربية بطريقة سهلة ومتاحة.",
            "تشجيع الباحثين والمؤسسات المعنية بحوسبة القرآن الكريم والعلوم الإسلامية واللغة العربية على المزيد من إنتاجاتهم العلمية والإلكترونية بالبرمجيات مفتوحة المصدر."
        ]
    else:
        return [
            "Establishing a digital scientific reference for computer data and information related to the Holy Quran, Islamic sciences, the Arabic language, and everything related to it.",
            "Forming an umbrella for researchers and professionals interested in computing the Noble Quran, Islamic sciences and the Arabic language, to coordinate efforts among them.",
            "Establishing scientific partnerships between specialists from individuals and institutions concerned with computing the Noble Quran, forensic sciences, the Arabic language, and related sciences.",
            "Setting standards and controls for data that are dealt with in the fields of computing the Holy Quran, Islamic sciences and the Arabic language in order to reach correct and accurate scientific results.",
            "Developing and training researchers and those interested in computing the Noble Quran, Islamic sciences and the Arabic language, while preparing methodological and exemplary training materials.",
            "Opening channels of communication with different disciplines of scientific, legal, literary and others to serve the computerization of the Holy Quran, Islamic sciences and the Arabic language.",
            "Encouraging scientific research in the fields of computing the Noble Quran, Islamic sciences and the Arabic language, and providing research topics, development ideas and technical solutions.",
            "Dissemination of knowledge and public awareness of the results of research in computing the Holy Quran, Islamic sciences and the Arabic language in an easy and accessible way.",
            "Encouraging researchers and institutions concerned with computing the Noble Quran, Islamic sciences and the Arabic language to further their scientific and electronic productions with open source software."
        ]

