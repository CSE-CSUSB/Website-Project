from flask_wtf import Form
from util.auth import Auth
from wtforms import TextField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired


class EditPageForm(Form):

    title = TextField('Title', validators=[DataRequired()])
    url = TextField('URL', validators=[DataRequired()])

    content = TextAreaField('Content', validators=[DataRequired()])

    level = SelectField('Access Level', choices=[("0", 'Public'), ("1", 'Members'), ("2", 'Officers')])

    navigation = BooleanField('Show in Navigation')

    submit = SubmitField('Submit', validators=[DataRequired()])


class DelPageForm(Form):
    submit = SubmitField('Delete', validators=[DataRequired()])
