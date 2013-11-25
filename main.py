# coding=utf-8
from flask import Flask, url_for, render_template, redirect, session, request, jsonify, flash
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)
app.config.from_object('config')
assets_env = Environment(app)

from db import *
from forms import LoginForm

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
        user = User.query.filter_by(username=form.login.data, password=get_password_hash(form.password.data)).first()
        if not user:
            flash(u'Неверный логин или пароль')
            return render_template('login-form.html', form=form)
        # Example
        session['logged_as'] = form.login.data
        session.permanent = form.remember_me.data
        return redirect(url_for('index'))

    return render_template('login-form.html', form=form)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')