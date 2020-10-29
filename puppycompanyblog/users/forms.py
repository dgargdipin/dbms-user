from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField   
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed

from flask_login import current_user
from puppycompanyblog.models import User

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired('Data required'),Email('email required')])
    password=PasswordField('Password',validators=[DataRequired('Data required')])
    submit=SubmitField('Login')

class RegistrationForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired('Data required'),Email('email required')])
    password=PasswordField('Password',validators=[DataRequired('Data required'),
    EqualTo('pass_confirm',message="Passwords must match!")])
    pass_confirm=PasswordField('Confirm Password',validators=[DataRequired('Data required')])
    year = SelectField('Year of study', choices=[
                       (1, '1st'), (2, '2nd'), (3, '3rd'),(4,'4th')])
    branch = SelectField('Branch', validators=[DataRequired('Data required')],
                                            choices=[('CSE',"Computer Science"),('EE','Electrical'),('ME','Mechanical'),('CE','Civil')])
    submit=SubmitField('Register')
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already')
    

class UpdateUserForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired('Data required'),Email('email required')])
    submit=SubmitField('Update')
    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already')
    
