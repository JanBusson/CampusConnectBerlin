# ermöglicht durch Erstellen einer Blueprint die Auslagerung der einzelnen Routen
from flask import Blueprint

# Bluepring Objekt um Routen zuzuordnen
main_bp = Blueprint('main', __name__)

# Importiert alle Routen
from . import route_start
from . import route_login
from . import route_register
from . import route_welcome
from . import route_matching
from . import profile_picture
from . import route_quiz
from . import route_quizresult
#from . import route_friend_suggestions
from . import route_my_matches
from . import route_chat
from . import route_chat_room