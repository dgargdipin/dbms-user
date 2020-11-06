from enum import unique

from sqlalchemy.orm import backref
# from cms.core.views import index
from cms import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


course_helper=db.Table('course_helper',
                        db.Column('user_id',db.Integer,db.ForeignKey('users.id')),
                        db.Column('course_id',db.Integer,db.ForeignKey('courses.id'))
                        )
branch_helper=db.Table('branch_helper',
                        db.Column('course_id',db.Integer,db.ForeignKey('courses.id')),
                        db.Column('branch_id',db.Integer,db.ForeignKey('branches.id'))
                        )


class Branch(db.Model):
    __tablename__='branches'
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    students=db.relationship('User',backref='branch')
    professors = db.relationship('Professor', backref='branch')
    def __init__(self,name):
        self.name = name
    def __repr__(self) -> str:
        return self.name

class User(db.Model,UserMixin):
    __tablename__='users'
    name=db.Column(db.String(),nullable=False)
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String(64),unique=True,index=True)
    password_hash=db.Column(db.String(128))
    year=db.Column(db.Integer())
    branch_id=db.Column(db.Integer,db.ForeignKey('branches.id'))
    courses = db.relationship('Course', secondary=course_helper,
                              backref=db.backref('students'))
    def __init__(self,name,email,password,year,branch_id):
        self.name=name
        self.email=email
        self.password_hash=generate_password_hash(password)
        self.year=year
        self.branch_id=branch_id

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)


class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    details = db.Column(db.String())
    prof_id = db.Column(db.Integer, db.ForeignKey(
        'professors.id'), nullable=False)
    course_code = db.Column(db.String(), unique=True)
    branches=db.relationship('Branch',secondary=branch_helper,backref=db.backref('courses'))
    can_apply=db.Column(db.Boolean)
    courseNotes = db.relationship('courseNote', backref='Course')
    def __init__(self, name, course_code, details, prof_id,can_apply,):
        self.name = name
        self.course_code = course_code
        self.details = details
        self.prof_id = prof_id
        self.can_apply=can_apply


class Professor(db.Model, UserMixin):
    __tablename__ = 'professors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String(64), unique=True, index=True)
    branch_id = db.Column(db.Integer, db.ForeignKey('branches.id'))
    courses = db.relationship('Course', backref='professor', lazy=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, name, email, password, branch_id):
        self.email = email
        self.name = name
        self.password_hash = generate_password_hash(password)
        self.branch_id = branch_id

class courseNote(db.Model):
    __tablename__='coursenotes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    details = db.Column(db.String())
    time=db.Column(db.DateTime,nullable=False,default=datetime.now)
    attachments=db.relationship('Attachment',backref='coursenote')
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    def __init__(self,title,details,course_id):
        self.title=title
        self.details=details
        self.course_id=course_id
class Attachment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    ext = db.Column(db.String(10))
    link = db.Column(db.String())
    coursenote_id=db.Column(db.Integer,db.ForeignKey('coursenotes.id'))
    def __init__(self,name,ext,link,coursenote_id):
        self.name=name
        self.ext=ext
        self.link=link
        self.coursenote_id=coursenote_id
    
