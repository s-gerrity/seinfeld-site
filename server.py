"""Server for The Ultimate Seinfeld Experience."""


from flask import (Flask, render_template, request, session)
from model import connect_to_db, Bot, BotResponse
import arrow
import random

app = Flask(__name__)

app.secret_key = "sehn"

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
        session['user_name_key'] = user_name_input
 

    # a variable that holds the username
    user_name_display = session.get('user_name_key', None)
  

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



    ###### BOT NAME / CHAR SELECTION ####################
    bot_char = request.args.get("character-bot")

    # upon first load, None is the char. Save all 
    # selections after that to a session
    if bot_char != None:

        session['bot_name_key'] = bot_char

    # save select char as value and show through jinja display
    if bot_char != 'no_selection':

        session['bot_name_key'] = bot_char
        bot_char_display = session['bot_name_key'] 
    
    # save the bot selected to the display
    bot_char_display = session['bot_name_key']

    # show previous selected char
    if 'bot_name_key' not in session:
        session['bot_name_key'] = bot_char_display





    ####### BOT RESPONSE ##########################
    # # # # # ###### IF BOT CHAR DISPLAY IS "NONE" NEED TO RELOAD PAGE AS IS#########

    # create a session value list to collect bot responses
    if 'bot_responses_key' not in session:

        # hold place for bot response
        session['bot_responses_key'] = []

    # if there is a list in session, add a new message to the bot response session
    elif bot_char_display != None:
        # dict for bot character names with matching id to iterate through for query creation
        char_name_id = {"Jerry": 1, "George": 2, "Elaine": 3, "Kramer": 4}
        # to query a random bot response, first pull response options and count total
        count_queries = BotResponse.query.filter(BotResponse.bot_id == char_name_id[bot_char_display]).count()          
        # when querying random responses, offset skips to the random num. Need to 
        # reduce total by 1 
        offset_num = count_queries - 1
        # get a random num between 1 and total options
        rand_num = random.randint(1, offset_num)       
        # query the response option that is the random num (remember that offset skips to the option above)
        bot_response = BotResponse.query.filter(BotResponse.bot_id == char_name_id[bot_char_display]).offset(rand_num).first()
        # add the response to the session
        session['bot_responses_key'].append(str(bot_response))
      

    user_messages = session['user_messages_key']
    bot_responses = session['bot_responses_key']
    
    return render_template('homepage.html',
                            days_left=days_left.days,
                            user_messages=user_messages,
                            user_name=user_name_display,
                            bot_responses=bot_responses,
                            bot_name=bot_char_display
                            )


@app.route('/where-are-they-now')
def where_are_they_now():
    """Loads tweets from Twitter API."""
    


    return render_template('where-are-they-now.html')

if __name__ == '__main__':

    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)