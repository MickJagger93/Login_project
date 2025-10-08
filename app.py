"""
app.py

Archivo principal de la aplicación Flask para el sistema de autenticación de usuarios.
Configura la aplicación, la base de datos, la gestión de sesiones y registra los blueprints.
"""

from flask import Flask
from models import db
from config import Config
from flask_login import LoginManager
from flask_migrate import Migrate

def create_app():
    
    """
    Crea y configura la instancia principal de la aplicación Flask.

    - Inicializa la configuración desde el objeto Config.
    - Inicializa la base de datos y las migraciones.
    - Configura Flask-Login para la gestión de sesiones de usuario.
    - Registra los blueprints de autenticación y rutas principales.

    Returns:
        app (Flask): La aplicación Flask configurada.
    """
    
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager(app)
    from models import User

    @login_manager.user_loader
    def load_user(user_id):

        """
        Carga un usuario desde la base de datos por su ID.

        Args:
            user_id (int): ID del usuario.

        Returns:
            User: Instancia del usuario si existe, si no, None.
        """

        return db.session.get(User, user_id)

    from auth.routes import auth_bp
    from main.routes import main_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)