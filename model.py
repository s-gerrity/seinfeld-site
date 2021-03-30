"""Models for HB Project: Seinfeld Fan Site"""

from flask_sqlalchemy import flask_sqlalchemy

db = SQLAlchemy()

# route needs to be defined. XXXX placeholder. 
def connect_to_db(flask_app, db_uri='postgresql:///XXXX', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

class Bot():
    """Bot table class."""

    __tablename__ = 'bots'

    id = db.Column(db.Integer,
                   autoincrement=True,
                   primary_key=True)
    bot_name = db.Column(db.String)

    def __repr__(self):
            return f'<Bot id={self.id} bot_name={self.bot_name} I thought it was a booger but its snot.>'

class BotResponse():
    """Bot Responses table class."""

    __tablename__ = 'bot_responses'

    response_id = db.Column(db.Integer,
                    autoincrement=True,
                    primary_key=True)
    bot_id = db.Column(db.Integer,
                    db.ForeignKey('Bot.id'))
    response = db.Column(db.String)

    def __repr__(self):
                return f'<bot_response id={self.response_id}> '  

#db.create_all() is to create all the tables with the details above in python class
#caution: check to see if the variable will return a list or an actual string

if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)