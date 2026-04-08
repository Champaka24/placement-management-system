from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import Student, Admin

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/student-register', methods=['GET', 'POST'])
def student_register():
    """Student registration"""
    if request.method == 'POST':
        usn = request.form.get('usn')
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        branch = request.form.get('branch')
        semester = request.form.get('semester')
        cgpa = request.form.get('cgpa')
        skills = request.form.get('skills')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validation
        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('auth.student_register'))
        
        if Student.query.filter_by(usn=usn).first():
            flash('USN already exists!', 'danger')
            return redirect(url_for('auth.student_register'))
        
        if Student.query.filter_by(email=email).first():
            flash('Email already registered!', 'danger')
            return redirect(url_for('auth.student_register'))
        
        # Create new student
        try:
            student = Student(
                usn=usn,
                name=name,
                email=email,
                phone=phone,
                branch=branch,
                semester=int(semester),
                cgpa=float(cgpa),
                skills=skills
            )
            student.set_password(password)
            db.session.add(student)
            db.session.commit()
            
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('auth.student_login'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
            return redirect(url_for('auth.student_register'))
    
    return render_template('auth/student_register.html')

@auth_bp.route('/student-login', methods=['GET', 'POST'])
def student_login():
    """Student login"""
    if current_user.is_authenticated:
        return redirect(url_for('student.dashboard'))
    
    if request.method == 'POST':
        identifier = request.form.get('identifier')  # email or USN
        password = request.form.get('password')
        
        student = Student.query.filter(
            (Student.email == identifier) | (Student.usn == identifier)
        ).first()
        
        if student and student.check_password(password):
            login_user(student)
            flash('Login successful!', 'success')
            return redirect(url_for('student.dashboard'))
        else:
            flash('Invalid credentials!', 'danger')
    
    return render_template('auth/student_login.html')

@auth_bp.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    """Admin login"""
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        admin = Admin.query.filter_by(username=username).first()
        
        if admin and admin.check_password(password):
            login_user(admin)
            flash('Login successful!', 'success')
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid credentials!', 'danger')
    
    return render_template('auth/admin_login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    """Logout"""
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('auth.student_login'))
