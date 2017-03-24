from flask import Flask, render_template, request

import sys
sys.path.append('./')
from flask_app.account import Account
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home_page.jinja')


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.jinja')
    if request.method == 'POST':
        print("Logged in user: " + request.form['username'])
        return render_template('home_page.jinja')


@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.jinja')
    if request.method == 'POST':
        print("Signed up user: " + request.form['username'])
        return render_template('home_page.jinja')


@app.route('/users_list', methods=['GET'])
def users_list():
    return render_template('users_list.jinja', user_list=[Account(user_name='tanay'), Account(user_name='tushar')])


if __name__ == "__main__":
    app.run()
