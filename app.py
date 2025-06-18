#für Render Template müssen noch alle notwendigen Templates erstellt werden
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from routes import main_bp

app = Flask(__name__)

app.config.from_mapping(
    #Noch nich timplementiert
    SECRET_KEY = 'secret_key_just_for_dev_environment',
    #DATABASE = os.path.join(app.instance_path, 'todos.sqlite'),
    BOOTSTRAP_BOOTSWATCH_THEME = 'pulse'  # (2.)
)

bootstrap = Bootstrap5(app)

# Blueprint registrieren
app.register_blueprint(main_bp)


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

if __name__ == '__main__':
    app.run(debug=True)