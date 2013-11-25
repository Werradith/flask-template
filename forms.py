# coding=utf-8
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, TextAreaField, FileField, HiddenField, BooleanField, SelectField, SubmitField
from flask.ext.wtf.recaptcha import RecaptchaField
from wtforms.validators import Required, Length, Email, Regexp

class LoginForm(Form):
    login = TextField('login', validators=[Required(), Length(min=3, max=30), Regexp(r'[\w]*')])
    password = PasswordField('password', validators=[Required(), Length(min=6)])
    remember_me = BooleanField('remember-me')
    commit = SubmitField('commit')
    captcha = RecaptchaField()

class RegisterForm(LoginForm):
    email = TextField('email', validators=[Required(), Length(max=70), Email()])
