import streamlit as st
from typing import Optional, Dict, Any
from src.database import Database
from src.email_service import EmailService
import re

class AuthManager:
    def __init__(self, db: Database):
        self.db = db
        self.email_service = EmailService()
    
    def register(self, email: str, password: str, first_name: str, last_name: str) -> Dict[str, Any]:
        """Register a new user"""
        return self.db.create_user(email, password, first_name, last_name)
    
    def login(self, email: str, password: str) -> Dict[str, Any]:
        """Login user"""
        return self.db.verify_user(email, password)
    
    def get_user(self, user_id: int) -> Dict[str, Any]:
        """Get user by ID"""
        return self.db.get_user_by_id(user_id)
    
    def init_session_state(self):
        """Initialize session state variables"""
        if 'user_id' not in st.session_state:
            st.session_state.user_id = None
        if 'user_email' not in st.session_state:
            st.session_state.user_email = None
        if 'is_authenticated' not in st.session_state:
            st.session_state.is_authenticated = False
    
    def logout(self):
        """Logout user"""
        st.session_state.user_id = None
        st.session_state.user_email = None
        st.session_state.is_authenticated = False
    
    def is_authenticated(self) -> bool:
        """Check if user is authenticated"""
        return st.session_state.get('is_authenticated', False)
    
    def get_current_user_id(self) -> Optional[int]:
        """Get current user ID"""
        return st.session_state.get('user_id')
    
    def get_current_user_email(self) -> Optional[str]:
        """Get current user email"""
        return st.session_state.get('user_email')

