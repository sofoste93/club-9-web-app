from flask import Flask, render_template, request
from modules.auth import login, register
from modules.members import get_members, add_member
from modules.contributions import get_contributions, add_contribution

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login_route():
    return login()


@app.route('/register', methods=['GET', 'POST'])
def register_route():
    return register()


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
