from sqlite3 import IntegrityError
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from .models import User, db

def init_routes(app):
    @app.route('/')
    def index():
        return 'Welcome to the Auth Service!'

    @app.route('/auth/register', methods=['POST'])
    def register():
        data = request.get_json()
        new_user = User(username=data['username'], password=data['password'])
        try:
            db.session.add(new_user)
            db.session.commit()
            access_token = create_access_token(identity={'username': new_user.username})
            return jsonify(message="User created", access_token=access_token), 201
        except IntegrityError:
            db.session.rollback()
            return jsonify(message="Username already exists"), 400
        except Exception as e:
            db.session.rollback()
            return jsonify(message="An error occurred while creating the user"), 500

    @app.route('/auth/login', methods=['POST'])
    def login():
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user and user.password == data['password']:
            access_token = create_access_token(identity={'username': user.username})
            return jsonify(access_token=access_token), 200
        else:
            return jsonify(message="Invalid credentials"), 401