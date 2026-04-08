# Placement Management System - Setup Guide

## Quick Start (5 minutes)

### Step 1: Open Terminal in Project Directory
Navigate to your project folder:
```bash
cd C:\Users\chand\OneDrive\Desktop\Project1
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

After activation, your terminal prompt should show `(venv)` prefix.

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- Flask: Web framework
- Flask-SQLAlchemy: ORM for database
- Flask-Login: User authentication
- Werkzeug: Security utilities

### Step 4: Initialize Database
```bash
python init_db.py
```

This creates the database and populates it with:
- 1 Admin user
- 5 Sample Companies
- 3 Sample Students

### Step 5: Run Application
```bash
python run.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

Open your browser and go to: **http://localhost:5000**

---

## Login Credentials

### Admin Login
- **URL**: http://localhost:5000/auth/admin-login
- **Username**: admin
- **Password**: admin123

### Student Login (Sample)
- **URL**: http://localhost:5000/auth/student-login
- **USN**: USN001
- **Email**: raj@example.com
- **Password**: password123

### Register New Student
- **URL**: http://localhost:5000/auth/student-register
- Fill in all required fields

---

## File Structure Explanation

```
Project1/
│
├── app/                              # Main application package
│   ├── __init__.py                  # Flask app factory & extensions
│   ├── models.py                    # Database models (Student, Admin, etc.)
│   ├── auth.py                      # Authentication routes
│   ├── student.py                   # Student feature routes
│   ├── admin.py                     # Admin feature routes
│   ├── routes.py                    # Main/home routes
│   │
│   ├── templates/                   # HTML templates
│   │   ├── base.html               # Base template (navbar, footer)
│   │   ├── index.html              # Home page
│   │   │
│   │   ├── auth/
│   │   │   ├── student_login.html     # Student login page
│   │   │   ├── student_register.html  # Student registration page
│   │   │   └── admin_login.html       # Admin login page
│   │   │
│   │   ├── student/
│   │   │   ├── dashboard.html       # Student dashboard
│   │   │   ├── view_companies.html  # Browse companies
│   │   │   ├── applications.html    # Track applications
│   │   │   └── profile.html         # Student profile
│   │   │
│   │   └── admin/
│   │       ├── dashboard.html       # Admin dashboard
│   │       ├── add_company.html     # Add new company
│   │       ├── view_companies.html  # List companies
│   │       ├── view_students.html   # List students
│   │       ├── view_applications.html # Review applications
│   │       └── student_detail.html  # Student details & apps
│   │
│   └── static/                      # Static files
│       ├── css/
│       │   └── style.css           # Custom Bootstrap styles
│       └── js/                      # JavaScript files (optional)
│
├── config.py                        # Configuration settings
├── run.py                           # Application entry point
├── init_db.py                       # Database initialization script
├── requirements.txt                 # Python dependencies
├── README.md                        # Project overview
├── SETUP.md                         # This file
└── .gitignore                       # Git ignore file
```

---

## Development Workflow

### 1. Always Activate Virtual Environment
Before working, activate the virtual environment:
```bash
venv\Scripts\activate
```

### 2. Run the Application
```bash
python run.py
```

### 3. Make Changes
Edit Python files or HTML templates as needed.

### 4. Restart Application
Press `Ctrl + C` to stop the server, then run `python run.py` again.

### 5. Database Changes
If you modify models, run:
```bash
python
>>> from app import create_app
>>> app = create_app()
>>> from flask import Flask
>>> with app.app_context():
>>>     from app import db
>>>     db.create_all()
```

Or delete `placement.db` and restart (database will be recreated).

---

## Troubleshooting

### Issue: Module not found error
**Solution**: Ensure virtual environment is activated:
```bash
venv\Scripts\activate
pip install -r requirements.txt
```

### Issue: Port 5000 already in use
**Solution**: Use a different port:
```bash
python run.py --port 5001
```
Or change in `run.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, port=5001)
```

