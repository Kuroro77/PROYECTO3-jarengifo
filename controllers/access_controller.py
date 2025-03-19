from config.auth import login_manager
from flask import Blueprint, render_template, request
from models.usuarios import Usuarios
from flask_login import current_user, logout_user, login_user

home_blueprint = Blueprint("home", __name__)
@login_manager.user_loader
def load_user(user_id:int):
    return Usuarios.query.get(int(user_id))

@home_blueprint.route('/')
def login():
    return render_template('access/login.html')
@home_blueprint.route('/auth', methods=['POST'])
def auth():
    username = request.form.get("username")
    password = request.form.get("password")

    user = Usuarios.auth(username, password)

    if user:
        login_user(user)
        return render_template('access/bienvenida.html', current_user=current_user)
    else:
        return render_template('access/404.html')

@home_blueprint.route('/logout')
def logout():
    logout_user()
    return render_template('access/login.html')