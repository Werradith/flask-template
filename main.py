# coding=utf-8
from flask import Flask, url_for, render_template, redirect, session, request, jsonify, flash
from flask.ext.assets import Environment, Bundle
from flask.ext.babel import Babel
from datetime import datetime

app = Flask(__name__)
app.config.from_object('config')
assets_env = Environment(app)
babel = Babel(app) # TODO: Localization

from db import *
from forms import LoginForm, RegisterForm

@app.before_request
def before_request():
    'This function called before any request'

def redirect_url(default='index'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('logged_as'):
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.login.data).count():
            flash('User with this name already exists')
            return render_template('register.html', form=form)
        elif User.query.filter_by(email=form.email.data).count():
            flash('User with this e-mail address already exists')
            return render_template('register.html', form=form)
        user = User(username=form.login.data, password=get_password_hash(form.password.data), email=form.email.data, register_date = datetime.now(), register_ip=request.remote_addr)
        db.session.add(user)
        db.session.commit()
        session['logged_as'] = user.username
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_as'):
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        from sqlalchemy import or_
        user = User.query.filter(or_(User.username == form.login.data, User.email == form.login.data), User.password == get_password_hash(form.password.data)).first()
        if not user:
            flash('Invalid login or password')
            return render_template('login-form.html', form=form)
        # Example
        session['logged_as'] = user.username
        session.permanent = form.remember_me.data
        try:
            user.last_ip = request.remote_addr
            user.last_login = datetime.now()
            db.session.add(user)
            db.session.commit()
        except AssertionError:
            pass
        return redirect(url_for('index'))

    return render_template('login-form.html', form=form)

@app.route('/logout')
def logout():
    session['logged_as'] = None
    return redirect(redirect_url())

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')