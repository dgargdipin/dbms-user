from flask import render_template, request,Blueprint
from flask_login import current_user
core=Blueprint('core',__name__)
print("__name__ is ",__name__)


@core.route('/')
def index():
    enrolled_courses = None
    if current_user.is_authenticated:
        enrolled_courses=current_user.courses
    return render_template('index.html',enrolled_courses=enrolled_courses)

@core.route('/info')
def info():
    return render_template('info.html')