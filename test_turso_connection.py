#!/usr/bin/env python3
"""
Simple Turso Connection Test Script
Run this to verify your Turso database URL and auth token
"""

import requests
import json
import os

# Get credentials from environment variables
# For libSQL URL, convert to HTTPS for HTTP API
LIBSQL_URL = os.getenv("DATABASE_URL", "libsql://quran-institute-qurancomputing.aws-us-east-1.turso.io")
DATABASE_URL = LIBSQL_URL.replace("libsql://", "https://")  # Convert libSQL to HTTPS
TURSO_AUTH_TOKEN = os.getenv("TURSO_AUTH_TOKEN", "")

def test_turso_connection():
    """Test connection to Turso database"""
    
    headers = {
        "Authorization": f"Bearer {TURSO_AUTH_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # Simple test query
    payload = {
        "statements": [
            {
                "q": "SELECT 1 as test",
                "params": []
            }
        ]
    }
    
    print(f"🔍 Testing connection to: {DATABASE_URL}")
    print(f"🔑 Using token: {TURSO_AUTH_TOKEN[:10]}...{TURSO_AUTH_TOKEN[-10:] if len(TURSO_AUTH_TOKEN) > 20 else '[short]'}")
    
    try:
        response = requests.post(
            DATABASE_URL,
            headers=headers,
            json=payload,
            timeout=10
        )
        
        print(f"📊 Response Status: {response.status_code}")
        print(f"📊 Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            print("✅ SUCCESS! Connection works!")
            result = response.json()
            print(f"Result: {json.dumps(result, indent=2)}")
        else:
            print(f"❌ FAILED with status {response.status_code}")
            print(f"Error response: {response.text}")
            
            # Try to get JSON error details
            try:
                error_data = response.json()
                print(f"Error details: {json.dumps(error_data, indent=2)}")
            except:
                print("Could not parse error as JSON")
                
    except Exception as e:
        print(f"❌ Exception occurred: {e}")
        print(f"Exception type: {type(e).__name__}")

if __name__ == "__main__":
    print("🧪 Turso Connection Test")
    print("=" * 40)
    
    if not TURSO_AUTH_TOKEN:
        print("⚠️ WARNING: TURSO_AUTH_TOKEN environment variable not set!")
        print()
        print("Set your environment variables:")
        print("export TURSO_AUTH_TOKEN='your_actual_token'")
        print("export DATABASE_URL='libsql://your-database-url.turso.io'  # Optional, has default")
        print()
        print("Or create a .env file with:")
        print("TURSO_AUTH_TOKEN=your_actual_token")
        print("DATABASE_URL=libsql://quran-institute-qurancomputing.aws-us-east-1.turso.io")
    else:
        print(f"📊 Using libSQL URL: {LIBSQL_URL}")
        print(f"📊 Converted to HTTP URL: {DATABASE_URL}")
        print()
        test_turso_connection() 