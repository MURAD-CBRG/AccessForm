from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class AccessForm(FlaskForm):
    astro_id = StringField('ID астронавта', validators=[DataRequired()])
    astro_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    captain_id = StringField('ID капитана', validators=[DataRequired()])
    captain_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Отправить данные')
