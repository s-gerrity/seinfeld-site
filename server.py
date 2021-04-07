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
    print(user_name_input, user_name_input is None)
    if user_name_input != "":

        # assign their username as the value in session
        session['user_name_key'] = user_name_input
 

    # a variable that holds the username
    user_name_display = session['user_name_key']
  

    # if the username wasn't entered, use the previous username
    if 'user_name_key' not in session:
        session['user_name_key'] = user_name_display

    
    ########## USER MESSAGE #######################
    user_message = request.args.get("user-input")

    # start collecting user message input into an empty list 
    # value and always append into the list (value)
    if 'user_messages_key' not in session:
        session['user_messages_key'] = []
        session['user_messages_key'].append(user_message)

    # if there are messages in session, add them to the users value
    else:
        session['user_messages_key'].append(user_message)


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
                #{% for username in session %}
    ###### BOT NAME / CHAR SELECTION ####################
    bot_char = request.args.get("character-bot")
    
    # hold place for bot response
    bot_response = ""

    # upon first load, None is the char. Save all 
    # selections after that to a session
    if bot_char != None:

        session['bot_name_key'] = bot_char

    # Must save select char as value and show through jinja display
    if bot_char != 'no_selection':

        session['bot_name_key'] = bot_char
        bot_char_display = session['bot_name_key'] 
    
    # save the bot selected to the display
    bot_char_display = session['bot_name_key']
    

    # print("HELLO")
    # print(bot_char) # when loading for the first time: None
    # print(session) # first time all: None

    # show previous selected char
    if 'bot_name_key' not in session:
        session['bot_name_key'] = bot_char_display

    # show this upon first load
    if bot_char == None:

        bot_char_display = f"Pick a character"



    ####### BOT RESPONSE ##########################
    print("ALOHA")
    # print(bot_char) # first time: None
    # print(bot_char_display) # first time: None
    print(session)

    
    if bot_char == "Jerry":
        # queries all jerry quotes from db
        f_jerry = BotResponse.query.filter(BotResponse.bot_id == 1).first()

        # count the quote rows
        # count_f_jerry = int(f_jerry.count(f_jerry))

        # choose a randon jerry response from the db
        bot_response = f_jerry
        # f_jerry(int(count_f_jerry*random.random())).first()
        # bot_response = f_jerry.response

    elif bot_char == 'George':
        f_george = BotResponse.query.filter(BotResponse.bot_id == 2).first()
        bot_response = f_george


    
    # session['botname'] = bot_name
    # session['botresponse'] = bot_response
    # print('POSTBOT', session)
    # for key, value in session.items():
    #     if key == 'usermessage':
    #         for value in value:
    #             user_message_loop = value
    # user_message_loop

    user_messages = session['user_messages_key']
    bot_responses = [str(bot_response) + str(i) for i in range(0, len(user_messages))]

    return render_template('homepage.html',
                            days_left=days_left.days,
                            user_messages=user_messages,
                            user_name=user_name_display,
                            bot_responses=bot_responses,
                            bot_name=bot_char_display
                            )

#<p id="user-message">{{ user_name }}: {{ message }}</p><br>
#<p id="bot-message">{{ bot_name }}: {{ bot_message }}</p><br>

if __name__ == '__main__':

    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)