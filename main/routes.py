"""
routes.py

Define las rutas principales de la aplicación Flask.
Incluye rutas para la página de inicio, home y landing (protegida para usuarios autenticados).
"""

from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from models import User, db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():

    """
    Redirige la ruta raíz ('/') a la página principal ('/home').
    """
    return redirect(url_for('main.home'))

@main_bp.route('/home')
def home():

    """
    Renderiza la plantilla base para la página principal.
    """
    return render_template('layouts/base.html')

@main_bp.route('/landing')
@login_required
def landing():

    """
    Renderiza la página 'landing' solo para usuarios autenticados.

    Returns:
        Renderiza 'landing.html' con la información del usuario actual.
    """
    user = db.session.get(User, current_user.id)
    return render_template('/layouts/partials/landing.html', user=user)