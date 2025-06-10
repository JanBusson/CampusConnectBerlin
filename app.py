from flask import Flask

app = Flask(__name__)

#Start page
@app.route('/')
def index():
    return 'Start Window!'

#Login page
@app.route('/login')
def login():
    return 'Login Screen'

#Register page
@app.route('/register')
def login():
    return 'Register Screen'