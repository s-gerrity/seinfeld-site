"""Load bot response quotes into the database."""

from model import db, connect_to_db, BotResponse, Seinfood, Bot
from server import app


def make_bots():
    """Create bots with names for the database."""

    bot_name_list = ['jerry_bot', 
                 'george_bot', 
                 'elaine_bot', 
                 'kramer_bot']

    for i in range(len(bot_name_list)):

        bot_to_make = bot_name_list[i]
        bot_creation = Bot(bot_name=bot_to_make)
        db.session.add(bot_creation)
            
    db.session.commit()


def get_responses():
    """Load response quotes from dataset into database."""

    with open("data/bot_responses.tsv") as response_data:
        for i, line in enumerate(response_data):
            # if i >= 7000: # limit the number of rows read
            #     break
            bot_id,response=(line.split("#"))
            db.session.add(BotResponse(bot_id=bot_id,
                                      response=response)
                                      )
    db.session.commit()


def import_food_categories():
    """Load food search categories for Food Locator into the database."""

    with open("data/food_categories.tsv") as category_data:
        for i, line in enumerate(category_data):

            food_category,category_active=(line.split("#"))
            # convert type from str to int (1 = True, 0 = False)
            category_active = int(category_active)
            db.session.add(Seinfood(food_category=food_category,
                                    category_active=category_active)
                                    )
    db.session.commit()


if __name__ == '__main__':
    connect_to_db(app)
    db.create_all()

    make_bots()
    get_responses()
    import_food_categories()