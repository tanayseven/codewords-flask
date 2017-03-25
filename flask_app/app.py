from flask import Flask, render_template, request
from flask_injector import FlaskInjector

import sys

from injector import inject, Injector, Module

sys.path.append('./')
from flask_app.account import Account
from flask_app.interfaces import AccountRepo
from flask_app.repos import AccountRepository

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
@inject(account_repo=AccountRepo)
def users_list(account_repo):
    accounts = account_repo.get_all_account()
    return render_template('users_list.jinja', user_list=accounts)


class DevModule(Module):
    def configure(self, binder):
        binder.bind(
            AccountRepo,
            to=AccountRepository,
            scope=request,
        )


injector = Injector(DevModule)
FlaskInjector(app=app, injector=injector)

if __name__ == "__main__":
    app.run()
