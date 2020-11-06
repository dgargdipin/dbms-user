import os
from flask import render_template, url_for, flash, redirect, request, Blueprint, abort,send_from_directory
from flask_login import login_user, current_user, logout_user, login_required
from cms import basedir,db

from cms.models import User, Course

from cms.users.forms import RegistrationForm, LoginForm, UpdateUserForm
CourseBluerint = Blueprint('course', __name__)
cb=CourseBluerint

@cb.route('/serve/<filename>')
@login_required
def serve_file(filename):
    return send_from_directory(os.path.join(basedir, '..', '..', 'static_material'), filename=filename, as_attachment=True)


@cb.route('/course/<course_id>')
@login_required
def view_course(course_id):
    courseToRender=Course.query.filter_by(id=course_id).first()
    return render_template('view_course.html',course=courseToRender)





@cb.route('/course/drop/<course_id>')
@login_required
def unenroll(course_id):
    courseToDrop = Course.query.filter_by(id=course_id).first()
    current_user.courses.remove(courseToDrop)
    db.session.commit()
    return redirect(url_for('core.index'))
