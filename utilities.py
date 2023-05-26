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
def get_team_logo(team_id):
    match team_id:
        case 11:
            pass
        case 1:
            pass
        case 2:
            pass
        case 12:
            pass
        case 6:
            pass
        case 7:
            pass
        case 26:
            pass
        case 16:
            pass
        case 8:
            pass
        case 21:
            pass
        case 27:
            pass
        case 9:
            pass
        case 22:
            pass
        case 23:
            pass
        case 28:
            pass
        case 13:
            pass
        case 10:
            pass
        case 17:
            pass
        case 29:
            pass
        case 3:
            pass
        case 18:
            pass
        case 14:
            pass
        case 4:
            pass
        case 24:
            pass
        case 19:
            pass
        case 25:
            pass
        case 30:
            pass
        case 5:
            pass
        case 20:
            pass
        case 15:
            pass
        case _:
            pass