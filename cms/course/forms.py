from cms.models import Quiz
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField,SelectMultipleField,TextAreaField
from wtforms.fields.core import RadioField
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


def quiz_factory(quiz):
    class QuizForm(FlaskForm):
        pass
    
    for question in quiz.questions:
        if question.is_multicorrect:
            setattr(QuizForm, f"question_{question.id}", SelectMultipleField(question.question,choices=[(option.id,option.option) for option in question.options],coerce=int,validators=[DataRequired('Data required')]))
        else:
            setattr(QuizForm, f"question_{question.id}", RadioField(question.question,choices=[(option.id,option.option) for option in question.options],coerce=int,validators=[DataRequired('Data required')]))
    setattr(QuizForm,'Submit',SubmitField('Submit'))
    print(vars(QuizForm))
    return QuizForm,['Submit']

class postForm(FlaskForm):
    details = TextAreaField('Details', validators=[DataRequired('Data required')])
    attachments = MultipleFileField('Attachments')
    submit = SubmitField('Submit')