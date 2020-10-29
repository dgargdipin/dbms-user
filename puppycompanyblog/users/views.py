# register user
#login user
#logout user
# account update UserForm)

from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user,current_user,logout_user,login_required
from puppycompanyblog import db
from puppycompanyblog.models import User
from puppycompanyblog.users.forms import RegistrationForm,LoginForm,UpdateUserForm
users=Blueprint('users',__name__)

@users.route('/register',methods=['GET', 'POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        # user_data={k:v.data for k,v in form}
        # print(user_data)
        print(form)
        user=User(form.email.data,form.password.data,form.year.data,form.branch.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration!')
        return redirect(url_for('users.login'))
    return render_template('register.html',form=form)

@users.route('/login',methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user =User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash('Login success')
            next=request.args.get('next')
            if next==None or not next[0]=='/':
                next=url_for('core.index')
            return redirect(next)
    
    return render_template('login.html',form=form)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("core.index"))


@users.route('/account',methods=['GET', 'POST'])
@login_required
def account():
    form=UpdateUserForm()
    if form.validate_on_submit():
        
        if form.email.data:
            current_user.email=form.email.data
        db.session.commit()
        flash('User account updated')
        return redirect(url_for('users.account'))
    elif request.method=="GET":
        form.email.data=current_user.email
    return render_template('account.html',form=form)

