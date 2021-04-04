"""Server for The Ultimate Seinfeld Experience."""


from flask import (Flask, render_template, request, flash)
from model import connect_to_db, Bot, BotResponse
import arrow
import crud
import random

app = Flask(__name__)

app.secret_key = "sein"

@app.route ('/')
def homepage():
    """Loads countdown to Festivus."""

    todays_date = arrow.now('US/Pacific')
    festivus_date = arrow.get(2021, 12, 23)
    days_left = festivus_date - todays_date
    
    user_message = request.args.get("user-input")
    user_name = request.args.get("username")

    bot_char = request.args.get("character-bot")
    

    
    if bot_char == "jerry":
        f_jerry = BotResponse.query.filter(BotResponse.bot_id == 1).first()
        bot_response = f_jerry.response
    # elif bot_char == "george":
    #     f_george = BotResponse.query.filter(BotResponse.bot_id == 2).first()
    #     bot_response = f_george.response
    # elif bot_char == "no_selection":
    #     bot_response = " "
    #     flash("Please select a character")
    
    return render_template('homepage.html',
                            days_left=days_left.days,
                            message=user_message,
                            username=user_name,
                            bot_message=bot_response
                            )

    # PSUEDOCODE ####################
    # if user-input submit is clicked
    #      print/append via jinja the username and input
    #             always return user-input with a bot response


# saved for crud querying
# query = crud.find_jerry_bot(jerry)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)