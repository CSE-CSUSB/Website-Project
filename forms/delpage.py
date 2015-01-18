from flask_wtf import Form
from wtforms import SubmitField
from wtforms.validators import DataRequired


class DelPageForm(Form):
    submit = SubmitField('Delete', validators=[DataRequired()])
