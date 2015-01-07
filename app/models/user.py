from flask import Flask

app = Flask(__name__)
app.debug = True
app.secret_key = '1234567890'

@app.route("/")

def hello():
    """docstring for hello"""
    return render_template('index.html') 
    
