"""CRUD operations."""

from model import *

def find_jerry_bot(jerry):

    return BotResponse.query.filter(BotResponse.bot_id == 1).first()



