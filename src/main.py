"""
Fixed Quran Institute Streamlit Application
Main application file with all forms functionality working correctly.
"""

import streamlit as st
import sqlite3
import hashlib
import secrets
from datetime import datetime
import re
import json
from typing import Dict, Any, Optional

# Import termcolor with fallback
try:
    from termcolor import colored
    print("✅ termcolor imported successfully")
except ImportError as e:
    print(f"❌ termcolor not available: {e}")
    # Fallback function if termcolor is not available
    def colored(text, color=None):
        return text

# Import custom modules (updated for deployment)
# Use direct imports for Streamlit Cloud deployment
try:
    from content_manager import ContentManager
    print(colored("✅ ContentManager imported successfully", "green"))
except Exception as e:
    print(colored(f"❌ Error importing ContentManager: {str(e)}", "red"))
    print(colored(f"Error type: {type(e).__name__}", "red"))
    raise

# from forms_manager import FormsManager
# from database import Database
# Try Turso cloud SQLite, fallback to Google Cloud Storage if needed
try:
    from database_turso import TursoDatabase as Database
    print(colored("✅ TursoDatabase imported successfully", "green"))
    USE_TURSO = True
except Exception as e:
    print(colored(f"❌ Error importing TursoDatabase: {str(e)}", "red"))
    print(colored("🔄 Falling back to Google Cloud Storage database...", "yellow"))
    try:
        from database import Database
        print(colored("✅ GCS Database imported as fallback", "green"))
        USE_TURSO = False
    except Exception as fallback_error:
        print(colored(f"❌ Fallback also failed: {fallback_error}", "red"))
        raise

try:
    if USE_TURSO:
        from forms_manager_turso import TursoFormsManager as FormsManager
        print(colored("✅ TursoFormsManager imported successfully", "green"))
    else:
        from forms_manager import FormsManager
        print(colored("✅ GCS FormsManager imported as fallback", "green"))
except Exception as e:
    print(colored(f"❌ Error importing FormsManager: {str(e)}", "red"))
    print(colored(f"Error type: {type(e).__name__}", "red"))
    raise

try:
    from ui_utils import get_text, apply_language_styles, get_language_direction
    print(colored("✅ UI utils imported successfully", "green"))
except Exception as e:
    print(colored(f"❌ Error importing UI utils: {str(e)}", "red"))
    print(colored(f"Error type: {type(e).__name__}", "red"))
    raise

try:
    from user_preferences import UserPreferences
    print(colored("✅ UserPreferences imported successfully", "green"))
except Exception as e:
    print(colored(f"❌ Error importing UserPreferences: {str(e)}", "red"))
    print(colored(f"Error type: {type(e).__name__}", "red"))
    raise

