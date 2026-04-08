# Placement Management System

A comprehensive web-based system for managing campus placements built with Flask, SQLAlchemy, and Bootstrap.

## Features

### Core Features (✅ Implemented)
- ✅ Student Registration & Login
- ✅ Admin Login & Management
- ✅ Company Management (Add, View)
- ✅ Eligibility Check System
- ✅ Job Applications
- ✅ Application Status Tracking
- ✅ Student Dashboard & Analytics
- ✅ Admin Dashboard & Analytics

### Optional Features (Can be added)
- 📋 Search functionality for students and companies
- 📊 Dashboard statistics and reports
- 📄 Resume upload system
- 📥 Export to CSV functionality
- 🔍 Advanced filtering options

## Project Structure

```
Project1/
├── app/
│   ├── __init__.py              # Flask app factory
│   ├── models.py                # Database models
│   ├── auth.py                  # Authentication routes
│   ├── student.py               # Student module routes
│   ├── admin.py                 # Admin module routes
│   ├── routes.py                # Main routes
│   ├── templates/               # HTML templates
│   │   ├── base.html           # Base template
│   │   ├── index.html          # Home page
│   │   ├── auth/               # Auth templates
│   │   ├── student/            # Student templates
│   │   └── admin/              # Admin templates
│   └── static/                  # Static files
│       ├── css/
│       │   └── style.css       # Custom styles
│       └── js/                  # JavaScript files
├── config.py                    # Configuration
├── run.py                       # Application entry point
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Tech Stack

- **Backend**: Python 3.x with Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Authentication**: Flask-Login
- **Security**: Werkzeug for password hashing

## Installation & Setup

### 1. Prerequisites
- Python 3.7+
- pip (Python package manager)

### 2. Clone/Setup the Project
```bash
cd Project1
```

### 3. Create Virtual Environment (Optional but Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Application
```bash
python run.py
```

The application will start on `http://localhost:5000`

## Default Admin Login

**Note**: You'll need to create an admin account in the database before accessing admin features.

To create an admin programmatically, open Python shell:
```bash
python
>>> from app import create_app, db
>>> from app.models import Admin
>>> app = create_app()
>>> with app.app_context():
>>>     admin = Admin(username='admin', email='admin@example.com')
>>>     admin.set_password('password123')
>>>     db.session.add(admin)
>>>     db.session.commit()
>>> exit()
```

Then login with:
- **Username**: admin
- **Password**: password123

## User Flows

### Student Flow
1. Register with details (Name, USN, Email, Branch, Semester, CGPA, Skills)
2. Login with Email or USN
3. View eligible companies (based on CGPA & Branch)
4. Apply for companies
5. Track application status

### Admin Flow
1. Login with credentials
2. Add company details
3. View all students
4. Review applications
5. Update application status (Applied → Shortlisted → Selected/Rejected)

## Database Models

### Student
- USN, Name, Email, Phone
- Branch, Semester, CGPA
- Skills, Password

### Admin
- Username, Email, Password

### Company
- Name, Role, Package
- Minimum CGPA, Eligible Branches
- Required Skills, Application Deadline

### Application
- Student ID, Company ID
- Status (Applied, Shortlisted, Rejected, Selected)
- Applied Date, Updated Date

## Eligibility Criteria

A student is eligible for a company if:
1. CGPA >= Company's Minimum CGPA
2. Branch is in Eligible Branches list
3. Application deadline hasn't passed
4. (Optional) Has at least one of the required skills

## API Routes

### Authentication
- `GET/POST /auth/student-register` - Student registration
- `GET/POST /auth/student-login` - Student login
- `GET/POST /auth/admin-login` - Admin login
- `GET /auth/logout` - Logout

### Student Routes
- `GET /student/dashboard` - Student dashboard
- `GET /student/view-companies` - View eligible companies
- `POST /student/apply/<company_id>` - Apply for company
- `GET /student/applications` - View applications
- `GET /student/profile` - View profile

### Admin Routes
- `GET /admin/dashboard` - Admin dashboard
- `GET/POST /admin/add-company` - Add company
- `GET /admin/companies` - View companies
- `GET /admin/students` - View students
- `GET /admin/applications` - View applications
- `POST /admin/update-status/<app_id>` - Update application status
- `GET /admin/student/<student_id>` - View student details

## Future Enhancements

1. **Resume Upload**: Allow students to upload resumes
2. **Search & Filter**: Advanced search for companies and students
3. **Notifications**: Email/SMS notifications for status changes
4. **Reports**: Generate placement reports and analytics
5. **Interview Scheduling**: Schedule and manage interviews
6. **Feedback System**: Collect feedback from students and companies
7. **Multi-round Applications**: Support for multiple interview rounds
8. **Mobile App**: React Native or Flutter mobile application

## Troubleshooting

### Database Issues
If you encounter database errors, delete `placement.db` and restart the app.

### Port Already in Use
If port 5000 is in use:
```bash
python run.py --port 5001
```

### Module Import Errors
Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

## License

This project is created for educational purposes.

## Support

For issues or questions, please refer to the code comments or create an issue.

---

**Happy Coding!** 🚀
