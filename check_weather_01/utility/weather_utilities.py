from pathlib import Path
import yaml


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