"""
models.py

Define los modelos de base de datos para la aplicación Flask.
Incluye el modelo de usuario y la configuración de SQLAlchemy.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):

    """
    Modelo de usuario para la base de datos.

    Atributos:
        id (int): Identificador único del usuario.
        name (str): Nombre del usuario.
        email (str): Correo electrónico único del usuario.
        password_hash (str): Hash seguro de la contraseña del usuario.
    """
    
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email, password):

        """
        Inicializa una nueva instancia de usuario y almacena el hash de la contraseña.

        Args:
            name (str): Nombre del usuario.
            email (str): Correo electrónico del usuario.
            password (str): Contraseña en texto plano.
        """
        
        self.name = name
        self.email = email
        self.set_password(password)
    
    def set_password(self, password):

        """
        Genera y almacena el hash de la contraseña del usuario.

        Args:
            password (str): Contraseña en texto plano.
        """
        
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):

        """
        Verifica si la contraseña proporcionada coincide con el hash almacenado.

        Args:
            password (str): Contraseña en texto plano.

        Returns:
            bool: True si la contraseña es correcta, False en caso contrario.
        """
        
        return check_password_hash(self.password_hash, password)