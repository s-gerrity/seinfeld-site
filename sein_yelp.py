import os
import requests
from model import connect_to_db


# define the API key, define the endpoint, define the header
YELP_API_KEY = os.environ.get('YELP_API_KEY')
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % YELP_API_KEY}

# define parameters
PARAMETERS = {'term': 'chinese restaurant',
              'limit': 10,
              'radius': 10000,
              'location': '94609'}

# make a request to the yelp api
response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)

# convert the json string into a dictionary
business_data = response.json()

print(business_data)
