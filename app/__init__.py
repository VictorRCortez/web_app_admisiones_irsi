from flask import Flask, render_template
from flask_login import LoginManager
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from flask_talisman import Talisman
from dotenv import load_dotenv
from app.extensions import db, login_manager
import os
import logging
from logging.handlers import RotatingFileHandler

from .config import DevelopmentConfig, ProductionConfig, Config

# Inicialización de extensiones
mail = Mail()
csrf = CSRFProtect()
talisman = Talisman()

def create_app(config_name=None):
    load_dotenv()

    app = Flask(__name__)

    # Configuración según config_name
    if config_name == 'development':
        app.config.from_object(DevelopmentConfig)
    elif config_name == 'production':
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    mail.init_app(app)
    csrf.init_app(app)

    # Configuración de Talisman solo en producción (no testing/dev)
    if config_name != 'testing' and os.getenv("FLASK_ENV") != "development":
        csp = {
            'default-src': "'self'",
            'script-src': "'self' https://cdn.jsdelivr.net",
            'connect-src': "'self'",
            'img-src': "'self' data:",
            'style-src': "'self' https://cdn.jsdelivr.net",
            'font-src': "'self' https://cdn.jsdelivr.net"
        }
        talisman.init_app(app, content_security_policy=csp)

    # Importar modelos después de inicializar db
    from app.models import Usuario

    # Registrar Blueprints
    from app.auth.routes import auth
    from app.main.routes import main
    app.register_blueprint(auth)
    app.register_blueprint(main)

    # Cargar usuario para flask-login
    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    # Manejo de errores 403
    @app.errorhandler(403)
    def forbidden_error(error):
        return render_template('403.html'), 403

    # Configuración de logs solo para producción
    if config_name != 'testing':
        if not os.path.exists('logs'):
            os.mkdir('logs')

        file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=3)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        ))
        file_handler.setLevel(logging.INFO)

        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('App iniciada')

    return app

