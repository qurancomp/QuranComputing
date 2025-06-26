# Quran Institute Streamlit Application

## Overview
This is the complete deployment package for the International Computing Institute for Quran and Islamic Sciences Streamlit application.

## Package Contents
- `src/main.py` - Main Streamlit application (latest fixed version)
- `src/content_manager.py` - Content management system
- `src/forms_manager.py` - Forms handling with database integration
- `src/database.py` - Database operations and schema
- `src/auth.py` - Authentication utilities
- `src/ui_utils.py` - UI utility functions
- `logo.jpg` - Institute logo
- `quran_institute.db` - SQLite database with sample data
- `requirements.txt` - Python dependencies
- `DEPLOYMENT_INSTRUCTIONS.md` - Detailed setup instructions

## Quick Start

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application:**
   ```bash
   streamlit run src/main.py --server.port 8502 --server.address 0.0.0.0
   ```

3. **Access the Application:**
   Open your browser to `http://localhost:8502`

## Features
- ✅ Bilingual support (English/Arabic)
- ✅ 4 Working forms with database integration:
  - Membership Application
  - Research Database Submission
  - Member Nomination
  - General Suggestions
- ✅ Professional UI with institute branding
- ✅ SQLite database backend
- ✅ Form validation and error handling
- ✅ Responsive design

## Database
The included `quran_institute.db` file contains the complete database schema and sample data. The application will automatically use this database.

## Support
For detailed deployment instructions, see `DEPLOYMENT_INSTRUCTIONS.md`

## Version
This package contains the latest working version (v5) with all forms functionality fixed and tested.

