# Quran Institute Streamlit Application - Deployment Instructions

## Installation and Setup

### 1. Install Python Dependencies
```bash
pip install -r quran_institute_requirements.txt
```

### 2. Required Files Structure
```
quran_institute_app/
├── src/
│   ├── main_fixed_v5.py          # Main Streamlit application
│   ├── content_manager_v1.py     # Content management
│   ├── forms_manager_clean_v1.py # Forms handling
│   ├── database_v1.py            # Database operations
│   ├── auth.py                   # Authentication
│   └── ui_utils.py               # UI utilities
├── logo.jpg                      # Institute logo
├── quran_institute.db           # SQLite database (auto-created)
└── requirements.txt             # Dependencies
```

## Running the Application

### Command to Run the Streamlit Application:
```bash
cd /path/to/quran_institute_app
python -m streamlit run src/main_fixed_v5.py --server.port 8502 --server.address 0.0.0.0
```

### Alternative Command (if in src directory):
```bash
cd /path/to/quran_institute_app/src
streamlit run main_fixed_v5.py --server.port 8502 --server.address 0.0.0.0
```

### For Local Development:
```bash
cd /path/to/quran_institute_app
streamlit run src/main_fixed_v5.py
```

## Application Features
- ✅ Bilingual support (English/Arabic)
- ✅ Complete forms functionality (4 forms)
- ✅ Database integration with SQLite
- ✅ User authentication system
- ✅ Professional UI with institute branding
- ✅ Responsive design

## Database
- SQLite database is automatically created on first run
- Database file: `quran_institute.db`
- Contains tables for: users, membership_applications, bank_of_ideas, member_nominations, research_database, general_suggestions

## Port Configuration
- Default port: 8502
- Can be changed using --server.port parameter
- For external access, use --server.address 0.0.0.0

