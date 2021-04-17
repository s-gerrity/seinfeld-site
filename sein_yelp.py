"""Yelp API connection & queries."""

import os
import requests
from model import connect_to_db, Seinfood
from flask_sqlalchemy import SQLAlchemy
from server import get_zip_code

db = SQLAlchemy()

YELP_API_KEY = os.environ.get('YELP_API_KEY')
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % YELP_API_KEY}


def get_businesses(zip_code_search):
    """Query Yelp API for businesses according to search parameters."""
    
    food_query = db.session.query(Seinfood.food_category)
    food_list = food_query.filter(Seinfood.category_active == True).all()

    business_dict = {}
    # business_url = []

    for item in food_list:
        # calibrating search terms; limit 1 for 1 each search term; can adjust categories.
        # categories can have multiple arguments (comma no space) but businesses will contain all args. 
        # Ex: categories: chinese,bar -- result will look for places that are both chinese and have a bar.

        parameters = {'term': item,
                      'limit': 1,
                      'radius': 20000,
                      'categories': 'food', 
                      'location': zip_code_search,
                      }
        response = requests.get(url = ENDPOINT, 
                                params = parameters, 
                                headers = HEADERS)
        business_data = response.json()

        # key into businesses (other keys 'total' and 'region')
        for biz in business_data['businesses']:
            str_plus_str = []
            str_plus_str.append(biz['name'])
            str_plus_str.append(biz['location']['display_address'])
            new_list = []
            for place in str_plus_str:
                new_list.append(place)

            business_dict[item] = new_list
            # business_url.append(biz['url'])

    return business_dict

if __name__ == '__main__':
    from server import app
    connect_to_db(app)