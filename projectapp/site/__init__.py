from flask import Blueprint
siteobj = Blueprint('bpsite', __name__, template_folder='templates', static_folder='static',url_prefix='/site')

from . import siteroutes