### Issue: Database locked error
**Solution**: Delete the database and restart:
```bash
# Delete placement.db file, then restart
python run.py
```

### Issue: Login not working
**Solution**: 
1. Verify database is initialized: Check if `placement.db` exists
2. Re-initialize database: `python init_db.py`
3. Check credentials match exactly

### Issue: "No module named 'app'"
**Solution**: Ensure you're in the correct directory:
```bash
cd C:\Users\chand\OneDrive\Desktop\Project1
```

---

## Features Overview

### ✅ Student Features
- ✅ Register with email, USN, branch, CGPA, skills
- ✅ Login with email or USN
- ✅ View eligible companies (based on CGPA, branch)
- ✅ Apply for companies
- ✅ Track application status
- ✅ View profile

### ✅ Admin Features
- ✅ Login
- ✅ Add new companies
- ✅ View all students
- ✅ Review applications
- ✅ Update application status
- ✅ View student details

### ✅ System Features
- ✅ Eligibility checking (CGPA, Branch, Skills)
- ✅ Application deadline tracking
- ✅ Status workflow (Applied → Shortlisted → Selected/Rejected)
- ✅ Dashboard with statistics
- ✅ Responsive design (Bootstrap 5)
- ✅ Secure password hashing

---

## Next Steps / Enhancements

After getting the basic system working, you can add:

1. **Search & Filter**
   - Search companies by name/role
   - Filter by package, branch
   - Search students

2. **Resume Upload**
   - Allow students to upload PDF/DOC
   - Store in file system or database

3. **Notifications**
   - Email notifications on status change
   - SMS alerts

4. **Reports**
   - Placement statistics
   - Export to CSV/PDF

5. **Scheduling**
   - Interview scheduling system
   - Calendar integration

6. **Analytics**
   - Placement statistics
   - Company performance metrics
   - Student success rates

---

## Database Schema

### Students Table
```
id (Primary Key)
usn (Unique)
name
email (Unique)
phone
branch
semester
cgpa
skills
password_hash
created_at
```

### Companies Table
```
id (Primary Key)
name
role
package
min_cgpa
eligible_branches
required_skills
application_deadline
created_at
```

### Applications Table
```
id (Primary Key)
student_id (Foreign Key)
company_id (Foreign Key)
status (Applied, Shortlisted, Rejected, Selected)
applied_at
updated_at
```

### Admins Table
```
id (Primary Key)
username (Unique)
email (Unique)
password_hash
created_at
```

---

## API Endpoints Quick Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Home page |
| GET/POST | /auth/student-register | Register student |
| GET/POST | /auth/student-login | Student login |
| GET/POST | /auth/admin-login | Admin login |
| GET | /auth/logout | Logout |
| GET | /student/dashboard | Student dashboard |
| GET | /student/view-companies | Browse companies |
| POST | /student/apply/<id> | Apply for company |
| GET | /student/applications | View applications |
| GET | /student/profile | View profile |
| GET | /admin/dashboard | Admin dashboard |
| GET/POST | /admin/add-company | Add company |
| GET | /admin/companies | View companies |
| GET | /admin/students | View students |
| GET | /admin/applications | View applications |
| POST | /admin/update-status/<id> | Update status |

---

## Support & Tips

### VS Code Integration
1. Install Python extension
2. Select Python interpreter from `venv\Scripts\python.exe`
3. Use Debug mode to set breakpoints

### Flask Shell (Advanced)
```bash
# Activate virtual environment first
flask shell
>>> from app.models import Student
>>> students = Student.query.all()
>>> print(students[0].name)
```

### Test the Application
Test each feature:
1. Register a new student
2. Login as student
3. View companies
4. Apply for a company
5. Login as admin
6. Add a new company
7. Update application status
8. View student details

---

## Enjoy Building! 🚀

You've successfully set up a production-like placement management system. Continue building features and have fun coding!

For questions or issues, refer to the code comments and the README.md file.
