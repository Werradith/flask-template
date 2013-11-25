# coding=utf-8
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, TextAreaField, FileField, HiddenField, BooleanField, SelectField, SubmitField
from flask.ext.wtf.recaptcha import RecaptchaField
from wtforms.validators import Required, Length

class LoginForm(Form):
    login = TextField('login', validators=[Required()])
    password = PasswordField('password', validators=[Required()])
    remember_me = BooleanField('remember-me')
    #captcha = RecaptchaField()
    commit = SubmitField('commit')
    captcha = RecaptchaField()