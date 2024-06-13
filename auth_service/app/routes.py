from flask import request, jsonify, render_template, redirect, url_for
from flask_jwt_extended import create_access_token, jwt_required
from .models import User, db

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            data = request.form
            user = User.query.filter_by(username=data['username']).first()
            if user and user.password == data['password']:
                access_token = create_access_token(identity={'username': user.username})
                # Redirecionar para o serviço de livros com o token como parâmetro na URL
                return redirect(f'http://127.0.0.1:5002/?token={access_token}')
            else:
                return 'Invalid credentials', 401
        return render_template('login.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            data = request.form
            new_user = User(username=data['username'], password=data['password'])
            db.session.add(new_user)
            db.session.commit()
            access_token = create_access_token(identity={'username': new_user.username})
            # Redirecionar para o serviço de livros com o token como parâmetro na URL
            return redirect(f'http://127.0.0.1:5002/?token={access_token}')
        return render_template('register.html')
