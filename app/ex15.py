import requests,json

api_key = '278075fb7941265e26a1b138c6665130'
base_url = 'http://api.openweathermap.org/data/2.5/weather?'
city_name = 'mangalore'
complete_url = base_url + 'appid=' + api_key + '&q=' + city_name

