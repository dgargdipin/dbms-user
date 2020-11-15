from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField
from wtforms.fields.simple import MultipleFileField, TextAreaField   
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed

from flask_login import current_user
from cms.models import User,Branch

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired('Data required'),Email('email required')])
    password=PasswordField('Password',validators=[DataRequired('Data required')])
    submit=SubmitField('Login')

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired('Data required')])
    email=StringField('Email',validators=[DataRequired('Data required'),Email('email required')])
    password=PasswordField('Password',validators=[DataRequired('Data required'),
    EqualTo('pass_confirm',message="Passwords must match!")])
    pass_confirm=PasswordField('Confirm Password',validators=[DataRequired('Data required')])
    choices=[(branch.id,branch.name) for branch in Branch.query.all()]
    print("choices are",choices)
    year = SelectField('Year of study', choices=[
                       (1, '1st'), (2, '2nd'), (3, '3rd'),(4,'4th')])
    branch = SelectField('Branch', validators=[DataRequired('Data required')],
                                            choices=choices)
    submit=SubmitField('Register')
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already')
    

class UpdateUserForm(FlaskForm):
    email=StringField('Email',validators=[Email('email required')])
    password=StringField('Password')
    submit=SubmitField('Update')
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already')
    

class requestCourseForm(FlaskForm):
    title = StringField('Title of your request', validators=[
                        DataRequired('Data required')])
    course_id = StringField('Assignment Id', validators=[
                                DataRequired('Data required')])
    details = TextAreaField('Details')
    attachments = MultipleFileField('Attachments')
    submit = SubmitField('Submit')
