"""Models for The Ultimate Seinfeld Experience."""

from flask_sqlalchemy import SQLAlchemy
import arrow

db = SQLAlchemy()

def connect_to_db(flask_app, db_uri='postgresql:///ultimate', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

class Bot(db.Model):
    """Bot table class."""

    __tablename__ = 'bots'

    id = db.Column(db.Integer,
                   autoincrement=True,
                   primary_key=True)
    bot_name = db.Column(db.String)

    def __init__(self, bot_name):
        """Create a bot."""

        self.bot_name = bot_name
 

    def __repr__(self):
        return f'<Bot id={self.id} bot_name={self.bot_name} These pretzels are makin me thirsty.>'

class BotResponse(db.Model):
    """Bot Responses table class."""

    __tablename__ = 'bot_responses'

    response_id = db.Column(db.Integer,
                    autoincrement=True,
                    primary_key=True)
    bot_id = db.Column(db.Integer,
                    db.ForeignKey('bots.id'))
    response = db.Column(db.String)


    bot = db.relationship('Bot', backref='bot_responses')


    def __init__(self, bot_id, response):
        """Create a response."""

        self.bot_id = bot_id
        self.response = response



    def __repr__(self):
        return f'{self.response}'  


class Seinfood(db.Model):
    """Food Locator table class."""

    __tablename__ = 'seinfoods'

    seinfood_id = db.Column(db.Integer,
                            autoincrement= True,
                            primary_key=True)
    food_category = db.Column(db.String)
    category_active = db.Column(db.Boolean)


    def __init__(self, food_category, category_active):
        """Create a food search category."""

        self.food_category = food_category
        self.category_active = category_active


    def __repr__(self):
        return f'<{self.food_category}> Active? <{self.category_active}>' 




if __name__ == '__main__':
    from server import app
    
    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.
    # db.create_all() is to create all the tables with the details above in python class
    # caution: check to see if the variable will return a list or an actual string

    connect_to_db(app)
    db.create_all()
