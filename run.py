import os
from app import create_app, db
from app.models import Student, Admin, Company, Application

app = create_app(os.environ.get('FLASK_ENV', 'development'))

@app.shell_context_processor
def make_shell_context():
    """Add models to Flask shell context"""
    return {
        'db': db,
        'Student': Student,
        'Admin': Admin,
        'Company': Company,
        'Application': Application
    }

if __name__ == '__main__':
    app.run(debug=True)
