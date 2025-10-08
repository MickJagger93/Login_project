"""
config.py

Define la configuración principal de la aplicación Flask, incluyendo la clave secreta y la URI de la base de datos.
Permite la configuración mediante variables de entorno o valores por defecto.
"""

import os

class Config:
    
    """
    Clase de configuración para la aplicación Flask.

    Atributos de clase:
        SECRET_KEY (str): Clave secreta para la gestión de sesiones y seguridad.
        SQLALCHEMY_DATABASE_URI (str): URI de la base de datos utilizada por SQLAlchemy.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Desactiva el seguimiento de modificaciones para mejorar el rendimiento.
    """
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or '75004f149038473757da0be07ef76dd4a9bdbc8d'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///login.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

