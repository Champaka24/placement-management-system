"""
Database initialization script with sample data
Run this script to populate the database with test data
"""

from app import create_app, db
from app.models import Admin, Company, Student
from datetime import datetime, timedelta

def init_db():
    """Initialize database with sample data"""
    app = create_app()
    
    with app.app_context():
        # Drop existing tables and recreate
        db.drop_all()
        db.create_all()
        print("✓ Database tables created")
        
        # Create Admin Users
        admin = Admin(
            username='admin',
            email='admin@placement.edu'
        )
        admin.set_password('admin123')
        db.session.add(admin)
        print("✓ Admin user created (username: admin, password: admin123)")
        
        # Create Sample Companies
        companies = [
            Company(
                name='Google',
                role='Software Development Engineer',
                package=22.5,
                min_cgpa=7.5,
                eligible_branches='CSE, ECE',
                required_skills='Python, Java, C++',
                application_deadline=datetime.utcnow() + timedelta(days=30)
            ),
            Company(
                name='Microsoft',
                role='Associate Software Engineer',
                package=20.0,
                min_cgpa=7.0,
                eligible_branches='CSE, ECE',
                required_skills='C#, Java, Python',
                application_deadline=datetime.utcnow() + timedelta(days=25)
            ),
            Company(
                name='Amazon',
                role='Software Development Engineer - Backend',
                package=21.0,
                min_cgpa=7.0,
                eligible_branches='CSE',
                required_skills='Java, Python, Node.js',
                application_deadline=datetime.utcnow() + timedelta(days=20)
            ),
            Company(
                name='Infosys',
                role='Systems Engineer',
                package=6.0,
                min_cgpa=6.0,
                eligible_branches='CSE, ECE, ME',
                required_skills='',
                application_deadline=datetime.utcnow() + timedelta(days=15)
            ),
            Company(
                name='TCS',
                role='Software Developer',
                package=5.5,
                min_cgpa=6.0,
                eligible_branches='CSE, ECE, ME, CE',
                required_skills='',
                application_deadline=datetime.utcnow() + timedelta(days=10)
            ),
        ]
        
        for company in companies:
            db.session.add(company)
        
        db.session.commit()
        print(f"✓ {len(companies)} sample companies created")
        
        # Create Sample Students
        students = [
            Student(
                usn='USN001',
                name='Raj Kumar',
                email='raj@example.com',
                phone='9876543210',
                branch='CSE',
                semester=6,
                cgpa=8.5,
                skills='Python, Java, C++'
            ),
            Student(
                usn='USN002',
                name='Priya Singh',
                email='priya@example.com',
                phone='9876543211',
                branch='CSE',
                semester=6,
                cgpa=7.8,
                skills='Python, JavaScript, React'
            ),
            Student(
                usn='USN003',
                name='Arjun Patel',
                email='arjun@example.com',
                phone='9876543212',
                branch='ECE',
                semester=7,
                cgpa=7.5,
                skills='Java, C++, Python'
            ),
        ]
        
        for student in students:
            student.set_password('password123')
            db.session.add(student)
        
        db.session.commit()
        print(f"✓ {len(students)} sample students created")
        
        print("\n✅ Database initialization completed!")
        print("\nTest Credentials:")
        print("=" * 50)
        print("\nAdmin Login:")
        print("  Username: admin")
        print("  Password: admin123")
        print("\nStudent Login (Sample):")
        print("  Email/USN: raj@example.com or USN001")
        print("  Password: password123")
        print("=" * 50)

if __name__ == '__main__':
    init_db()
