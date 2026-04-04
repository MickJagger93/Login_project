from flask import Flask
from models import db
from config import Config
from flask_login import LoginManager
from flask_migrate import Migrate

def create_app():
    
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager(app)
    from models import User

    @login_manager.user_loader
    def load_user(user_id):

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