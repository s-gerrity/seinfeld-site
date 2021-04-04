"""Load bot response quotes into the database."""

from model import db, connect_to_db, BotResponse
from server import app




def get_responses():
    """Load response quotes from dataset into database."""

    # need to load all quotes into the db
    with open("data/test_responses.tsv") as response_data:
        for i, line in enumerate(response_data):
            # if i >= 7000: # limit the number of rows read
            #     break
            print(line)
            bot_id,response=(line.split("#"))
            # use split delimiter 
            db.session.add(BotResponse(bot_id=bot_id,response=response))


            print("Aloha")
    db.session.commit()



if __name__ == '__main__':
    connect_to_db(app)
    db.create_all()

    get_responses()