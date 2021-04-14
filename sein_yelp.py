import os
import requests
from model import connect_to_db


# define the API key, define the endpoint, define the header
YELP_API_KEY = os.environ.get('YELP_API_KEY')
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % YELP_API_KEY}


def get_businesses():
    """Query Yelp API for businesses according to search parameters."""
    
    # list of searches for the parameters to loop through
    food_list = ['chinese restaurant', 
                 'soup restaurant', 
                 'babka', 
                 'diner', 
                 'produce market', 
                 'calzone', 
                 'muffin', 
                 'pakistani restaurant', 
                 'marble rye']
    # dict to send the data to render template
    business_dict = {}

    for item in food_list:
        # calibrating search terms; limit 1 for 1 each search term; can adjust categories.
        # categories can have multiple arguments (comma no space) but businesses will contain all args. 
        # Ex: categories: chinese,bar -- result will look for places that are both chinese and have a bar.
        parameters = {'term': item,
                      'limit': 1,
                      'radius': 20000,
                      'categories': 'food', 
                      'location': '94609'}
        response = requests.get(url = ENDPOINT, 
                                params = parameters, 
                                headers = HEADERS)
        business_data = response.json()
        # key into businesses (other keys 'total' and 'region')
        for biz in business_data['businesses']:
            # add business name and address to dict
            business_dict[biz['name']] = biz['location']['display_address']

    return business_dict