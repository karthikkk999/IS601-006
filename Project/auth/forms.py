from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, Email, InputRequired, EqualTo, Length, Optional, Regexp

class RegisterForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(2, 30)])
    email = EmailField("email", validators=[DataRequired(), Email()])
    # password = PasswordField("password", validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField("confirm", validators=[DataRequired()])
    submit = SubmitField("Register")
    password = PasswordField("password", 
                             validators=[InputRequired(), Length(min=8), 
                             Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$', 
                             message='Password must contain at least one uppercase letter, one lowercase letter and one digit')])


class LoginForm(FlaskForm):
    email = StringField("email or username", validators=[DataRequired()]) #EmailField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[InputRequired()])
    submit = SubmitField("Login")

class ProfileForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(2, 30)])
    email = EmailField("email", validators=[DataRequired(), Email()])
    current_password = PasswordField("current password", validators=[Optional()])
    password = PasswordField("password", validators=[Optional(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField("confirm", validators=[Optional(), EqualTo("password")])
    submit = SubmitField("Update")