from flask import Blueprint
from ..models import User
from ..email import send_email


auth = Blueprint('auth', __name__)

from . import views, forms