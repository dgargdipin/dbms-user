from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_login import LoginManager
app =Flask(__name__)
app.config['SECRET_KEY']='mysecret'
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, '..', '..', 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
Migrate(app,db,render_as_batch=True)
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='users.login'
import cms.models
db.create_all()
from cms.core.views import core
from cms.error_pages.handlers import error_pages
from cms.users.views import users
from cms.course.views import CourseBluerint
app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(CourseBluerint)
print("route path is, ", core.root_path )

