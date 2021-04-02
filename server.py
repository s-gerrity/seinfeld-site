"""Server for The Ultimate Seinfeld Experience."""


from flask import (Flask, render_template, request)
from model import connect_to_db
import arrow

app = Flask(__name__)


@app.route ('/')
def homepage():
    """Loads countdown to Festivus."""

    todays_date = arrow.now('US/Pacific')
    festivus_date = arrow.get(2021, 12, 23)
    days_left = festivus_date - todays_date
    
    user_message = request.args.get("user-input")
    user_name = request.args.get("username")
    
    print("Aloha")
    
    return render_template('homepage.html',
                            days_left=days_left.days,
                            message=user_message,
                            username=user_name,
                            )
    # PSUEDOCODE ####################
    # if user-input submit is clicked
    #     then callback function that does:
    #         print/append via jinja the username and input
    #             always return user-input with a bot response


# @app.route ('/')
# def userMessage():
#     """Print username and their messages on homepage."""

#     user_message = request.args.get("user-input")
#     user_name = request.args.get("username")

#     # has never printed anything at all
#     return render_template('homepage.html',
#                             message=user_message,
#                             username=user_name,
                            
#                             )


# when a user submits a textarea input on homepage
# def open_seinfeld_quotes(filename):
#     """Access quotes from a csv file."""

#     file = open(filename)
#     read_file = file.read()





if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)