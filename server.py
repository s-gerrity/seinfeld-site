"""Server for The Ultimate Seinfeld Experience."""


from flask import (Flask, render_template, request)
from model import connect_to_db
import arrow

app = Flask(__name__)


@app.route ('/')
def homepage():
    """Go to homepage. Loads countdown to Festivus."""

    todays_date = arrow.now('US/Pacific')
    festivus_date = arrow.get(2021, 12, 23)
    days_left = festivus_date - todays_date
    
    return render_template('homepage.html',
                            days_left=days_left.days)



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)