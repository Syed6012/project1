from flask import Blueprint, render_template

common_bp = Blueprint('common', __name__)

@common_bp.route('/')
def home():
    return render_template('common/home.html')

@common_bp.route('/profile')
def profile():
    return render_template('common/profile.html')
