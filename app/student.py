from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import Student, Company, Application
from datetime import datetime

student_bp = Blueprint('student', __name__, url_prefix='/student')

@student_bp.before_request
def check_student():
    """Ensure only students access student routes"""
    if not isinstance(current_user, Student):
        flash('Access denied!', 'danger')
        return redirect(url_for('main.index'))

@student_bp.route('/dashboard')
@login_required
def dashboard():
    """Student dashboard"""
    # Count statistics
    total_applications = Application.query.filter_by(student_id=current_user.id).count()
    shortlisted = Application.query.filter_by(student_id=current_user.id, status='Shortlisted').count()
    selected = Application.query.filter_by(student_id=current_user.id, status='Selected').count()
    
    context = {
        'total_applications': total_applications,
        'shortlisted': shortlisted,
        'selected': selected
    }
    return render_template('student/dashboard.html', **context)

@student_bp.route('/view-companies')
@login_required
def view_companies():
    """View all companies"""
    companies = Company.query.all()
    
    # Check eligibility for each company
    eligible_companies = []
    for company in companies:
        if is_eligible(current_user, company):
            eligible_companies.append(company)
    
    return render_template('student/view_companies.html', companies=eligible_companies)

@student_bp.route('/apply/<int:company_id>', methods=['POST'])
@login_required
def apply_company(company_id):
    """Apply for a company"""
    company = Company.query.get_or_404(company_id)
    
    # Check if already applied
    existing_app = Application.query.filter_by(
        student_id=current_user.id,
        company_id=company_id
    ).first()
    
    if existing_app:
        flash('You have already applied to this company!', 'warning')
        return redirect(url_for('student.view_companies'))
    
    # Check eligibility
    if not is_eligible(current_user, company):
        flash('You are not eligible for this company!', 'danger')
        return redirect(url_for('student.view_companies'))
    
    try:
        application = Application(
            student_id=current_user.id,
            company_id=company_id
        )
        db.session.add(application)
        db.session.commit()
        flash(f'Application submitted successfully for {company.name}!', 'success')
        return redirect(url_for('student.view_applications'))
    except Exception as e:
        db.session.rollback()
        flash(f'Error submitting application: {str(e)}', 'danger')
        return redirect(url_for('student.view_companies'))

@student_bp.route('/applications')
@login_required
def view_applications():
    """View student's applications"""
    applications = Application.query.filter_by(student_id=current_user.id).all()
    return render_template('student/applications.html', applications=applications)

@student_bp.route('/profile')
@login_required
def profile():
    """View student profile"""
    return render_template('student/profile.html', student=current_user)

def is_eligible(student, company):
    """Check if student is eligible for company"""
    # Check CGPA
    if student.cgpa < company.min_cgpa:
        return False
    
    # Check branch
    eligible_branches = [b.strip() for b in company.eligible_branches.split(',')]
    if student.branch not in eligible_branches:
        return False
    
    # Check application deadline
    if datetime.utcnow() > company.application_deadline:
        return False
    
    # Check skills (optional)
    if company.required_skills:
        required_skills = [s.strip().lower() for s in company.required_skills.split(',')]
        student_skills = [s.strip().lower() for s in student.skills.split(',')]
        if not any(skill in student_skills for skill in required_skills):
            return False
    
    return True
