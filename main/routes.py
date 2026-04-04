from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from models import User, db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():

    return redirect(url_for('main.home'))

@main_bp.route('/home')
def home():

    return render_template('layouts/base.html')

@main_bp.route('/landing')
@login_required
def landing():

    user = db.session.get(User, current_user.id)
    return render_template('/layouts/partials/landing.html', user=user)