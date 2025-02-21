import os
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

from markupsafe import escape

app = Flask(__name__)

# To run this application run the following commands in the terminal:
# > az login
#   Enter credentials for Azure
# > flask run
#   Go to the url that is displayed

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
   app.run()
