# coding=utf-8
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, FileField, HiddenField, BooleanField, SelectField, SubmitField
from flask.ext.wtf.recaptcha import RecaptchaField
from wtforms.validators import Required, Length
from config import RANDOM_SETS

#class SampleForm(Form):
#	text = TextField('text', validators=[Required()])
#	captcha = RecaptchaField()