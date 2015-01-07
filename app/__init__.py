from flask import Flask
from flask import render_template
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.debug = True
app.secret_key = '1234567890'

class MyForm(Form):
    name = StringField('Username', validators=[DataRequired()]) 
    password= StringField('Password', validators=[DataRequired()])

@app.route('/')
@app.route('/templates')
def index():
    form = MyForm()
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()
    
