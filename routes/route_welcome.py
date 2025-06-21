from flask import render_template
from . import main_bp

@main_bp.route('/welcome/<int:id>')
def welcome():
    #parameter temporär
    return render_template('welcome.html')