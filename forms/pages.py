from flask_wtf import Form
from wtforms import TextField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class EditPageForm(Form):

    title = TextField('Title', validators=[DataRequired()])
    url = TextField('URL', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])

    submit = SubmitField('Submit', validators=[DataRequired()])


class DelPageForm(Form):
    submit = SubmitField('Delete', validators=[DataRequired()])
