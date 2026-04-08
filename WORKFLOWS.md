# Placement Management System - User Workflows

## 📊 System Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│          PLACEMENT MANAGEMENT SYSTEM                     │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  ┌──────────────┐         ┌──────────────┐              │
│  │   Students   │         │    Admins    │              │
│  └──────┬───────┘         └──────┬───────┘              │
│         │                        │                       │
│         ├─ Register              ├─ Login               │
│         ├─ Login                 ├─ Add Company         │
│         ├─ Browse Companies      ├─ View Students       │
│         ├─ Apply                 ├─ Review Applications │
│         └─ Track Status          └─ Update Status       │
│                                                           │
│                    ┌──────────────┐                      │
│                    │  Database    │                      │
│                    ├──────────────┤                      │
│                    │ Companies    │                      │
│                    ├──────────────┤                      │
│                    │ Applications │                      │
│                    └──────────────┘                      │
└─────────────────────────────────────────────────────────┘
```

## 🎓 Student Workflow

```
┌─────────────────────────────────────────────────────────────┐
│              STUDENT USER FLOW                               │
└─────────────────────────────────────────────────────────────┘

START
  │
  ├─→ [Home Page]
  │       │
  │       ├─→ "Student Login" → [Login Page]
  │       │       │
  │       │       ├─ Enter: Email/USN + Password
  │       │       └─→ [Dashboard]
  │       │
  │       └─→ "Register" → [Registration Page]
  │               │
  │               ├─ Fill: USN, Name, Email, Phone
  │               ├─ Select: Branch, Semester
  │               ├─ Enter: CGPA, Skills, Password
  │               ├─ Validation: Email unique, CGPA valid
  │               └─→ [Login Page] → [Dashboard]
  │
  ├─→ [Student Dashboard]
  │       │
  │       ├─ View Statistics:
  │       │   • Total Applications
  │       │   • Shortlisted Count
  │       │   • Selected Count
  │       │
  │       ├─→ [View Companies]
  │       │       │
  │       │       ├─ System Checks:
  │       │       │  ✓ CGPA >= Company Min CGPA
  │       │       │  ✓ Branch in Eligible List
  │       │       │  ✓ Deadline not passed
  │       │       │  ✓ (Optional) Skills match
  │       │       │
  │       │       ├─ Shows ONLY eligible companies
  │       │       │
  │       │       └─→ [Apply for Company]
  │       │               │
  │       │               ├─ Check: Not already applied
  │       │               ├─ Check: Is eligible
  │       │               └─→ Success / Error Message
  │       │
  │       ├─→ [My Applications]
  │       │       │
  │       │       └─ Display:
  │       │           • Company Name
  │       │           • Role & Package
  │       │           • Status (Applied/Shortlisted/etc)
  │       │           • Application Date
  │       │
  │       ├─→ [My Profile]
  │       │       │
  │       │       └─ Display Personal & Academic Info
  │       │
  │       └─→ [Logout]
  │
  END
```

## 👨‍💼 Admin Workflow

```
┌─────────────────────────────────────────────────────────────┐
│              ADMIN USER FLOW                                 │
└─────────────────────────────────────────────────────────────┘

START
  │
  ├─→ [Home Page]
  │       │
  │       └─→ "Admin Login"
  │
  ├─→ [Admin Login Page]
  │       │
  │       ├─ Enter: Username + Password
  │       └─→ [Admin Dashboard]
  │
  ├─→ [Admin Dashboard]
  │       │
  │       ├─ View Statistics:
  │       │   • Total Students
  │       │   • Total Companies
  │       │   • Total Applications
  │       │   • Shortlisted Count
  │       │   • Selected Count
  │       │
  │       ├─→ [Add Company]
  │       │       │
  │       │       ├─ Fill:
  │       │       │  • Company Name, Role
  │       │       │  • Package (LPA)
  │       │       │  • Minimum CGPA
  │       │       │  • Eligible Branches
  │       │       │  • Required Skills
  │       │       │  • Application Deadline
  │       │       │
  │       │       └─→ Success Message
  │       │
  │       ├─→ [Manage Companies]
  │       │       │
  │       │       └─ View all added companies
  │       │
  │       ├─→ [View Students]
  │       │       │
  │       │       ├─ Display list with:
  │       │       │  • USN, Name, Email
  │       │       │  • Branch, CGPA
  │       │       │
  │       │       ├─→ [Student Details]
  │       │       │       │
  │       │       │       ├─ Show student info
  │       │       │       └─ Show all applications
  │       │
  │       ├─→ [Review Applications]
  │       │       │
  │       │       ├─ Display table:
  │       │       │  • Student Name (USN)
  │       │       │  • Company Name
  │       │       │  • Role
  │       │       │  • Current Status
  │       │       │  • Application Date
  │       │       │
  │       │       ├─→ [Update Status] (Dropdown)
  │       │       │       │
  │       │       │       ├─ Options:
  │       │       │       │  • Applied
  │       │       │       │  • Shortlisted
  │       │       │       │  • Rejected
  │       │       │       │  • Selected
  │       │       │       │
  │       │       │       └─→ Status Updated
  │       │
  │       └─→ [Logout]
  │
  END
```

## 🔄 Eligibility Check Engine

```
┌─────────────────────────────────────────────────────────────┐
│          ELIGIBILITY CHECKING ALGORITHM                      │
└─────────────────────────────────────────────────────────────┘

