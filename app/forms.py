from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField
from wtforms.fields.simple import BooleanField


class SignUpForm(FlaskForm):
    nickname = StringField("Nickname", validators=[validators.DataRequired()])
    email = StringField("email", validators=[
        validators.DataRequired(),
        validators.Email()
    ])
    password = PasswordField("password", validators=[
        validators.DataRequired(),
        validators.Length(min=4),
        ])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    nickname = StringField("Nickname", validators=[validators.DataRequired()])
    password = PasswordField("password", validators=[
        validators.DataRequired(),
        validators.Length(min=4),
        ])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField("Login")