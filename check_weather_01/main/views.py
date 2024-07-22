from django.shortcuts import render 
# import json to load json data to python dictionary 
import json 
# urllib.request to make a request to api 
import urllib.request 
import os
from pathlib import Path
import yaml
from utility.weather_utilities import get_api_key


FILE_PATH = Path(os.path.abspath(__file__))

def index(request):
    if request.method == 'POST': 
        city = request.POST['city'] 
        ''' api key might be expired use your own api_key 
            place api_key in place of appid ="your_api_key_here "  '''
  
        # source contain JSON data from API 
        api_key = get_api_key(FILE_PATH)
        print(api_key)

        source = urllib.request.urlopen(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}").read() 
  
        # converting JSON data to a dictionary 
        list_of_data = json.loads(source) 
  
        # data for variable list_of_data 
        data = { 
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        } 
    else:
        data ={}
    return render(request, "index.html", data)
