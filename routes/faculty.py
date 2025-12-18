from flask import Blueprint, render_template

faculty_bp = Blueprint('faculty', __name__, url_prefix='/faculty')

@faculty_bp.route('/')
def dashboard():
    return render_template('faculty/dashboard.html')

@faculty_bp.route('/profile')
def profile():
    return render_template('faculty/profile.html')

@faculty_bp.route('/attendance')
def attendance():
    return render_template('faculty/attendance.html')

@faculty_bp.route('/classes')
def classes():
    return render_template('faculty/classes.html')
