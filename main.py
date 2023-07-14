from flask import Flask, render_template, request
from modules.auth import login, register, logout
from modules.members import get_members, add_member
from modules.contributions import get_contributions, add_contribution

app = Flask(__name__)
app.secret_key = "super_secret_key"  # Ceci est nécessaire pour utiliser les sessions dans Flask.


@app.route('/login', methods=['GET', 'POST'])
def login_route():
    return login(request)


@app.route('/register', methods=['GET', 'POST'])
def register_route():
    return register(request)


@app.route('/logout')
def logout_route():
    return logout()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/members', methods=['GET', 'POST'])
def members_route():
    if request.method == 'POST':
        return add_member()
    return get_members()


@app.route('/contributions', methods=['GET', 'POST'])
def contributions_route():
    if request.method == 'POST':
        return add_contribution()
    return get_contributions()


@app.route('/overview')
def overview_route():
    return render_template('overview.html')


if __name__ == "__main__":
    app.run(debug=True)
