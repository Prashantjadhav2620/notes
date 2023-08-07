from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    # user = get_logged_in_user()
    return render_template('home.html')





