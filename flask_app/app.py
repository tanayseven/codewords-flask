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
        if Account().login(request.form['username'], request.form['password']):
            return render_template(
                'home_page.jinja',
                message='Hello! ' + request.form['username'] + ' you have logged in successfully',
            )
        else:
            return render_template(
                'home_page.jinja',
                message='Sorry, invalid login!',
            )


@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.jinja')
    if request.method == 'POST':
        print("Signed up user: " + request.form['username'])
        return render_template('home_page.jinja')


@app.route('/users_list', methods=['GET'])
def users_list():
    account = Account()
    return render_template('users_list.jinja', user_list=account.all_accounts)


if __name__ == "__main__":
    app.run()
