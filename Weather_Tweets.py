# Dependencies
import tweepy
import time
import json
import random
import requests as req
import datetime
from config import consumer_key, consumer_secret, access_token, access_token_secret, weather_api_key

# Twitter API Keys
consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret


# Weather API Key
# OpenWeatherMap API Key
api_key = weather_api_key


# Create a function that gets the weather in London and Tweets it
def WeatherTweet():

    # Construct a Query URL for the OpenWeatherMap
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = input(f"Pick a city: ")
    units = "imperial"
    query_url = url + "appid=" + api_key + "&q=" + city + "&units=" + units

    # Perform the API call to get the weather
    response = req.get(query_url).json()
    weather_tweet = response['main']['temp']

    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet the weather
    api.update_status(f"The current temp in {city} is {weather_tweet}")

    # Print success message

# Set timer to run every 1 hour
# Create a loop that calls the TweetOut function every minute
counter = 0

# Infinite loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    WeatherTweet()

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1
    if counter == 1:
        break

