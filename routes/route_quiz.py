from flask import render_template
from . import main_bp


@main_bp.route('/quiz')
def quiz():
    return render_template('quiz.html')