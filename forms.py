from flask_wtf import FlaskForm
from wtforms.fields import (StringField, PasswordField, IntegerField,
                            SelectField, TextAreaField, SubmitField)
from wtforms.validators import DataRequired, Length, EqualTo
from flask_wtf.file import FileField, FileAllowed

class RegisterForm(FlaskForm):
    username = StringField("Enter Username", validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField("Enter Password", validators=[DataRequired(), Length(min=6, max=24)])
    confirm_password = PasswordField("Confirm Password", validators=[
        DataRequired(),
        EqualTo("password", message="Passwords must match!")
    ])
    register = SubmitField("Register")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    login = SubmitField("Log In")

class ChampionshipForm(FlaskForm):
    title = StringField("Championship Title", validators=[DataRequired()])
    sport = SelectField("Sport Category", choices=[
        ('football', 'Football'),
        ('basketball', 'Basketball'),
        ('tennis', 'Tennis')
    ], validators=[DataRequired()])
    year = IntegerField("Year Held", validators=[DataRequired()])
    winner = StringField("Tournament Winner", validators=[DataRequired()])
    runner_up = StringField("Runner-up", validators=[DataRequired()])
    team1 = StringField("Finalist Team 1", validators=[DataRequired()])
    team2 = StringField("Finalist Team 2", validators=[DataRequired()])
    final_score = StringField("Final Score Line", validators=[DataRequired()])
    semi_final_1 = StringField("Semi Final 1 Details", validators=[DataRequired()])
    semi_final_2 = StringField("Semi Final 2 Details", validators=[DataRequired()])
    description = TextAreaField("Brief Summary Description", validators=[DataRequired()])
    image = FileField("Upload Cover Image", validators=[
        FileAllowed(['jpg', 'jpeg', 'png'], 'Only .jpg, .jpeg, and .png files are allowed!')
    ])
    submit = SubmitField("Save Championship")