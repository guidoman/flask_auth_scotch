# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

# @main.route('/')
# def index():
#     return render_template('index.html')

@main.route('/')
@login_required
def profile():
    return render_template('profile.html', name=current_user.username)


if __name__ == '__main__':
    from project import create_app
    app = create_app()
    app.run(port=3333, debug=True)