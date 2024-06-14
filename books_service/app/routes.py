from flask import request, jsonify, render_template, redirect, url_for
from flask_jwt_extended import jwt_required, decode_token, get_jwt_identity
from .models import Book, db

def init_routes(app):
    @app.route('/')
    def index():
        token = request.args.get('token')
        if token:
            try:
                decoded_token = decode_token(token)
                return render_template('index.html', token=token)
            except:
                return 'Invalid or expired token', 401
        else:
            return 'Token is required', 400

    @app.route('/books', methods=['GET'])
    def get_books():
        token = request.args.get('token')
        if token:
            try:
                decoded_token = decode_token(token)
                books = Book.query.all()
                return render_template('books.html', books=books, token=token)
            except:
                return 'Invalid or expired token', 401
        else:
            return 'Token is required', 400

    @app.route('/add_book', methods=['GET', 'POST'])
    def add_book():
        token = request.args.get('token')
        if token:
            try:
                decoded_token = decode_token(token)
                if request.method == 'POST':
                    data = request.form
                    new_book = Book(title=data['title'], author=data['author'])
                    db.session.add(new_book)
                    db.session.commit()
                    return redirect(url_for('get_books', token=token))
                return render_template('add_book.html', token=token)
            except:
                return 'Invalid or expired token', 401
        else:
            return 'Token is required', 400

    @app.route('/delete_book', methods=['POST'])
    def delete_book_form():
        book_id = request.form.get('book_id')
        token = request.form.get('token')
        if book_id and token:
            try:
                decoded_token = decode_token(token)
                book = Book.query.get(book_id)
                if not book:
                    return 'Book not found', 404
                db.session.delete(book)
                db.session.commit()
                return redirect(url_for('get_books', token=token))
            except:
                return 'Invalid or expired token', 401
        else:
            return 'Book ID and token are required', 400

    @app.route('/delete_book_form', methods=['GET'])
    def render_delete_book_form():
        token = request.args.get('token')
        if token:
            return render_template('delete_book.html', token=token)
        else:
            return 'Token is required', 400

    ######################## ROTA DE UPDATE ###########################

    @app.route('/edit_book/<int:id>', methods=['GET', 'POST'])
    def edit_book(id):
        token = request.args.get('token')
        if token:
            try:
                decoded_token = decode_token(token)
                book = Book.query.get(id)
                if not book:
                    return 'Book not found', 404
                
                if request.method == 'POST':
                    book.title = request.form.get('title')
                    book.author = request.form.get('author')
                    db.session.commit()
                    return redirect(url_for('get_books', token=token))
                
                return render_template('edit_book.html', book=book, token=token)
            except:
                return 'Invalid or expired token', 401
        else:
            return 'Token is required', 400