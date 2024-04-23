"""Working with API's (Applied Programming Interface)
https://alissa-huskey.github.io/python-class/lessons/web-apis.html  """

from pprint import pprint
import requests 
from private import LAT, LNG, OPENUV_KEY


def request_demo():
    """Explore how web request works"""
    url = "https://raw.githubusercontent.com/alissa-huskey/python-class/master/hello.txt"
    response = requests.get(url)
    # this shows us the body of the response
    print(response.text)
    # this converts the headers value into a dictionary for pprint
    print(response.status_code)
    # here we can see the headers. For example, the
    # 'Content-Length' tells us that the size is 40 bytes and
    # 'Content-Type' tells us that it was plain text
    headers = dict(response.headers)
    pprint(headers)

def request_weather():
    """Exercise 109 Print the weather"""
    url = "http://wttr.in"
    response = requests.get(url)
    print(response.text)

def request_astros():
    """Print out the astronauts currently in space using NASAs astros API
    https://api.nasa.gov/
    """
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    # this shows the body of the response
    # print(response.text)
    # accessing data from the API with Json using the dictionary syntax 'variable['key'] method
    data = response.json()
    print(f"There are {data['number']} people in space today.")
    # using a for loop to print the names of the astronauts with dictionary syntax
    for astro in data['people']:
        print(f"- {astro['name']}")

def request_location():
    """Exercise 110 Latitude and Longitude"""
    # getting the URL
    url = "https://freegeoip.app/json/"
    # this shows the body of the response
    response = requests.get(url)
    data = response.json()
    print(data)
    # output is:{'ip': '159.118.197.220', 'country_code': 'US', 'country_name': 'United States',
    # 'region_code': 'US-ID', 'region_name': 'Idaho', 'city': 'Nampa', 'zip_code': '83651',
    # 'time_zone': 'America/Boise', 'latitude': 43.541038513183594, 'longitude': -116.56346130371094,
    # 'metro_code': 0}
    # printing the city and state of the location for this IP address
    print(f"I am currently in {data['city']}, {data['region_name']}")
    # output is: 'I am currently in Nampa, Idaho'

def request_hello():
    """Say "hello" in another language using the hellosalut API
    https://hellosalut.stefanbohacek.dev/
    """
    url = "https://hellosalut.stefanbohacek.dev/"
    response = requests.get(url, params={'lang': 'de'})
    data = response.json()
    print(data)
    print(data['hello'])

def bored_activity():
    """Exercise 111 Parameters"""
    # getting the URL also referred to as 'endpoints'
    url = "https://www.boredapi.com/api/activity"
    response = requests.get(url, params={'participants': 1})
    activity = response.json()
    print(f"My activity for today is: {activity['activity']}")

def request_uv():
    """Print UV and Ozone info for today"""
    KEY = OPENUV_KEY
    response = requests.get(
        "https://api.openuv.io/api/v1/us",
        params={'lat': LAT, 'lng': LNG},
        headers={'x-access=token': KEY}
    )

    data = response.json()
    print("UV Index:", data['result']['uv'])
    print("Ozone:", data['result']['ozone'])

request_uv()
# bored_activity()
# request_hello()
# request_location()
# request_astros()
# request_weather()
# request_demo()
