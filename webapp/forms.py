from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Отправить')

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя',validators=[DataRequired()],
          render_kw={"class": "form-control"})  
    password = PasswordField('Пароль',validators=[DataRequired()],
          render_kw={"class": "form-control"})
    submit = SubmitField('Отправить',render_kw={"class":"btn btn-primary"})


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
