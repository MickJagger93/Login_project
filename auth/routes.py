from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from models import User, db
from forms import LoginForm, RegisterForm, ResetForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data

        if password != confirm_password:

            flash('Passwords do not match. Please try again.')
            return render_template('layouts/partials/register.html', form=form)

        user = User.query.filter_by(email=email).first()

        if user:

            flash('Your email is aready registered')
            return redirect(url_for('auth.register'))

        else:
            
            user = User(name=name, email=email, password=password)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()

            flash('Successfully registration! Please log in.')
            return redirect(url_for('auth.login'))
    
    return render_template('layouts/partials/register.html', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    
    if form.validate_on_submit():
        
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):

            login_user(user)
            return redirect(url_for('main.landing'))
            
        else:
            flash('User not found or incorrect password. Try again')
        
    return render_template('layouts/partials/login.html', form=form)

@auth_bp.route('/reset_password', methods=['GET', 'POST'])
def reset_password():

    form = ResetForm()

    if form.validate_on_submit:
        
        email = form.email.data
        new_password = form.new_password.data
        confirm_new_password = form.confirm_new_password.data

        if new_password == confirm_new_password:

            user = User.query.filter_by(email=email).first()

            if user:

                user.set_password(new_password)
                db.session.commit()

                flash('Your password has been successfully updated!')
                return redirect(url_for('auth.login'))
        
        else:
            flash('Passwords do not match or invalid email. Please try again.')

    return render_template('layouts/partials/reset_password.html', form=form)

@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():

    logout_user()
    flash('You have been logged out succesfully.')
    return redirect(url_for('auth.login'))