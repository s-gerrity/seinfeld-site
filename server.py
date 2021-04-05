"""Server for The Ultimate Seinfeld Experience."""


from flask import (Flask, render_template, request, session)
from model import connect_to_db, Bot, BotResponse
import arrow
import crud
import random

app = Flask(__name__)

app.secret_key = "sein"

@app.route ('/')
def homepage():
    """Loads Festivus countdown + bot chat."""


    ########## Festivus countdown #################
    todays_date = arrow.now('US/Pacific')
    festivus_date = arrow.get(2021, 12, 23)
    days_left = festivus_date - todays_date

    
    ########## Bot chat ###########################
    #### USER NAME #################################
    user_name_input = request.args.get("username")

    # if user in session's username is not blank
    if user_name_input != "":

        # assign their username as the value in session
        session['username'] = user_name_input
 

    # a variable that holds the username
    user_name_display = session['username']
  

    # if the username wasn't entered, use the previous username
    if 'username' not in session:
        session['username'] = user_name_display


    ########## USER MESSAGE #######################
    user_message = request.args.get("user-input")

    # start collecting user message input into an empty list 
    # value and always append into the list (value)
    if 'usermessage' not in session:
        session['usermessage'] = []
        session['usermessage'].append(user_message)

    # if there are messages in session, add them to the users value
    else:
        session['usermessage'].append(user_message)


    '''
    dictionary must do this
    1) get typed user name
    2) get what the user said
    3) get the bot user name
    4) get the bot response
    5) multiple messsages
    USERNAME : one of these (bob, robert, bobert, maria)
    BOTNAME : jerry george, elaine, kramer
    USERSAIDS: "Im a user" "serious"
    BOTRESPONSE:

    SESSION = {
        "USERNAME": "bob",
        "BOTNAME": "jerry",
        "jerry" : ["imabot", "and my name is jerry"]
    }
    '''

    ###### BOT NAME / CHAR SELECTION ####################
    bot_char = request.args.get("character-bot")

    # add bot character selected to session
    session['botname'] = bot_char

    # save the bot selected to the display
    bot_char_display = session['botname']


    if bot_char in session == 'no_selection':
        session['botname'] = bot_char_display

    
    # if jerry is selected, query a response from db
    if bot_char == "jerry":
        f_jerry = BotResponse.query.filter(BotResponse.bot_id == 1).first()
        
        # bot_name = "Jerry"
        bot_response = f_jerry.response

    # elif bot_char == "george":
    #     f_george = BotResponse.query.filter(BotResponse.bot_id == 2).first()

    #     bot_response = f"George: " + f_george.response

    # elif bot_char == "elaine":
    #     f_elaine = BotResponse.query.filter(BotResponse.bot_id == 2).first()
    #     bot_response = f"Elaine: " + f_elaine.response

    # elif bot_char == "kramer":
    #     f_kramer = BotResponse.query.filter(BotResponse.bot_id == 2).first()
    #     bot_response = f"Kramer: " + f_kramer.response
        

    elif bot_char == None:
        bot_response = " "
        # needs a bot name
        # bot_name = "jerry"
        # flash messages are not working, but site runs fine without it
        f"Please select a character"

    # elif bot_char == "no_selection":
    #     bot_response = " "
    #     # needs a bot name
    #     bot_name = "jerry"
    #     # flash messages are not working, but site runs fine without it
    #     f"Please select a character"
    
    # session['botname'] = bot_name
    # session['botresponse'] = bot_response
    # print('POSTBOT', session)


    return render_template('homepage.html',
                            days_left=days_left.days,
                            message=user_message,
                            user_name=user_name_display,
                            bot_message=bot_response,
                            bot_name=bot_char_display
                            )


if __name__ == '__main__':

    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)