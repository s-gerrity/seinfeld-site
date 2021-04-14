import os
import requests
from model import connect_to_db


# define the API key, define the endpoint, define the header
YELP_API_KEY = os.environ.get('YELP_API_KEY')
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % YELP_API_KEY}

# # define parameters
# PARAMETERS = {'term': 'good food',
#               'limit': 5,
#               'radius': 10000,
#               'categories': 'chinese',
#               'location': '94609'}

# make a request to the yelp api
# response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)

# # convert the json string into a dictionary
# business_data = response.json()

# #print(business_data.keys())

# for biz in business_data['businesses']:
#     print(biz['name'])

# Make functions for each seinfood category that returns 1 results
# or make one function that searches for each category one by one
# and adds the business to a list
# function called in server.py and jinja template loops through each option

def get_businesses():
    """Query Yelp API for businesses according to search parameters."""
    
    food_list = ['chinese', 'soup', 'babka']
    business_list = []

    for food in food_list:
        parameters = {'term': food,
                      'limit': 1,
                      'radius': 20000,
                    #   'categories': food, 
                      'location': '94609'}
        response = requests.get(url = ENDPOINT, 
                                params = parameters, 
                                headers = HEADERS)
        business_data = response.json()
        for biz in business_data['businesses']:
            biz['name']
            business_list.append(biz['location']['display_address'])

    return business_list