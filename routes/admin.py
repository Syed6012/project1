from flask import Blueprint, render_template

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
def dashboard():
    return render_template('admin/dashboard.html')

@admin_bp.route('/users')
def users():
    return render_template('admin/users.html')

@admin_bp.route('/faculty')
def faculty_portal():
    return render_template('admin/faculty_portal.html')

@admin_bp.route('/faculty/add')
def faculty_add():
    return render_template('admin/faculty/add.html')

@admin_bp.route('/faculty/list')
def faculty_list():
    return render_template('admin/faculty/list.html')

@admin_bp.route('/faculty/profile')
def faculty_profile():
    return render_template('admin/faculty/profile.html')

@admin_bp.route('/faculty/subject-allocation')
def faculty_subject_allocation():
    return render_template('admin/faculty/subject_allocation.html')

@admin_bp.route('/faculty/time-table')
def faculty_time_table():
    return render_template('admin/faculty/time_table.html')
