from flask import Blueprint, render_template

student_bp = Blueprint('student', __name__, url_prefix='/student')

@student_bp.route('/attendance')
def attendance():
    return render_template('student/attendance.html')
