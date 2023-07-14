from flask import Flask, render_template
from werkzeug.security import check_password_hash, generate_password_hash
from modules.utils import read_from_file, write_to_file, generate_pin
from flask import session, redirect, url_for

app = Flask(__name__)
app.secret_key = "super_secret_key"  # Ceci est nécessaire pour utiliser les sessions dans Flask.


def get_user(username):
    users = read_from_file('database/members.txt')
    for user in users:
        if user['username'] == username:
            return user
    return None


def login(request):
    if request.method == 'POST':
        username = request.form.get('username')
        pin = request.form.get('password')  # Change 'pin' to 'password' to match the HTML form
        user = get_user(username)
        if user and pin and check_password_hash(user['pin'], pin):
            session['user'] = user
            return redirect(url_for('home'))
        else:
            return 'Invalid credentials'
    return render_template('login.html')


def register(request):
    if request.method == 'POST':
        username = request.form.get('username')
        user = get_user(username)
        if user:
            return 'Username already exists'
        pin = generate_pin()
        new_user = {
            'username': username,
            'pin': generate_password_hash(pin)
        }
        users = read_from_file('database/members.txt')
        users.append(new_user)
        write_to_file('database/members.txt', users)
        return f'User registered with PIN: {pin}'
    return render_template('register.html')


def logout():
    session.pop('user', None)
    return redirect(url_for('login'))
