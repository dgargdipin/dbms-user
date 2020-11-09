from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField,SelectMultipleField,TextAreaField
from wtforms.fields.simple import MultipleFileField
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed
from wtforms.validators import DataRequired

class submissionForm(FlaskForm):
    title = StringField('Submission Title', validators=[
                        DataRequired('Data required')])
    assignment_id=StringField('Assignment Id',validators=[DataRequired('Data required')])
    details = TextAreaField('Details')
    attachments=MultipleFileField('Attachments')
    submit=SubmitField('Submit')
