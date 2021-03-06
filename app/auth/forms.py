# -*- coding: utf-8 -*-
__author__ = 'wangting'

from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Email, Required, Length


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])

    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
