"""Server for The Ultimate Seinfeld Experience."""

# Don't need Flask just yet
# from flask import (Flask, render_template, request)
from model import connect_to_db

app = Flask(__name__)
# What is the app secret key? Do I need it?
# app.secret_key = "dev"


@app.route ('/')
def homepage():
    """Go to homepage."""

    return render_template('homepage.html')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)