# coding=utf-8
from flask import Flask, url_for, render_template, redirect, session, request
from flask.ext.assets import Environment, Bundle
from db import *
from forms import LoginForm

app = Flask(__name__)
app.config.from_object('config')
assets_env = Environment(app)

@app.before_request
def before_request():
    'This function called before any request'

def redirect_url(default='index'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_as'):
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # Example
        session['logged_as'] = form.login.data
        session.permanent = form.remember_me.data
        return redirect(url_for('index'))

    return render_template('login-form.html', form=form)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    if app.config['DEBUG_ENABLED']:
        app.run(port=5000, debug=True, host='127.0.0.1')
    else:
        app.run(port=80, debug=False, host='0.0.0.0')
