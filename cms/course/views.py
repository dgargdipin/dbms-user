import string
import random
import os
from flask import render_template, url_for, flash, redirect, request, Blueprint, abort,send_from_directory
from flask.templating import render_template_string
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename
from cms import basedir,db
from cms.models import Attachment, Quiz, QuizResponse, Submission, User, Course, quizQuestionResponse

from cms.users.forms import RegistrationForm, LoginForm, UpdateUserForm
CourseBluerint = Blueprint('course', __name__)
cb=CourseBluerint
from .forms import quiz_factory, submissionForm
@cb.route('/serve/<filename>')
@login_required
def serve_file(filename):
    return send_from_directory(os.path.join(basedir, '..', '..', 'static_material'), filename=filename, as_attachment=True)


@cb.route('/course/<course_id>',methods=['GET', 'POST'])
@login_required
def view_course(course_id):
    submissionArray = [a.assignment_id for a in current_user.submissions ]
    print(submissionArray)
    form=submissionForm()
    if form.submit.data and form.validate:
        attachments = []
        if not current_user.is_authenticated:
            abort(405)
        print(form.title.data, form.details.data, form.assignment_id.data)
        newCourseNote = Submission(
            form.title.data, form.details.data,form.assignment_id.data,current_user.id)
        db.session.add(newCourseNote)
        db.session.commit()
        
        if form.attachments.data:
            print(form.attachments.data, request.files)
            for uploaded_file in request.files.getlist('attachments'):

                filename, file_extension = os.path.splitext(
                    uploaded_file.filename)
                if not filename or not file_extension:
                    continue
                savename = secure_filename(filename)+''.join(
                    random.choice(string.ascii_lowercase) for i in range(16))+file_extension
                print(filename, savename)
                if savename == "":
                    break

                uploaded_file.save(os.path.join(
                    basedir, '..', '..', 'static_material', savename))
                new_attachment = Attachment(
                    filename, file_extension, url_for('course.serve_file', filename=savename), submission_id=newCourseNote.id)
                attachments.append(new_attachment)
        print(attachments)

        db.session.add_all(attachments)
        db.session.commit()
        return redirect(url_for('course.view_course', course_id=course_id))
    courseToRender=Course.query.filter_by(id=course_id).first()
    return render_template('view_course.html',course=courseToRender,form=form,submissionArray=submissionArray)





@cb.route('/course/drop/<course_id>')
@login_required
def unenroll(course_id):
    courseToDrop = Course.query.filter_by(id=course_id).first()
    current_user.courses.remove(courseToDrop)
    db.session.commit()
    return redirect(url_for('core.index'))


@cb.route('/quiz/attempt/<quiz_id>',methods=['GET', 'POST'])
def attempt_quiz(quiz_id):
    current_quiz=Quiz.query.get_or_404(quiz_id)
    # if current_user not in current_quiz.course.students:
        # abort(405)
    quiz_Class,default_fields=quiz_factory(current_quiz)
    quiz_form=quiz_Class()
    if quiz_form.Submit.data and quiz_form.validate:
        print(quiz_form.data.items())
        qResponse=QuizResponse(user_id=current_user.id,quiz_id=quiz_id)
        db.session.add(qResponse)
        for field in quiz_form:
            if not field.name.startswith("question"):continue
            print(field.name)
            question_id=int(field.name.split('_')[1])
            qqResponse=quizQuestionResponse(user_id=current_user.id,question_id=question_id,quiz_id=quiz_id,response=str(field.data))
            db.session.add(qqResponse)
            qResponse.quizQuestionResponses.append(qqResponse)
        db.session.commit()
    


        
    return render_template('give_quiz.html',form=quiz_form,)
