import os
import secrets

from flask import (Flask, render_template, send_from_directory, redirect, url_for, request)
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from markupsafe import escape

# To run this application run the following commands in the terminal:
# > az login
#   Enter credentials for Azure
# > flask run
#   Go to the url that is displayed

app = Flask(__name__)

secret_key = secrets.token_hex(16)
print(secret_key)

app.secret_key = secret_key
login_manager = LoginManager()
login_manager.init_app(app)

# Create a user class
class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        user = User(user_id)
        login_user(user)
        return redirect(url_for('protected'))
    return render_template('login.html')

@app.route('/protected')
@login_required
def protected():
   print(f'Hello, {current_user.id}! You are logged in.')
   return render_template('index.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/BusinessPlanForm', methods=['POST'])
def BusinessPlanForm():
   print('Request for Business Plan page received')
   return render_template('Executive Summary.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
   app.run()