When Student Views Companies:

FOR EACH company IN all_companies:
    
    Check 1: CGPA Requirement
    ┌─────────────────────────────────────┐
    │ Student CGPA >= Company Min CGPA?  │
    │ YES ─────────────────────┐          │
    │  NO ─────────────────────┼─ HIDE   │
    └─────────────────────────┘          │
                              └──────────┘
    
    Check 2: Branch Eligibility
    ┌─────────────────────────────────────┐
    │ Student Branch in Eligible List?   │
    │ YES ─────────────────────┐          │
    │  NO ─────────────────────┼─ HIDE   │
    └─────────────────────────┘          │
                              └──────────┘
    
    Check 3: Deadline Passed?
    ┌─────────────────────────────────────┐
    │ Current Date < Deadline?            │
    │ YES ─────────────────────┐          │
    │  NO ─────────────────────┼─ HIDE   │
    └─────────────────────────┘          │
                              └──────────┘
    
    Check 4: Skills (Optional)
    ┌─────────────────────────────────────┐
    │ If required_skills specified:       │
    │   Student has ANY required skill?  │
    │   YES ─────────────────────┐        │
    │   NO ─────────────────────┼─ HIDE  │
    │                            │         │
    │ If no required_skills:     │        │
    │   SHOW ───────────────────┘        │
    └─────────────────────────────────────┘
    
    Result: SHOW COMPANY (eligible for student)

Return: List of eligible companies
```

## 📱 Application Status Lifecycle

```
Student Applies
       │
       ├─→ Status: "Applied"
       │       │
       │       ├─→ [Admin Review]
       │       │       │
       │       │       ├─ OPTION 1: Shortlist
       │       │       │       └─→ Status: "Shortlisted"
       │       │       │           ├─ Further rounds
       │       │       │           └─→ OPTION A: Select
       │       │       │                   └─→ Status: "Selected"
       │       │       │
       │       │       └─ OPTION 2: Reject
       │       │               └─→ Status: "Rejected"
       │       │
       │       └─→ [Student Views on Dashboard]
       │           Shows current status with badge
       │
       END

Legend:
✅ Selected  = Green badge
⭕ Shortlisted = Blue badge
❌ Rejected = Red badge
🔄 Applied = Gray badge
```

## 🔐 Authentication Flow

```
┌─────────────────────────────────────────────────────────────┐
│              AUTHENTICATION FLOW                             │
└─────────────────────────────────────────────────────────────┘

Student Registration:
  User Input
    ↓
  Validation (email unique, CGPA valid, password match)
    ↓
  Password Hash (Werkzeug)
    ↓
  Store in Database
    ↓
  Redirect to Login

Student Login:
  User Input (Email/USN, Password)
    ↓
  Query Database
    ↓
  Check Hash (Werkzeug.check_password_hash)
    ↓
  YES → Create Session (Flask-Login)
         Redirect to Dashboard
    ↓
  NO  → Show Error Message
         Redirect to Login

Protected Routes:
  Request from User
    ↓
  @login_required decorator
    ↓
  Session Valid? 
    ↓
  YES → Serve Page
    ↓
  NO  → Redirect to Login Page

Logout:
  User Click Logout
    ↓
  Clear Session (Flask-Login)
    ↓
  Redirect to Home
```

## 🗄️ Database Relationships

```
┌──────────────────────────────────────────────────────────────┐
│            DATABASE ENTITY RELATIONSHIPS                      │
└──────────────────────────────────────────────────────────────┘

        STUDENTS                        COMPANIES
        ────────                        ─────────
        id (PK)         ┌─────────────┐   id (PK)
        usn ──────┐     │             │   name
        name      │     │             │   role
        email     │     │             │   package
        phone     │     │             │   min_cgpa
        branch    │     │             │   eligible_branches
        semester  │     │ APPLICATIONS    required_skills
        cgpa      │     │             │   deadline
        skills    │     │             │
        password  │     │             │   ┌─ Applied at
                  │     │             │   │  status
        ┌─────────┴─────────┬─────────┴──┬┘
        │                   │
        └─ One-to-Many ────→ Many-to-One
                Relations    Relations:
            An application  • Each application
            connects one    is for one student
            student with    • Each application
            one company     is for one company
                           • One student can have
                            many applications
                           • One company can have
                            many applications
```

## 🚀 Request Response Cycle Example

```
User Action: Student Applies for Google

1. Browser Request
   POST /student/apply/1
   (1 = Google's company ID)

2. Flask Route Handler (student.py)
   ├─ Verify user is logged in (@login_required)
   ├─ Get company from database
   ├─ Check if already applied
   ├─ Call is_eligible() function
   │   ├─ Check CGPA
   │   ├─ Check Branch
   │   ├─ Check Deadline
   │   └─ Check Skills (optional)
   ├─ If eligible AND not applied:
   │   └─ Create Application row
   │       └─ Set status = "Applied"
   │       └─ Save to database
   └─ Return JSON response

3. Database Update
   INSERT INTO applications 
   (student_id, company_id, status, applied_at)
   VALUES (1, 1, 'Applied', NOW())

4. Browser Response
   ├─ Success message displayed
   └─ Application added to "My Applications"
```

---

**This workflow documentation provides a complete overview of how the system works and how users interact with it.**
