from django.shortcuts import render 
# import json to load json data to python dictionary 
import json 
# urllib.request to make a request to api 
import urllib.request 
import os
from pathlib import Path
import yaml
from utility.weather_utilities import get_api_key, process_source, strip_accents
from urllib.error import HTTPError


FILE_PATH = Path(os.path.abspath(__file__))

def index(request):
    if request.method == 'POST': 
        city = request.POST.get('city')
        city = strip_accents(city)
        api_key = get_api_key(FILE_PATH)
        try:
            source = urllib.request.urlopen(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}").read()
            print(type(source))
            weather_data = process_source(source)
        except HTTPError:
            weather_data = {"error_message": "Incorrect API call!"}
    else:
        weather_data ={}
    return render(request, "index.html", weather_data)
