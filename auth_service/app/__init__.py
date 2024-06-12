from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    db_path = os.path.join(os.path.dirname(__file__), 'users.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['JWT_SECRET_KEY'] = 'super-secret'

    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        from . import routes
        routes.init_routes(app)
        db.create_all()

    return app
