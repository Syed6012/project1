from flask import Flask
from routes.common import common_bp
from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.student import student_bp
from routes.faculty import faculty_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(common_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(student_bp)
app.register_blueprint(faculty_bp)

if __name__ == '__main__':
    app.run(debug=True)
