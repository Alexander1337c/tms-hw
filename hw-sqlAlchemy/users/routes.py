from users import users
from flask import render_template, redirect, url_for, request, session
from .queries import methods
from werkzeug.security import check_password_hash, generate_password_hash

menu = [{'url': 'books.select_books', 'title': 'Книги'}, {'url': 'authors.index', 'title': 'Авторы'}]


@users.route("/")
def index():
    return render_template("users/index.html", title='Пользователь', menu=menu)


@users.route('/register', methods=['POST', 'GET'])
def register():
    errors = []
    cls = None
    if request.method == 'POST':
        name = request.form['name']
        pasw1 = request.form['password1']
        pasw2 = request.form['password2']
        email = request.form['email']
        user = methods.select_email_user(email)
        if len(name) < 8:
            errors.append('Пароль должен быть не менее 8 символов')
        if pasw1 != pasw2:
            errors.append('Пароли не совпадают')
        if user and email == user.email:
            errors.append('Такой пользователь уже существует')
        if errors:
            cls = 'faild'
            return render_template('users/register.html', title='Регистрация', menu=menu, errors=errors, cls=cls)
        hash_pw = generate_password_hash(pasw1)
        methods.add_user(name, email, hash_pw)
        return redirect(url_for('index_app'))
    if request.method == 'GET':
        return render_template('users/register.html', title='Регистрация', menu=menu)


@users.route('/login', methods=['POST', 'GET'])
def login():
    errors = []
    cls = ''
    if request.method == 'POST':
        pasw = request.form['password1']
        email_req = request.form['email']
        user = methods.select_email_user(email_req)
        if user:
            _id, name, email = user.id, user.name, user.email
            if check_password_hash(user.password, pasw):
                session['user'] = _id
            else:
                errors.append('Пароли не совпадают')
        else:
            errors.append('Такого пользователя не существует')
            return render_template('users/index.html', title='Вход', menu=menu, errors=errors, cls='faild')
        return redirect(url_for('index_app'))
    if request.method == 'GET':
        return render_template('users/index.html', title='Вход', menu=menu)


@users.route('/logout', methods=['POST', 'GET'])
def logout():
    print('Зашли')
    print(session.get("user"))
    session.clear()
    print(session.get("user"))
    return redirect(url_for('.index'))
