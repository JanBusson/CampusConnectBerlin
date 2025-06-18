# ermöglicht durch Erstellen einer Blueprint die Auslagerung der einzelnen Routen
from flask import Blueprint

# BLuepring Objekt main_bp um denen dann Routen zuzuordnen
main_bp = Blueprint('main', __name__)

# Importiert alle Routen
from . import route_login
from . import route_index