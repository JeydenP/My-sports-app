import requests
import config
import json
import os

def get_data(url,querystring = None):
    response = requests.get(url,headers = {"apikey":config.api_key1},params=querystring)
    status_code = response.status_code
    if status_code != 200:
        raise Exception(status_code)
    data = response.json()
    return data

def make_json(name,data,save_path = None):
    save_path = os.path.join("../NBA/source/",name) 
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