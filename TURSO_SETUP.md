# Turso Cloud SQLite Setup

## What is Turso?
Turso provides **distributed SQLite** in the cloud with direct HTTP API access. Perfect for keeping your SQLite format while getting cloud benefits.

## Benefits:
- ✅ **Keep SQLite format** - no schema migration needed
- ✅ **Direct HTTP API** - no file downloads/uploads
- ✅ **Edge replication** - faster global access
- ✅ **Free tier** - generous limits for small apps
- ✅ **Real-time sync** - instant data persistence
- ✅ **Same SQL syntax** - no code changes needed

## Setup Steps:

### 1. Create Turso Account
```bash
# Install Turso CLI
curl -sSfL https://get.tur.so/install.sh | bash

# Login to Turso
turso auth login

# Create database
turso db create quran-institute

# Get database URL (HTTP API URL, not the connection URL)
turso db show quran-institute --url
# This gives you the libSQL URL like: libsql://quran-institute-qurancomputing.aws-us-east-1.turso.io

# For HTTP API, you need the HTTP URL:
turso db show quran-institute --http-url
# This should give you something like: https://quran-institute-qurancomputing.aws-us-east-1.turso.io

# Create auth token
turso db tokens create quran-institute
```

turso db export quran-institute --output-file quran_institute.db --with-metadata --overwrite 
OR
turso db shell quran-institute .dump > dump.sql
sqlite3 quran_institute.db < dump.sql

## Via web browser
https://app.turso.tech/qurancomputing/settings


### 2. Add to Streamlit Secrets
In your Streamlit Cloud app settings, add to `secrets.toml`:

```toml
[turso]
database_url = "libsql://quran-institute-qurancomputing.aws-us-east-1.turso.io"
auth_token = "your-auth-token-here"
```

**Note**: You can use either the `libsql://` URL (which gets automatically converted to `https://`) or directly use the `https://` URL format.

### 3. Migrate Your Existing Data (Optional)
If you have existing SQLite data:

```bash
# Export your current database
sqlite3 quran_institute.db .dump > data.sql

# Import to Turso
turso db shell quran-institute < data.sql
```

----------------------

 https://quran-institute-qurancomputing.aws-us-east-1.turso.io
------------------------

turso db export quran-institute --output-file quran_institute.db --with-metadata --overwrite 
OR
turso db shell quran-institute .dump > dump.sql
sqlite3 quran_institute.db < dump.sql


### 4. Update Your Application
Simply change the import in `src/main.py`:

```python
# Change this:
from database import Database
from forms_manager import FormsManager

# To this:
from database_turso import Database
from forms_manager_turso import FormsManager
```

## How It Works:

### Direct Cloud Operations:
```python
# Before (file-based):
conn = sqlite3.connect("local_file.db")
# Download, operate, upload cycle

# After (cloud-native):
result = db.execute_sql("INSERT INTO users (...)", [params])
# Direct cloud operation, immediate persistence
```

### Real-time Benefits:
1. **No File Management**: No temp files, downloads, or uploads
2. **Instant Persistence**: Every write immediately saved to cloud
3. **Global Access**: Edge replication for faster access worldwide
4. **Automatic Backups**: Built-in backup and point-in-time recovery
5. **Scalability**: Handles multiple concurrent users seamlessly

### Migration Checklist:
- [ ] Create Turso account and database
- [ ] Add credentials to Streamlit secrets
- [ ] Update imports in main.py
- [ ] Test form submissions
- [ ] Migrate existing data (if any)
- [ ] Deploy updated application

## Cost:
- **Free Tier**: 8 GB storage, 1 billion row reads/month
- **Perfect for** small to medium applications
- **Much cheaper** than file storage + bandwidth costs

## Support:
- **Same SQLite syntax** - all your existing queries work
- **Foreign keys supported** - full relational database features
- **Transactions** - ACID compliance maintained
- **Indexes** - same performance optimizations

Ready to migrate? The new files are ready to use! 