#für Render Template müssen noch alle notwendigen Templates erstellt werden
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from routes import main_bp
from db import db, create_tables
from models import *

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    SQLALCHEMY_DATABASE_URI='sqlite:///campusconnect_berlin.sqlite',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db.init_app(app)
create_tables(app)

bootstrap = Bootstrap5(app)

# Blueprint registrieren
app.register_blueprint(main_bp)


#Login page
@app.route('/login')
def login():
    return 'Login Screen'

#Register page
@app.route('/register')
def register():
    return render_template('register.html')

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
    return render_template('404.html'), 404

@app.errorhandler(500)
def http_internal_server_error(e):
    return render_template('500.html'), 500