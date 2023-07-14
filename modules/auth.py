from flask import request, render_template
from flask import Flask, render_template, redirect, url_for, session
from werkzeug.security import check_password_hash, generate_password_hash
from utils import read_from_file, write_to_file, generate_pin

app = Flask(__name__)
app.secret_key = "super_secret_key"  # Ceci est nécessaire pour utiliser les sessions dans Flask.


def get_user(username):
    users = read_from_file('database/members.txt')
    for user in users:
        if user['username'] == username:
            return user
    return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        pin = request.form.get('pin')
        user = get_user(username)
        if user and check_password_hash(user['pin'], pin):
            session['user'] = user
            return redirect(url_for('home'))
        else:
            return 'Invalid credentials'
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
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


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))