# Page configuration
st.set_page_config(
    page_title="International Computing Institute for Quran and Islamic Sciences",
    page_icon="🕌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize user preferences manager
@st.cache_resource
def get_user_preferences():
    print(colored("⚙️ Loading user preferences...", "green"))
    return UserPreferences()

user_prefs = get_user_preferences()

# Initialize session state with user preferences
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'user_id' not in st.session_state:
    st.session_state.user_id = None
if 'language' not in st.session_state:
    # Use saved language preference (defaults to Arabic)
    st.session_state.language = user_prefs.get_language()
    print(colored(f"🌐 Setting default language to: {st.session_state.language}", "cyan"))
if 'page' not in st.session_state:
    st.session_state.page = 'home'

print(colored("🔧 Initializing Streamlit application...", "cyan"))

# Simple email validation function
def validate_email(email: str) -> bool:
    """Simple email validation with space checking"""
    if not email:
        return False
    
    email_stripped = email.strip()
    
    # Check for spaces within the email (after trimming)
    if ' ' in email_stripped:
        return False
    
    # Basic format validation
    return '@' in email_stripped and '.' in email_stripped and len(email_stripped) > 5

# Initialize managers
@st.cache_resource
def get_content_manager():
    try:
        print(colored("📚 Loading content manager...", "green"))
        return ContentManager()
    except Exception as e:
        print(colored(f"❌ Error loading ContentManager: {str(e)}", "red"))
        print(colored(f"Error type: {type(e).__name__}", "red"))
        import traceback
        print(colored(f"Traceback: {traceback.format_exc()}", "red"))
        raise

@st.cache_resource
def get_forms_manager():
    try:
        print(colored("📝 Loading forms manager...", "green"))
        db = get_database()
        return FormsManager(db)
    except Exception as e:
        print(colored(f"❌ Error loading FormsManager: {str(e)}", "red"))
        print(colored(f"Error type: {type(e).__name__}", "red"))
        raise

@st.cache_resource
def get_database():
    try:
        print(colored("🗄️ Loading database...", "green"))
        return Database()
    except Exception as e:
        print(colored(f"❌ Error loading Database: {str(e)}", "red"))
        print(colored(f"Error type: {type(e).__name__}", "red"))
        raise

# Initialize managers with error handling
try:
    content_manager = get_content_manager()
    print(colored("✅ ContentManager initialized successfully", "green"))
except Exception as e:
    print(colored(f"❌ Failed to initialize ContentManager: {str(e)}", "red"))
    st.error(f"Failed to initialize ContentManager: {str(e)}")
    st.stop()

try:
    forms_manager = get_forms_manager()
    print(colored("✅ FormsManager initialized successfully", "green"))
except Exception as e:
    print(colored(f"❌ Failed to initialize FormsManager: {str(e)}", "red"))
    st.error(f"Failed to initialize FormsManager: {str(e)}")
    st.stop()

try:
    database = get_database()
    print(colored("✅ Database initialized successfully", "green"))
except Exception as e:
    print(colored(f"❌ Failed to initialize Database: {str(e)}", "red"))
    st.error(f"Failed to initialize Database: {str(e)}")
    st.stop()

def render_header():
    """Render the application header with logo and title"""
    # Apply language-specific styles first
    st.markdown(apply_language_styles(st.session_state.language), unsafe_allow_html=True)
    
    # Custom CSS for header styling
    st.markdown(f"""
    <style>
    .main-header {{
        background: linear-gradient(135deg, #2E8B57 0%, #4682B4 100%);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin: 10px 0 20px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        direction: {get_language_direction(st.session_state.language)};
    }}
    
    .main-title {{
        color: white;
        font-size: 2.8em;
        font-weight: bold;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }}
    
    .main-subtitle {{
        color: #f0f8ff;
        font-size: 1.3em;
        margin: 10px 0 0 0;
        font-weight: 300;
    }}
    
    .language-selector {{
        position: absolute;
        top: 20px;
        right: 20px;
        z-index: 1000;
    }}
    
    .stSelectbox > div > div {{
        background-color: rgba(255,255,255,0.9);
        border-radius: 8px;
        border: 2px solid #4682B4;
    }}
    </style>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 4, 1])
    
    with col1:
        try:
            st.image("logo.jpg", width=120)
        except:
            st.markdown("🕌", unsafe_allow_html=True)
    
    with col2:
        content = content_manager.get_content("home", st.session_state.language)
        
        st.markdown(f"""
        <div class='main-header'>
            <h1 class='main-title'>{content["title"]}</h1>
            <p class='main-subtitle'>{content["subtitle"]}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        # Enhanced Language selector with better contrast and styling
        st.markdown("""
        <style>
        .language-container {
            background: rgba(255, 255, 255, 0.95);
            padding: 15px;
            border-radius: 12px;
            border: 2px solid #2E8B57;
            box-shadow: 0 3px 6px rgba(0,0,0,0.1);
        }
        
        .language-title {
            color: #2E8B57;
            font-weight: bold;
            font-size: 1.1em;
            margin-bottom: 10px;
            text-align: center;
        }
        
        .stSelectbox > div > div {
            background: linear-gradient(135deg, #ffffff, #f8f9fa) !important;
            border: 2px solid #2E8B57 !important;
            border-radius: 8px !important;
            font-weight: bold !important;
            color: #2E8B57 !important;
        }
        
        .stSelectbox > div > div:hover {
            border-color: #4682B4 !important;
            box-shadow: 0 2px 4px rgba(70, 130, 180, 0.3) !important;
        }
        
        .stSelectbox label {
            color: #2E8B57 !important;
            font-weight: bold !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="language-container">', unsafe_allow_html=True)
        st.markdown(f'<div class="language-title">{get_text("language", st.session_state.language)}</div>', unsafe_allow_html=True)
        
        lang_options = {
            'English': 'en', 
            'العربية': 'ar'
        }
        
        current_lang_label = 'English' if st.session_state.language == 'en' else 'العربية'
        
        selected_lang = st.selectbox(
            "🌐 Select Language",
            list(lang_options.keys()), 
            index=list(lang_options.keys()).index(current_lang_label),
            key="language_selector",
            help="Choose your preferred language / اختر لغتك المفضلة"
        )
        
        if lang_options[selected_lang] != st.session_state.language:
            st.session_state.language = lang_options[selected_lang]
            # Save language preference
            user_prefs.set_language(st.session_state.language)
            print(colored(f"🌐 Language changed to: {st.session_state.language}", "blue"))
            st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

def render_navigation():
    """Render the enhanced navigation menu with RTL support"""
    # Elegant spacing divider
    st.markdown("""
    <div style="height: 2px; background: linear-gradient(90deg, transparent, #e9ecef, transparent); margin: 15px 0; border-radius: 1px;"></div>
    """, unsafe_allow_html=True)
    
    # Language-aware text alignment
    text_align = "right" if st.session_state.language == 'ar' else "left"
    
    st.markdown(f"""
    <style>
    .nav-container {{
        background: linear-gradient(90deg, #f8f9fa, #e9ecef);
        padding: 15px;
        border-radius: 12px;
        margin: 20px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        direction: {get_language_direction(st.session_state.language)};
    }}
    
    .stButton > button {{
        width: 100%;
        height: 50px;
        background: linear-gradient(135deg, #28a745, #20c997) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        font-size: 14px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2) !important;
        text-align: center !important;
    }}
    
    .stButton > button:hover {{
        background: linear-gradient(135deg, #218838, #1e7e34) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3) !important;
    }}
    
    .stButton > button:focus {{
        background: linear-gradient(135deg, #1e7e34, #155724) !important;
        box-shadow: 0 0 0 3px rgba(40, 167, 69, 0.25) !important;
    }}
    </style>
    """, unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="nav-container">', unsafe_allow_html=True)
        
        # Create navigation buttons with translations
        cols = st.columns(9)
        
        nav_items = [
            ("home", "🏠", "home"),
            ("the_institute", "🏛️", "institute"), 
            ("all_activities", "📅", "activities"),
            ("members", "👥", "members"),
            ("projects", "🚀", "projects"),
            ("news", "📰", "news"),
            ("donations", "💰", "donations"),
            ("forms", "📝", "forms"),
            ("contact_us", "💡", "contact")
        ]
        
        # Reverse navigation order for Arabic (RTL)
        if st.session_state.language == 'ar':
            nav_items = nav_items[::-1]
        
        for i, (text_key, icon, page_key) in enumerate(nav_items):
            with cols[i]:
                button_text = f"{icon} {get_text(text_key, st.session_state.language)}"
                if st.button(button_text, key=f"nav_{page_key}"):
                    st.session_state.page = page_key
                    print(colored(f"🧭 Navigation: {page_key}", "yellow"))
                    st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Another elegant spacing divider
    st.markdown("""
    <div style="height: 2px; background: linear-gradient(90deg, transparent, #e9ecef, transparent); margin: 15px 0; border-radius: 1px;"></div>
    """, unsafe_allow_html=True)

def render_forms_page():
    """Render the forms page with proper navigation"""
    print(colored("📝 Rendering forms page...", "cyan"))
    
    # Initialize form selection in session state
    if 'selected_form' not in st.session_state:
        st.session_state.selected_form = None
    
    # Add back button if we're in a specific form
    if st.session_state.selected_form:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if st.button("← " + get_text('back_to_forms', st.session_state.language), key="back_to_forms"):
                # Clear form selection and go back to forms list
                st.session_state.selected_form = None
                print(colored("⬅️ Navigating back to forms list", "yellow"))
                st.rerun()
    
    # Forms title
    st.title(get_text('forms', st.session_state.language))
    
    if st.session_state.selected_form:
        if st.session_state.selected_form == 'membership':
            render_membership_form()
        elif st.session_state.selected_form == 'research':
            render_research_database_form()
        elif st.session_state.selected_form == 'nomination':
            render_nomination_form()
        elif st.session_state.selected_form == 'suggestions':
            render_suggestions_form()
        elif st.session_state.selected_form == 'bank_of_ideas':
            render_bank_of_ideas_form()
        else:
            render_form_selection()
    else:
        render_form_selection()

def render_form_selection():
    """Render the enhanced form selection interface"""
    # Elegant spacing divider
    st.markdown("""
    <div style="height: 2px; background: linear-gradient(90deg, transparent, #e9ecef, transparent); margin: 15px 0; border-radius: 1px;"></div>
    """, unsafe_allow_html=True)
    
    # Language-aware content container
    content_class = "arabic-content" if st.session_state.language == 'ar' else "english-content"
    
    st.markdown(f"""
    <div class="{content_class}">
        {get_text('select_form_message', st.session_state.language)}
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced form selection with better styling
    st.markdown("""
    <style>
    .form-card {
        background: linear-gradient(135deg, #ffffff, #f8f9fa);
        padding: 20px;
        border-radius: 12px;
        border: 2px solid #e9ecef;
        margin: 10px 0;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .form-card:hover {
        border-color: #4682B4;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        transform: translateY(-2px);
    }
    </style>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        st.subheader("📝 " + get_text('membership_application', st.session_state.language))
        st.markdown(get_text('membership_desc', st.session_state.language))
        if st.button(get_text('apply_now', st.session_state.language), key="membership_btn"):
            st.session_state.selected_form = "membership"
            print(colored("📝 Opening membership form", "green"))
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        st.subheader("🔬 " + get_text('researcher_profile', st.session_state.language))
        st.markdown(get_text('research_desc', st.session_state.language))
        if st.button(get_text('submit_research', st.session_state.language), key="research_btn"):
            st.session_state.selected_form = "research"
            print(colored("🔬 Opening research form", "green"))
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        st.subheader("👥 " + get_text('member_nomination', st.session_state.language))
        st.markdown(get_text('nomination_desc', st.session_state.language))
        if st.button(get_text('nominate_member', st.session_state.language), key="nomination_btn"):
            st.session_state.selected_form = "nomination"
            print(colored("👥 Opening nomination form", "green"))
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        st.subheader("💡 " + get_text('bank_of_ideas', st.session_state.language))
        st.markdown(get_text('suggestions_desc', st.session_state.language))
        if st.button(get_text('submit_idea', st.session_state.language), key="ideas_btn"):
            st.session_state.selected_form = "bank_of_ideas"
            print(colored("💡 Opening bank of ideas form", "green"))
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

def render_bank_of_ideas_form():
    """Render the bank of ideas form"""
    print(colored("💡 Rendering bank of ideas form...", "cyan"))
    
    content_class = "arabic-content" if st.session_state.language == 'ar' else "english-content"
    text_align = "right" if st.session_state.language == 'ar' else "left"
    
    st.markdown(f'<h2 style="text-align: {text_align};">{get_text("bank_of_ideas", st.session_state.language)}</h2>', unsafe_allow_html=True)
    st.markdown(f'<div class="{content_class}">{get_text("bank_of_ideas_desc", st.session_state.language)}</div>', unsafe_allow_html=True)
    
    with st.form("bank_of_ideas_form"):
        # Form fields
        email = st.text_input(get_text('email', st.session_state.language), placeholder="example@email.com")
        submitter_name = st.text_input(get_text('submitter_name', st.session_state.language))
        title_degrees = st.text_input(get_text('title_degrees', st.session_state.language))
        project_title = st.text_input(get_text('project_title', st.session_state.language))
        
        project_nature = st.selectbox(
            get_text('project_nature', st.session_state.language),
            [get_text('computing', st.session_state.language),
             get_text('religious', st.session_state.language),
             get_text('linguistic', st.session_state.language),
             get_text('other_specify', st.session_state.language)]
        )
        
        project_nature_other = st.text_input(get_text('project_nature_other', st.session_state.language))
        
        project_type = st.selectbox(
            get_text('project_type', st.session_state.language),
            [get_text('theoretical_research', st.session_state.language),
             get_text('applied_research', st.session_state.language),
             get_text('field_study', st.session_state.language),
             get_text('other_specify', st.session_state.language)]
        )
        
        project_type_other = st.text_input(get_text('project_type_other', st.session_state.language))
        brief_description = st.text_area(get_text('brief_description', st.session_state.language))
        specialization_area = st.text_input(get_text('specialization_area', st.session_state.language))
        objectives = st.text_area(get_text('objectives', st.session_state.language))
        benefits = st.text_area(get_text('benefits', st.session_state.language))
        web_links = st.text_area(get_text('web_links', st.session_state.language))
        additional_notes = st.text_area(get_text('additional_notes', st.session_state.language))
        
        submitted = st.form_submit_button(get_text('submit', st.session_state.language))
        
        if submitted:
            if email and submitter_name and project_title and brief_description:
                form_data = {
                    'email': email,
                    'submitter_name': submitter_name,
                    'title_degrees': title_degrees,
                    'project_title': project_title,
                    'project_nature': project_nature,
                    'project_nature_other': project_nature_other,
                    'project_type': project_type,
                    'project_type_other': project_type_other,
                    'brief_description': brief_description,
                    'specialization_area': specialization_area,
                    'objectives': objectives,
                    'benefits': benefits,
                    'web_links': web_links,
                    'additional_notes': additional_notes
                }
                
                try:
                    result = forms_manager.submit_bank_of_ideas(st.session_state.user_id, form_data)
                    if result['success']:
                        st.success("✅ " + get_text('form_submitted', st.session_state.language))
                        st.balloons()
                        print(colored("✅ Bank of ideas form submitted successfully", "green"))
                    else:
                        st.error(f"❌ {get_text('error', st.session_state.language)}: {result.get('error', 'Unknown error')}")
                        print(colored(f"❌ Error submitting bank of ideas: {result.get('error')}", "red"))
                except Exception as e:
                    st.error(f"❌ {get_text('error', st.session_state.language)}: {str(e)}")
                    print(colored(f"❌ Exception submitting bank of ideas: {str(e)}", "red"))
            else:
                st.error("❌ " + get_text('fill_required_fields', st.session_state.language))

def render_membership_form():
    """Render the membership application form"""
    print(colored("📝 Rendering membership form...", "cyan"))
    
    content_class = "arabic-content" if st.session_state.language == 'ar' else "english-content"
    text_align = "right" if st.session_state.language == 'ar' else "left"
    
    st.markdown(f'<h2 style="text-align: {text_align};">{get_text("membership_application", st.session_state.language)}</h2>', unsafe_allow_html=True)
    st.markdown(f'<div class="{content_class}">{get_text("membership_form_desc", st.session_state.language)}</div>', unsafe_allow_html=True)
    
    # Email input outside the form for real-time validation
    email = st.text_input(
        get_text('email', st.session_state.language), 
        placeholder="example@email.com", 
        help="Please include @ symbol",
        key="membership_email"
    )
    
    # Real-time email validation
    email_valid = True
    email_available = True
    if email:
        # Trim spaces and validate
        email_trimmed = email.strip()
        if not validate_email(email):
            email_valid = False
            if ' ' in email_trimmed:
                error_msg = "البريد الإلكتروني لا يجب أن يحتوي على مسافات" if st.session_state.language == 'ar' else "Email address cannot contain spaces"
            else:
                error_msg = "يرجى إدخال عنوان بريد إلكتروني صحيح يحتوي على @" if st.session_state.language == 'ar' else "Please enter a valid email address containing @"
            st.error(f"❌ {error_msg}")
        else:
            # Check if email already exists (using trimmed email)
            try:
                email_check = forms_manager.check_email_exists(email_trimmed, 'membership_applications')
                if email_check.get('exists'):
                    email_available = False
                    if st.session_state.language == 'ar':
                        error_msg = "معلومات العضوية للبريد الإلكتروني المستخدم تم إدخالها من قبل"
                    else:
                        error_msg = "Membership information for this email has already been submitted."
                    st.error(f"❌ {error_msg}")
                else:
                    st.success("✅ " + ("البريد الإلكتروني متاح" if st.session_state.language == 'ar' else "Email is available"))
            except Exception as e:
                st.warning("⚠️ " + ("تعذر التحقق من البريد الإلكتروني" if st.session_state.language == 'ar' else "Could not verify email"))
    
    with st.form("membership_form"):
        # Rest of form fields
        full_name = st.text_input(get_text('full_name', st.session_state.language))
        current_institution = st.text_input(get_text('current_institution', st.session_state.language))
        current_position = st.text_input(get_text('current_position', st.session_state.language))
        academic_degree = st.text_input(get_text('academic_degree', st.session_state.language))
        specialization = st.text_input(get_text('specialization', st.session_state.language))
        experience_years = st.number_input(get_text('years_experience', st.session_state.language), min_value=0, max_value=50, value=0)
        research_interests = st.text_area(get_text('research_interests', st.session_state.language))
        motivation = st.text_area(get_text('motivation', st.session_state.language))
        cv_link = st.text_input(get_text('cv_link', st.session_state.language))
        additional_info = st.text_area(get_text('additional_info', st.session_state.language))
        
        submitted = st.form_submit_button(get_text('submit_application', st.session_state.language))
        
        if submitted:
            if email and full_name and current_institution and email_valid and email_available:
                form_data = {
                    'email': email.strip(),
                    'full_name': full_name,
                    'current_institution': current_institution,
                    'current_position': current_position,
                    'academic_degree': academic_degree,
                    'specialization': specialization,
                    'experience_years': experience_years,
                    'research_interests': research_interests,
                    'motivation': motivation,
                    'cv_link': cv_link,
                    'additional_info': additional_info
                }
                
                try:
                    result = forms_manager.submit_membership_application(st.session_state.user_id, form_data)
                    if result['success']:
                        st.success("✅ " + get_text('application_submitted', st.session_state.language))
                        st.balloons()
                        print(colored("✅ Membership application submitted successfully", "green"))
                    else:
                        # Handle duplicate email error with appropriate language
                        if result.get('error') == 'duplicate_email':
                            if st.session_state.language == 'ar':
                                error_message = f"❌ {result.get('error_ar', 'معلومات العضوية للبريد الإلكتروني المستخدم تم إدخالها من قبل')}"
                            else:
                                error_message = f"❌ {result.get('error_en', 'Membership information for this email has already been submitted.')}"
                            st.error(error_message)
                            print(colored(f"❌ Duplicate email error: {email}", "red"))
                        else:
                            st.error(f"❌ {get_text('error', st.session_state.language)}: {result.get('error', 'Unknown error')}")
                            print(colored(f"❌ Error submitting membership: {result.get('error')}", "red"))
                except Exception as e:
                    st.error(f"❌ {get_text('error', st.session_state.language)}: {str(e)}")
                    print(colored(f"❌ Exception submitting membership: {str(e)}", "red"))
            else:
                if not email_valid:
                    error_msg = "يرجى إدخال عنوان بريد إلكتروني صحيح يحتوي على @" if st.session_state.language == 'ar' else "Please enter a valid email address containing @"
                    st.error(f"❌ {error_msg}")
                elif not email_available:
                    error_msg = "معلومات العضوية للبريد الإلكتروني المستخدم تم إدخالها من قبل" if st.session_state.language == 'ar' else "Membership information for this email has already been submitted."
                    st.error(f"❌ {error_msg}")
                else:
                    st.error("❌ " + get_text('fill_required_fields', st.session_state.language))

def render_research_database_form():
    """Render the research database form"""
    print(colored("🔬 Rendering research database form...", "cyan"))
    
    content_class = "arabic-content" if st.session_state.language == 'ar' else "english-content"
    text_align = "right" if st.session_state.language == 'ar' else "left"
    
    st.markdown(f'<h2 style="text-align: {text_align};">{get_text("researcher_profile", st.session_state.language)}</h2>', unsafe_allow_html=True)
    st.markdown(f'<div class="{content_class}">{get_text("research_form_desc", st.session_state.language)}</div>', unsafe_allow_html=True)
    
    with st.form("research_form"):
        title = st.text_input(get_text('research_title', st.session_state.language))
        authors = st.text_input(get_text('authors', st.session_state.language))
        publication_year = st.number_input(get_text('publication_year', st.session_state.language), min_value=1900, max_value=2030, value=2024)
        journal_conference = st.text_input(get_text('journal_conference', st.session_state.language))
        publisher = st.text_input(get_text('publisher', st.session_state.language))
        abstract = st.text_area(get_text('abstract', st.session_state.language))
        keywords = st.text_input(get_text('keywords', st.session_state.language))
        doi_link = st.text_input(get_text('doi_link', st.session_state.language))
        research_type = st.selectbox(get_text('research_type', st.session_state.language), 
                                   [get_text('journal_article', st.session_state.language),
                                    get_text('conference_paper', st.session_state.language),
                                    get_text('book', st.session_state.language),
                                    get_text('thesis', st.session_state.language),
                                    get_text('other', st.session_state.language)])
        field_of_study = st.text_input(get_text('field_of_study', st.session_state.language))
        language = st.selectbox(get_text('language', st.session_state.language), 
                              [get_text('english', st.session_state.language),
                               get_text('arabic', st.session_state.language),
                               get_text('other', st.session_state.language)])
        additional_notes = st.text_area(get_text('additional_notes', st.session_state.language))
        
        submitted = st.form_submit_button(get_text('submit_research', st.session_state.language))
        
        if submitted:
            if title and authors and abstract and publisher:
                form_data = {
                    'title': title,
                    'authors': authors,
                    'publication_year': publication_year,
                    'journal_conference': journal_conference,
                    'publisher': publisher,
                    'abstract': abstract,
                    'keywords': keywords,
                    'doi_link': doi_link,
                    'research_type': research_type,
                    'field_of_study': field_of_study,
                    'language': language,
                    'additional_notes': additional_notes
                }
                
                try:
                    result = forms_manager.submit_research_database(st.session_state.user_id, form_data)
                    if result['success']:
                        st.success("✅ " + get_text('form_submitted', st.session_state.language))
                        st.balloons()
                        print(colored("✅ Research form submitted successfully", "green"))
                    else:
                        st.error(f"❌ {get_text('error', st.session_state.language)}: {result.get('error', 'Unknown error')}")
                        print(colored(f"❌ Error submitting research: {result.get('error')}", "red"))
                except Exception as e:
                    st.error(f"❌ {get_text('error', st.session_state.language)}: {str(e)}")
                    print(colored(f"❌ Exception submitting research: {str(e)}", "red"))
            else:
                st.error("❌ " + get_text('fill_required_fields', st.session_state.language))

def render_nomination_form():
    """Render the nomination form"""
    print(colored("👥 Rendering nomination form...", "cyan"))
    
    content_class = "arabic-content" if st.session_state.language == 'ar' else "english-content"
    text_align = "right" if st.session_state.language == 'ar' else "left"
    
    st.markdown(f'<h2 style="text-align: {text_align};">{get_text("member_nomination", st.session_state.language)}</h2>', unsafe_allow_html=True)
    st.markdown(f'<div class="{content_class}">{get_text("nomination_form_desc", st.session_state.language)}</div>', unsafe_allow_html=True)
    
    with st.form("nomination_form"):
        # Nominee Information
        st.markdown("**Nominee Information**")
        nominee_full_name = st.text_input(get_text('nominee_name', st.session_state.language))
        nominee_email = st.text_input(get_text('nominee_email', st.session_state.language), help="Please include @ symbol")
        nominee_place_of_work = st.text_input(get_text('nominee_institution', st.session_state.language))
        nominee_specialization = st.text_input(get_text('nominee_position', st.session_state.language))
        nominee_country = st.text_input(get_text('country', st.session_state.language))
        nominee_phone = st.text_input(get_text('phone_number', st.session_state.language))
        nominee_address = st.text_area(get_text('address_optional', st.session_state.language))
        nominee_url_link = st.text_input(get_text('website_url_optional', st.session_state.language))
        nominee_qualifications = st.text_area(get_text('nominee_achievements', st.session_state.language))
        
        st.markdown("**Nominator Information**")
        nominating_member_name = st.text_input(get_text('nominator_name', st.session_state.language))
        nominator_email = st.text_input(get_text('nominator_email', st.session_state.language), help="Please include @ symbol")
        
        st.markdown("**Additional Information**")
        nomination_reason = st.text_area(get_text('nomination_reason', st.session_state.language))
        additional_comments = st.text_area(get_text('additional_comments', st.session_state.language))
        
        submitted = st.form_submit_button(get_text('submit_nomination', st.session_state.language))
        
        if submitted:
            if (nominee_full_name and nominee_email and nominee_place_of_work and nominee_specialization and 
                nominee_country and nominee_phone and nominee_qualifications and nominating_member_name and 
                nominator_email and nomination_reason and validate_email(nominee_email) and validate_email(nominator_email)):
                form_data = {
                    'nominee_full_name': nominee_full_name,
                    'nominee_email': nominee_email,
                    'nominee_place_of_work': nominee_place_of_work,
                    'nominee_specialization': nominee_specialization,
                    'nominee_country': nominee_country,
                    'nominee_phone': nominee_phone,
                    'nominee_address': nominee_address,
                    'nominee_url_link': nominee_url_link,
                    'nominee_qualifications': nominee_qualifications,
                    'nominating_member_name': nominating_member_name,
                    'nominator_email': nominator_email,
                    'nomination_reason': nomination_reason,
                    'additional_comments': additional_comments
                }
                
                try:
                    result = forms_manager.submit_member_nomination(st.session_state.user_id, form_data)
                    if result['success']:
                        st.success("✅ " + get_text('form_submitted', st.session_state.language))
                        st.balloons()
                        print(colored("✅ Nomination form submitted successfully", "green"))
                    else:
                        st.error(f"❌ {get_text('error', st.session_state.language)}: {result.get('error', 'Unknown error')}")
                        print(colored(f"❌ Error submitting nomination: {result.get('error')}", "red"))
                except Exception as e:
                    st.error(f"❌ {get_text('error', st.session_state.language)}: {str(e)}")
                    print(colored(f"❌ Exception submitting nomination: {str(e)}", "red"))
            else:
                if not validate_email(nominee_email) or not validate_email(nominator_email):
                    error_msg = "يرجى إدخال عناوين بريد إلكتروني صحيحة تحتوي على @" if st.session_state.language == 'ar' else "Please enter valid email addresses containing @"
                    st.error(f"❌ {error_msg}")
                else:
                    st.error("❌ " + get_text('fill_required_fields', st.session_state.language))

def render_suggestions_form():
    """Render the general suggestions form"""
    print(colored("💡 Rendering suggestions form...", "cyan"))
    
    content_class = "arabic-content" if st.session_state.language == 'ar' else "english-content"
    text_align = "right" if st.session_state.language == 'ar' else "left"
    
    st.markdown(f'<h2 style="text-align: {text_align};">{get_text("general_suggestions", st.session_state.language)}</h2>', unsafe_allow_html=True)
    st.markdown(f'<div class="{content_class}">{get_text("suggestions_form_desc", st.session_state.language)}</div>', unsafe_allow_html=True)
    
    with st.form("suggestions_form"):
        name = st.text_input(get_text('your_name', st.session_state.language))
        email = st.text_input(get_text('email', st.session_state.language), help="Please include @ symbol")
        subject = st.text_input(get_text('subject', st.session_state.language))
        category = st.selectbox(get_text('category', st.session_state.language), 
                              [get_text('general', st.session_state.language),
                               get_text('website', st.session_state.language),
                               get_text('research', st.session_state.language),
                               get_text('events', st.session_state.language),
                               get_text('membership', st.session_state.language),
                               get_text('other', st.session_state.language)])
        suggestion = st.text_area(get_text('suggestion_feedback', st.session_state.language))
        priority = st.selectbox(get_text('priority', st.session_state.language), 
                              [get_text('low', st.session_state.language),
                               get_text('medium', st.session_state.language),
                               get_text('high', st.session_state.language)])
        contact_back = st.checkbox(get_text('contact_back', st.session_state.language))
        additional_info = st.text_area(get_text('additional_info', st.session_state.language))
        
        submitted = st.form_submit_button(get_text('submit_suggestion', st.session_state.language))
        
        if submitted:
            if name and email and subject and suggestion and validate_email(email):
                form_data = {
                    'name': name,
                    'email': email,
                    'subject': subject,
                    'category': category,
                    'suggestion': suggestion,
                    'priority': priority,
                    'contact_back': contact_back,
                    'additional_info': additional_info
                }
                
                try:
                    result = forms_manager.submit_general_suggestion(st.session_state.user_id, form_data)
                    if result['success']:
                        st.success("✅ " + get_text('form_submitted', st.session_state.language))
                        st.balloons()
                        print(colored("✅ Suggestion form submitted successfully", "green"))
                    else:
                        st.error(f"❌ {get_text('error', st.session_state.language)}: {result.get('error', 'Unknown error')}")
                        print(colored(f"❌ Error submitting suggestion: {result.get('error')}", "red"))
                except Exception as e:
                    st.error(f"❌ {get_text('error', st.session_state.language)}: {str(e)}")
                    print(colored(f"❌ Exception submitting suggestion: {str(e)}", "red"))
            else:
                if not validate_email(email):
                    error_msg = "يرجى إدخال عنوان بريد إلكتروني صحيح يحتوي على @" if st.session_state.language == 'ar' else "Please enter a valid email address containing @"
                    st.error(f"❌ {error_msg}")
                else:
                    st.error("❌ " + get_text('fill_required_fields', st.session_state.language))

def render_home_page():
    """Render the home page"""
    content = content_manager.get_content("home", st.session_state.language)
    content_class = "arabic-content" if st.session_state.language == 'ar' else "english-content"
    text_align = "right" if st.session_state.language == 'ar' else "left"
    
    st.title(content["title"])
    
    # Mission section
    st.markdown(f'<h2 style="text-align: {text_align};">{get_text("mission", st.session_state.language)}</h2>', unsafe_allow_html=True)
    st.markdown(f'<div class="{content_class}">{content["mission"]}</div>', unsafe_allow_html=True)
    
    # Vision section  
    st.markdown(f'<h2 style="text-align: {text_align};">{get_text("vision", st.session_state.language)}</h2>', unsafe_allow_html=True)
    st.markdown(f'<div class="{content_class}">{content["vision"]}</div>', unsafe_allow_html=True)
    
    # Objectives section
    st.markdown(f'<h2 style="text-align: {text_align};">{get_text("objectives", st.session_state.language)}</h2>', unsafe_allow_html=True)
    for i, objective in enumerate(content["objectives"], 1):
        st.markdown(f'<div class="{content_class}"><strong>{i}.</strong> {objective}</div>', unsafe_allow_html=True)

def render_institute_page():
    """Render the institute page"""
    content = content_manager.get_content("institute", st.session_state.language)
    content_class = "arabic-content" if st.session_state.language == 'ar' else "english-content"
    text_align = "right" if st.session_state.language == 'ar' else "left"
    
    st.title(get_text('the_institute', st.session_state.language))
    
    # Mission
    st.markdown(f'<h2 style="text-align: {text_align};">{content["mission"]["title"]}</h2>', unsafe_allow_html=True)
    st.markdown(f'<div class="{content_class}">{content["mission"]["content"]}</div>', unsafe_allow_html=True)
    
    # Vision
    st.markdown(f'<h2 style="text-align: {text_align};">{content["vision"]["title"]}</h2>', unsafe_allow_html=True)
    st.markdown(f'<div class="{content_class}">{content["vision"]["content"]}</div>', unsafe_allow_html=True)
    
    # Board members
    st.markdown(f'<h2 style="text-align: {text_align};">{content["board"]["title"]}</h2>', unsafe_allow_html=True)
    for member in content["board"]["members"]:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(f'<div class="board-member-name">{member["name"]}</div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div class="board-member-position"><strong>{member["position"]}</strong></div>', unsafe_allow_html=True)
    
    # Official Documents
    if 'documents' in content:
        st.markdown(f'<h2 style="text-align: {text_align};">{content["documents"]["title"]}</h2>', unsafe_allow_html=True)
        
        # Bylaws Section
        st.markdown(f'<h3 style="text-align: {text_align};">{content["documents"]["bylaws_section"]["title"]}</h3>', unsafe_allow_html=True)
        for link in content["documents"]["bylaws_section"]["links"]:
            st.markdown(f'<div class="{content_class}">📄 <a href="{link["url"]}" target="_blank">{link["title"]}</a></div>', unsafe_allow_html=True)
        
        # Policies Section
        st.markdown(f'<h3 style="text-align: {text_align};">{content["documents"]["policies_section"]["title"]}</h3>', unsafe_allow_html=True)
        for link in content["documents"]["policies_section"]["links"]:
            st.markdown(f'<div class="{content_class}">📋 <a href="{link["url"]}" target="_blank">{link["title"]}</a></div>', unsafe_allow_html=True)
        
        # Profile Section
        st.markdown(f'<h3 style="text-align: {text_align};">{content["documents"]["profile_section"]["title"]}</h3>', unsafe_allow_html=True)
        for link in content["documents"]["profile_section"]["links"]:
            st.markdown(f'<div class="{content_class}">📖 <a href="{link["url"]}" target="_blank">{link["title"]}</a></div>', unsafe_allow_html=True)

def render_activities_page():
    """Render the activities page"""
    content = content_manager.get_content("activities", st.session_state.language)
    content_class = "arabic-content" if st.session_state.language == 'ar' else "english-content"
    text_align = "right" if st.session_state.language == 'ar' else "left"
    
    st.title(content["title"])
    
    for section in content["sections"]:
        st.markdown(f'<h2 style="text-align: {text_align};">{section["title"]}</h2>', unsafe_allow_html=True)
        st.markdown(f'<div class="{content_class}">{section["content"]}</div>', unsafe_allow_html=True)
        # Elegant spacing divider
        st.markdown("""
        <div style="height: 2px; background: linear-gradient(90deg, transparent, #e9ecef, transparent); margin: 15px 0; border-radius: 1px;"></div>
        """, unsafe_allow_html=True)

def render_members_page():
    """Render the members page"""
    content = content_manager.get_content("members", st.session_state.language)
    content_class = "arabic-content" if st.session_state.language == 'ar' else "english-content"
    
    st.title(content["title"])
    st.markdown(f'<div class="{content_class}">{content["content"]}</div>', unsafe_allow_html=True)

def render_projects_page():
    """Render the projects page"""
    content = content_manager.get_content("projects", st.session_state.language)
    content_class = "arabic-content" if st.session_state.language == 'ar' else "english-content"
    
    st.title(content["title"])
    st.markdown(f'<div class="{content_class}">{content["content"]}</div>', unsafe_allow_html=True)

def render_news_page():
    """Render the news page"""
    content = content_manager.get_content("news", st.session_state.language)
    content_class = "arabic-content" if st.session_state.language == 'ar' else "english-content"
    text_align = "right" if st.session_state.language == 'ar' else "left"
    
    st.title(content["title"])
    st.markdown(f'<div class="{content_class}">{content["content"]}</div>', unsafe_allow_html=True)
    
    # Add news links if available
    if 'links' in content:
        st.markdown(f'<h2 style="text-align: {text_align};">📰 أخبار وروابط / News & Links</h2>', unsafe_allow_html=True)
        
        # Separate social media links from document links
        document_links = []
        social_links = []
        
        for link in content["links"]:
            title = link["title"]
            if any(platform in title.lower() for platform in ['youtube', 'twitter', 'facebook', 'يوتيوب', 'تويتر', 'فيسبوك', 'إكس']):
                social_links.append(link)
            else:
                document_links.append(link)
        
        # Display document links first
        if document_links:
            st.markdown(f'<h3 style="text-align: {text_align};">📄 وثائق ومستندات / Documents</h3>', unsafe_allow_html=True)
            for link in document_links:
                st.markdown(f'<div class="{content_class}" style="margin: 10px 0; padding: 10px; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #28a745;">🔗 <a href="{link["url"]}" target="_blank" style="text-decoration: none; font-weight: bold;">{link["title"]}</a></div>', unsafe_allow_html=True)
        
        # Display social media links with special styling
        if social_links:
            st.markdown(f'<h3 style="text-align: {text_align};">🌐 وسائل التواصل الاجتماعي / Social Media</h3>', unsafe_allow_html=True)
            
            # Create columns for social media links
            cols = st.columns(len(social_links))
            for i, link in enumerate(social_links):
                with cols[i]:
                    # Style based on platform
                    if 'youtube' in link["title"].lower() or 'يوتيوب' in link["title"]:
                        bg_color = "#FF0000"
                        hover_color = "#CC0000"
                    elif 'twitter' in link["title"].lower() or 'تويتر' in link["title"] or 'إكس' in link["title"]:
                        bg_color = "#1DA1F2"
                        hover_color = "#0d8bd9"
                    elif 'facebook' in link["title"].lower() or 'فيسبوك' in link["title"]:
                        bg_color = "#1877F2"
                        hover_color = "#166fe5"
                    else:
                        bg_color = "#28a745"
                        hover_color = "#218838"
                    
                    # Display with logo if available
                    icon_html = ""
                    if 'icon' in link:
                        icon_html = f'<img src="{link["icon"]}" style="width: 24px; height: 24px; margin-right: 10px; vertical-align: middle;" alt="logo">'
                    
                    st.markdown(f'''
                    <div style="margin: 10px 0;">
                        <a href="{link["url"]}" target="_blank" style="text-decoration: none;">
                            <div style="
                                background: {bg_color}; 
                                color: white; 
                                padding: 15px; 
                                border-radius: 10px; 
                                text-align: center; 
                                font-weight: bold;
                                transition: all 0.3s ease;
                                box-shadow: 0 2px 4px rgba(0,0,0,0.2);
                                display: flex;
                                align-items: center;
                                justify-content: center;
                            " onmouseover="this.style.background='{hover_color}'; this.style.transform='translateY(-2px)'" 
                               onmouseout="this.style.background='{bg_color}'; this.style.transform='translateY(0px)'">
                                {icon_html}{link["title"]}
                            </div>
                        </a>
                    </div>
                    ''', unsafe_allow_html=True)

def render_contact_page():
    """Render the contact page"""
    content = content_manager.get_content("contact", st.session_state.language)
    content_class = "arabic-content" if st.session_state.language == 'ar' else "english-content"
    text_align = "right" if st.session_state.language == 'ar' else "left"
    
    st.title(content["title"])
    st.markdown(f'<div class="{content_class}">{content["content"]}</div>', unsafe_allow_html=True)
    
    if "email" in content:
        st.markdown(f'<div class="contact-email"><strong>{get_text("email", st.session_state.language)}:</strong> {content["email"]}</div>', unsafe_allow_html=True)
    
    # Contact form
    st.markdown(f'<h2 style="text-align: {text_align};">✉️ Send us a message / راسلنا</h2>', unsafe_allow_html=True)
    
    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input(get_text('your_name', st.session_state.language), key="contact_name")
            email = st.text_input(get_text('email_address', st.session_state.language), key="contact_email")
        
        with col2:
            subject = st.text_input(get_text('subject', st.session_state.language), key="contact_subject")
            phone = st.text_input(get_text('phone_number', st.session_state.language), key="contact_phone")
        
        message = st.text_area(get_text('message', st.session_state.language), key="contact_message", height=150)
        
        submitted = st.form_submit_button(get_text('send_message', st.session_state.language))
        
        if submitted:
            if name and email and subject and message:
                if validate_email(email):
                    # Here you would normally send the email
                    # For now, we'll just show a success message
                    st.success("✅ " + ("تم إرسال رسالتك بنجاح!" if st.session_state.language == 'ar' else "Your message has been sent successfully!"))
                    st.info("📧 " + ("سيتم الرد عليك في أقرب وقت ممكن على البريد الإلكتروني: info@qurancomputing.org" if st.session_state.language == 'ar' else "You will receive a response at: info@qurancomputing.org"))
                else:
                    error_msg = "يرجى إدخال عنوان بريد إلكتروني صحيح" if st.session_state.language == 'ar' else "Please enter a valid email address"
                    st.error(f"❌ {error_msg}")
            else:
                error_msg = "يرجى ملء جميع الحقول المطلوبة" if st.session_state.language == 'ar' else "Please fill all required fields"
                st.error(f"❌ {error_msg}")

def render_donations_page():
    """Render the donations page"""
    content = content_manager.get_content("donations", st.session_state.language)
    content_class = "arabic-content" if st.session_state.language == 'ar' else "english-content"
    text_align = "right" if st.session_state.language == 'ar' else "left"
    
    st.title(content["title"])
    st.markdown(f'<div class="{content_class}">{content["content"]}</div>', unsafe_allow_html=True)
    
    # Add donation links
    st.markdown(f'<h2 style="text-align: {text_align};">💳 طرق التبرع / Donation Methods</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4CAF50, #45a049); padding: 20px; border-radius: 10px; margin: 10px 0; text-align: center;">
            <h3 style="color: white; margin: 0;">💳 Visa / MasterCard</h3>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <a href="https://donate.stripe.com/dR616G9Uk7C78WA5kk" target="_blank" style="text-decoration: none;">
            <button style="
                width: 100%;
                background: linear-gradient(135deg, #4CAF50, #45a049);
                color: white;
                padding: 15px;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
                transition: all 0.3s ease;
                box-shadow: 0 2px 4px rgba(0,0,0,0.2);
            " onmouseover="this.style.background='linear-gradient(135deg, #45a049, #3d8b40)'"
               onmouseout="this.style.background='linear-gradient(135deg, #4CAF50, #45a049)'">
                💳 Donate with Visa/MasterCard
            </button>
        </a>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #2196F3, #1976D2); padding: 20px; border-radius: 10px; margin: 10px 0; text-align: center;">
            <h3 style="color: white; margin: 0;">💰 PayPal</h3>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <a href="https://www.paypal.me/qurancomputing" target="_blank" style="text-decoration: none;">
            <button style="
                width: 100%;
                background: linear-gradient(135deg, #2196F3, #1976D2);
                color: white;
                padding: 15px;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
                transition: all 0.3s ease;
                box-shadow: 0 2px 4px rgba(0,0,0,0.2);
            " onmouseover="this.style.background='linear-gradient(135deg, #1976D2, #1565C0)'"
               onmouseout="this.style.background='linear-gradient(135deg, #2196F3, #1976D2)'">
                💰 Donate with PayPal
            </button>
        </a>
        """, unsafe_allow_html=True)
    
    # Direct links as backup
    st.markdown(f'<h3 style="text-align: {text_align};">🔗 روابط مباشرة / Direct Links</h3>', unsafe_allow_html=True)
    for link in content["donation_links"]:
        st.markdown(f'<div class="{content_class}">💰 <a href="{link["url"]}" target="_blank">{link["title"]}</a></div>', unsafe_allow_html=True)
    
def main():
    """Main application function"""
    print(colored("🚀 Starting main application...", "cyan"))
    
    render_header()
    render_navigation()
    
    # Initialize page in session state if not set
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    
    # Route to appropriate page
    current_page = st.session_state.get('page', 'home')
    print(colored(f"📄 Rendering page: {current_page}", "blue"))
    
    if current_page == "home":
        render_home_page()
    elif current_page == "institute":
        render_institute_page()
    elif current_page == "activities":
        render_activities_page()
    elif current_page == "members":
        render_members_page()
    elif current_page == "projects":
        render_projects_page()
    elif current_page == "news":
        render_news_page()
    elif current_page == "donations":
        render_donations_page()
    elif current_page == "forms":
        render_forms_page()
    elif current_page == "contact":
        render_contact_page()
    else:
        render_home_page()
    
    # Footer with elegant spacing and proper Arabic text
    st.markdown("""
    <div style="height: 2px; background: linear-gradient(90deg, transparent, #e9ecef, transparent); margin: 30px 0 20px 0; border-radius: 1px;"></div>
    """, unsafe_allow_html=True)
    
    if st.session_state.language == 'ar':
        footer_text = "© 2025 المعهد العالمي لحوسبة القرآن والعلوم الإسلامية. جميع الحقوق محفوظة."
    else:
        footer_text = "© 2025 International Computing Institute for Quran and Islamic Sciences. All rights reserved."
    
    st.markdown(f"""
    <div class="app-footer">
        {footer_text}
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

