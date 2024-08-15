from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField, FileField
from wtforms.fields.choices import SelectField
from wtforms.fields.numeric import FloatField
from wtforms.fields.simple import BooleanField
from wtforms.validators import DataRequired, NumberRange


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


class SneakerForm(FlaskForm):
    name = StringField('Sneaker Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    prize = FloatField('Price', validators=[DataRequired(), NumberRange(min=0)])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    category_id = SelectField('Category', coerce=int, validators=[DataRequired()])
    image = FileField('Image', validators=[DataRequired()])
    submit = SubmitField('Add Sneaker')
