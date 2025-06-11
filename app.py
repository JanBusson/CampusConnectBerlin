#für Render Template müssen noch alle notwendigen Templates erstellt werden
from flask import Flask, render_template

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
def register():
    return 'Register Screen'

#Find Match Page
@app.route('/findMatch')
def findMatch():
    return 'Find Match'

#Matches Page
@app.route('/Matches')
def matches():
    return 'My Matches'

#Error handling
@app.errorhandler(404)
def http_not_found(e):
    return '404'

@app.errorhandler(500)
def http_internal_server_error(e):
    return '500'