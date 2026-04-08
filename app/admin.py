from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app import db
from app.models import Student, Admin, Company, Application
from datetime import datetime

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.before_request
def check_admin():
    """Ensure only admins access admin routes"""
    if not isinstance(current_user, Admin):
        flash('Access denied!', 'danger')
        return redirect(url_for('main.index'))

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    """Admin dashboard"""
    total_students = Student.query.count()
    total_companies = Company.query.count()
    total_applications = Application.query.count()
    shortlisted = Application.query.filter_by(status='Shortlisted').count()
    selected = Application.query.filter_by(status='Selected').count()
    
    context = {
        'total_students': total_students,
        'total_companies': total_companies,
        'total_applications': total_applications,
        'shortlisted': shortlisted,
        'selected': selected
    }
    return render_template('admin/dashboard.html', **context)

@admin_bp.route('/add-company', methods=['GET', 'POST'])
@login_required
def add_company():
    """Add new company"""
    if request.method == 'POST':
        name = request.form.get('name')
        role = request.form.get('role')
        package = request.form.get('package')
        min_cgpa = request.form.get('min_cgpa')
        eligible_branches = request.form.get('eligible_branches')
        required_skills = request.form.get('required_skills')
        deadline = request.form.get('deadline')
        
        try:
            company = Company(
                name=name,
                role=role,
                package=float(package),
                min_cgpa=float(min_cgpa),
                eligible_branches=eligible_branches,
                required_skills=required_skills,
                application_deadline=datetime.strptime(deadline, '%Y-%m-%dT%H:%M')
            )
            db.session.add(company)
            db.session.commit()
            flash('Company added successfully!', 'success')
            return redirect(url_for('admin.view_companies'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('admin/add_company.html')

@admin_bp.route('/companies')
@login_required
def view_companies():
    """View all companies"""
    companies = Company.query.all()
    return render_template('admin/view_companies.html', companies=companies)

@admin_bp.route('/students')
@login_required
def view_students():
    """View all students"""
    students = Student.query.all()
    return render_template('admin/view_students.html', students=students)

@admin_bp.route('/applications')
@login_required
def view_applications():
    """View all applications"""
    applications = Application.query.all()
    return render_template('admin/view_applications.html', applications=applications)

@admin_bp.route('/update-status/<int:app_id>', methods=['POST'])
@login_required
def update_status(app_id):
    """Update application status"""
    application = Application.query.get_or_404(app_id)
    new_status = request.form.get('status')
    
    if new_status not in ['Applied', 'Shortlisted', 'Rejected', 'Selected']:
        return jsonify({'error': 'Invalid status'}), 400
    
    try:
        application.status = new_status
        application.updated_at = datetime.utcnow()
        db.session.commit()
        flash('Status updated successfully!', 'success')
        return redirect(url_for('admin.view_applications'))
    except Exception as e:
        db.session.rollback()
        flash(f'Error: {str(e)}', 'danger')
        return redirect(url_for('admin.view_applications'))

@admin_bp.route('/student/<int:student_id>')
@login_required
def view_student_detail(student_id):
    """View student details"""
    student = Student.query.get_or_404(student_id)
    applications = Application.query.filter_by(student_id=student_id).all()
    return render_template('admin/student_detail.html', student=student, applications=applications)
