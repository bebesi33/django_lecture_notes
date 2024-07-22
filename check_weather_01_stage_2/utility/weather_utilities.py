from pathlib import Path
import yaml
import json
from typing import Dict
import numpy as np
from utility.constants import CELSIUS_SYMBOL, KELVIN_TO_CELSIUS
import unicodedata


def get_api_key(view_location : Path) -> str:
    """return open weather API key

    Args:
        view_location (Path): _description_

    Returns:
        str: token for openweather
    """
    yaml_location = view_location.parents[3] / Path("tokens") / Path("open_weather_api_key.yaml")
    with open(yaml_location, 'r') as yaml_file:
        token = yaml.safe_load(yaml_file)
    return token


def process_source(source: bytes) -> Dict[str, str]:
    """Process API call result

    Args:
        source (bytes): byte streem input from OpeWeather

    Returns:
        Dict[str, str]: Parsed dictionary
    """
    list_of_data = json.loads(source)
    # print(list_of_data)
    # data for variable list_of_data
    data = {
        "city_name": str(list_of_data["name"]),
        "country_code": str(list_of_data['sys']['country']), 
        "coordinate": "longitude|" + str(list_of_data['coord']['lon']) + ' > latitude|'
                    + str(list_of_data['coord']['lat']), 
        "temp": process_kelvin_temperature(list_of_data['main']['temp']),
        "feels_like": process_kelvin_temperature(list_of_data['main']['feels_like']),
        "pressure": str(list_of_data['main']['pressure']) + " mbar", 
        "humidity": str(list_of_data['main']['humidity']) + " %", 
    }
    return data


def process_kelvin_temperature(temperature: float) -> str:
    """Calculates the Celsius value of Kelvin temperatures

    Args:
        temperature (float): Temperature in Kelvin

    Returns:
        str: Temperature in Celsius
    """
    temperature = np.round(temperature - KELVIN_TO_CELSIUS, 2)
    return str(temperature) + " " + CELSIUS_SYMBOL


def strip_accents(s: str) -> str:
    """
    Remove accents from a given string.

    Args:
        s (str): The input string from which accents need to be removed.

    Returns:
        str: A new string with all accents removed.
    """
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
