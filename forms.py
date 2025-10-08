"""
forms.py

Define los formularios utilizados en la aplicación Flask para autenticación y gestión de usuarios.
Incluye formularios para inicio de sesión, registro y restablecimiento de contraseña.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):

    """
    Formulario para el inicio de sesión de usuarios.

    Campos:
        email (StringField): Correo electrónico del usuario.
        password (PasswordField): Contraseña del usuario.
        submit (SubmitField): Botón para enviar el formulario.
    """
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')

class RegisterForm(FlaskForm):

    """
    Formulario para el registro de nuevos usuarios.

    Campos:
        name (StringField): Nombre del usuario.
        email (StringField): Correo electrónico del usuario.
        password (PasswordField): Contraseña del usuario.
        confirm_password (PasswordField): Confirmación de la contraseña.
        remember_password (BooleanField): Opción para recordar la contraseña.
        submit (SubmitField): Botón para enviar el formulario.
    """
    
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired()])
    remember_password = BooleanField('Remember password')
    submit = SubmitField('Register')

class ResetForm(FlaskForm):

    """
    Formulario para restablecer la contraseña de un usuario.

    Campos:
        email (StringField): Correo electrónico del usuario.
        new_password (PasswordField): Nueva contraseña.
        confirm_new_password (PasswordField): Confirmación de la nueva contraseña.
        submit (SubmitField): Botón para enviar el formulario.
    """
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    new_password = PasswordField('New password', validators=[DataRequired()])
    confirm_new_password = PasswordField('Confirm new password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Reset password')


