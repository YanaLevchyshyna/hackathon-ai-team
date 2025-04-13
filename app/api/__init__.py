from flask import Blueprint

main = Blueprint('main', __name__, template_folder='templates')
from app.api import routes  # to avoid circular imports

