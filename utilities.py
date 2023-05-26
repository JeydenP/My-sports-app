import requests
import config
import json
import os

def get_data(url,querystring = None,key = 1):
    api_key = ""
    if key == 1:
        api_key = config.api_key1
    elif key == 2:
        api_key = config.api_key2
    elif key == 3:
        api_key = config.api_key3
    else:
        raise Exception("Invalid api key")
    response = requests.get(url,headers = {"apikey":api_key},params=querystring)
    status_code = response.status_code
    if status_code != 200:
        raise Exception(status_code)
    data = response.json()
    return data

def make_json(name,data,save_path = None):
    save_path = os.path.join("../NBA/past-games-archive/",name) 
    with open(save_path+".json","w") as f:
        f.write(json.dumps(data))

#todo: add team logos urls.
def get_team_logo(team_name):
    match team_name:
        case "Atlanta Hawks":
            pass
        case "Boston Celtics":
            pass
        case "Brooklyn Nets":
            pass
        case "Charlotte Hornets":
            pass
        case "Chicago Bulls":
            pass
        case "Cleveland Cavaliers":
            pass
        case "Dallas Mavericks":
            pass
        case "Denver Nuggets":
            pass
        case "Detroit Pistons":
            pass
        case "Golden State Warriors":
            pass
        case "Houston Rockets":
            pass
        case "Indiana Pacers":
            pass
        case "Los Angeles Clippers":
            pass
        case "Los Angeles Lakers":
            pass
        case "Memphis Grizzlies":
            pass
        case "Miami Heat":
            pass
        case "Milwaukee Bucks":
            pass
        case "Minnesota Timberwolves":
            pass
        case "New Orleans Pelicans":
            pass
        case "New York Knicks":
            pass
        case "Oklahoma City Thunder":
            pass
        case "Orlando Magic":
            pass
        case "Philadelphia 76ers":
            pass
        case "Phoenix Suns":
            pass
        case "Portland Trail Blazers":
            pass
        case "Sacramento Kings":
            pass
        case "San Antonio Spurs":
            pass
        case "Toronto Raptors":
            pass
        case "Utah Jazz":
            pass
        case "Washington Wizards":
            pass
        case _:
            pass