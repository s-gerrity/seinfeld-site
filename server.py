"""Server for The Ultimate Seinfeld Experience."""


from flask import (Flask, render_template, request, session, redirect)
from model import connect_to_db, Bot, BotResponse
import arrow
import random
import sein_twit
import sein_yelp

app = Flask(__name__)

app.secret_key = "sehn"


@app.route ('/')
def homepage():
    """Loads homepage."""

    return render_template('homepage.html')


@app.route('/clear')
def clear():
    """Clears session with 'end convo' button."""

    session.clear()
    return redirect('/')


@app.route('/where-are-they-now')
def where_are_they_now():
    """Loads WATN page & tweets from Twitter API."""

    tweet_screen_name = {'Jerry': 'jerryseinfeld', 
                        'Julia': 'officialjld', 
                        'Jason': 'IJasonAlexander', 
                        'Modern': 'modern_seinfeld'}

    jerry_twitter_handle = sein_twit.get_twitter_handle(tweet_screen_name, 'Jerry')
    jerry_tweet_ids = sein_twit.get_tweet_id(tweet_screen_name, 'Jerry')

    julia_twitter_handle = sein_twit.get_twitter_handle(tweet_screen_name, 'Julia')
    julia_tweet_ids = sein_twit.get_tweet_id(tweet_screen_name, 'Julia')
    
    jason_twitter_handle = sein_twit.get_twitter_handle(tweet_screen_name, 'Jason')
    jason_tweet_ids = sein_twit.get_tweet_id(tweet_screen_name, 'Jason')

    modern_twitter_handle = sein_twit.get_twitter_handle(tweet_screen_name, 'Modern')
    modern_tweet_ids = sein_twit.get_tweet_id(tweet_screen_name, 'Modern')

    return render_template('where-are-they-now.html',
                            jerry_twitter_handle=jerry_twitter_handle,
                            jerry_tweet_ids=jerry_tweet_ids,

                            julia_twitter_handle=julia_twitter_handle,
                            julia_tweet_ids=julia_tweet_ids,

                            jason_twitter_handle=jason_twitter_handle,
                            jason_tweet_ids=jason_tweet_ids,
                            
                            modern_twitter_handle=modern_twitter_handle,
                            modern_tweet_ids=modern_tweet_ids,
                            )


@app.route('/zip-code')
def get_zip_code():
    """Loads search results when user submits a zip code."""

    zip_code_search = request.args.get("zip-code")   
    dict_of_businesses = sein_yelp.get_businesses(zip_code_search)
    
    return render_template('seinfood.html',
                            dict_of_businesses=dict_of_businesses,
                            zip_code_search=zip_code_search,
                    )


@app.route('/food-locator')
def load_seinfood():
    """Loads Seinfeld Food Locator page."""


    return render_template('seinfood.html',
                            )


@app.route('/festivus')
def load_festivus():
    """Loads Festivus countdown page."""

    todays_date = arrow.now('US/Pacific')
    festivus_date = arrow.get(2021, 12, 23)
    days_left = festivus_date - todays_date

    return render_template('festivus.html',
                            days_left=days_left.days,
                            )


@app.route('/character-chat')
def load_character_chat():
    """Loads character chat page & execute conversation."""

    #### USER NAME #################################
    user_name_input = request.args.get("username")

    # if user in session's username is not blank
    if user_name_input != "":
        session['user_name_key'] = user_name_input
 
    user_name_display = session.get('user_name_key', None)

    # if the username wasn't entered, use the previous username
    if 'user_name_key' not in session:
        session['user_name_key'] = user_name_display

    
    ########## USER MESSAGE #######################
    user_message = request.args.get("user-input")

    # start collecting user message input into an empty list 
    if 'user_messages_key' not in session:
        session['user_messages_key'] = []
        session['user_messages_key'].append(user_message)
    else:
        session['user_messages_key'].append(user_message)


    ###### BOT NAME / CHAR SELECTION ####################
    bot_char = request.args.get("character-bot")

    # upon first load, None is the char
    if bot_char != None:
        session['bot_name_key'] = bot_char

    # save select char as value and show through jinja display
    if bot_char != 'no_selection':

        session['bot_name_key'] = bot_char
        bot_char_display = session['bot_name_key'] 
    
    bot_char_display = session['bot_name_key']

    # show previous selected char
    if 'bot_name_key' not in session:
        session['bot_name_key'] = bot_char_display


    ####### BOT RESPONSE ##########################

    # create a session value list to collect bot responses
    if 'bot_responses_key' not in session:
        session['bot_responses_key'] = []

    elif bot_char_display != None:
        char_name_id = {"Jerry": 1, "George": 2, "Elaine": 3, "Kramer": 4}
        # to query a random bot response, first pull response options and count total
        count_queries = BotResponse.query.filter(BotResponse.bot_id == char_name_id[bot_char_display]).count()          
        # when querying random responses, offset skips to the num after. Need to reduce total by 1.
        offset_num = count_queries - 1
        rand_num = random.randint(1, offset_num)       
        bot_response = BotResponse.query.filter(BotResponse.bot_id == char_name_id[bot_char_display]).offset(rand_num).first()
        session['bot_responses_key'].append(str(bot_response))

    user_messages = session['user_messages_key']
    bot_responses = session['bot_responses_key']

    return render_template('character_chat.html',
                            user_messages=user_messages,
                            user_name=user_name_display,
                            bot_responses=bot_responses,
                            bot_name=bot_char_display,
                            )


if __name__ == '__main__':

    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)