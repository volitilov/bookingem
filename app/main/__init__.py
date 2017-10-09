from flask import Blueprint
from ..models import User

main = Blueprint('main', __name__)

from . import forms, views