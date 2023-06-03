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

def get_team_logo(team_ids):
    team_logos = []
    for id in team_ids:
        match id:
            case 11: #atlanta hawks
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/atl.png&w=70&h=70&transparent=true")
            case 1: #boston celtics
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/bos.png&w=70&h=70&transparent=true")
            case 2: #brooklyn nets
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/bkn.png&w=70&h=70&transparent=true")
            case 12: #charlotte hornets
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/cha.png&w=70&h=70&transparent=true")
            case 6: #chicago bulls
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/chi.png&w=70&h=70&transparent=true")
            case 7: #cleveland cavaliers
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/cle.png&w=70&h=70&transparent=true")
            case 26: #dallas mavericks
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/dal.png&w=70&h=70&transparent=true")
            case 16: #denver nuggets
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/den.png&w=70&h=70&transparent=true")
            case 8: #detroit pistons
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/det.png&w=70&h=70&transparent=true")
            case 21: #golden state warriors
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/gs.png&w=70&h=70&transparent=true")
            case 27: #houston rockets
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/hou.png&w=70&h=70&transparent=true")
            case 9: #indiana pacers
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/ind.png&w=70&h=70&transparent=true")
            case 22: #los angeles clippers
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/lac.png&w=70&h=70&transparent=true")
            case 23: #los angeles lakers
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/lal.png&w=70&h=70&transparent=true")
            case 28: #memphis grizzlies
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/mem.png&w=70&h=70&transparent=true")
            case 13: #miami heat
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/mia.png&h=70&w=70&transparent=true")
            case 10: #milwaukee bucks
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/mil.png&w=70&h=70&transparent=true")
            case 17: #minnesota timberwolves
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/min.png&w=70&h=70&transparent=true")
            case 29: #new orleans pelicans
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/no.png&w=70&h=70&transparent=true")
            case 3: #new york knicks
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/ny.png&w=70&h=70&transparent=true")
            case 18: #oklahoma city thunder
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/okc.png&w=70&h=70&transparent=true")
            case 14: #orlando magic
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/orl.png&w=70&h=70&transparent=true")
            case 4: #philadelphia 76ers
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/phi.png&w=70&h=70&transparent=true")
            case 24: #phoenix suns
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/phx.png&w=70&h=70&transparent=true")
            case 19: #portland trail blazers
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/por.png&w=70&h=70&transparent=true")
            case 25: #sacramento kings
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/sac.png&w=70&h=70&transparent=true")
            case 30: #san antonio spurs
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/sa.png&w=70&h=70&transparent=true")
            case 5: #toronto raptors
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/tor.png&w=70&h=70&transparent=true")
            case 20: #utah jazz
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/utah.png&w=70&h=70&transparent=true")
            case 15: #washington wizards
                team_logos.append("https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/wsh.png&w=70&h=70&transparent=true")
            case _: 
                return "Team not found"
    return team_logos
        
def get_broadcast_logo(broadcast):
    logos = []
    for stream in broadcast:
        match stream:
            case "ESPN":
                logos.append("https://a.espncdn.com/redesign/assets/img/logos/logo-espn-82x20.png")
            case "TNT":
                logos.append("https://www.tntdrama.com/themes/custom/ten_theme/images/tnt/tnt_logo_top.png")
            case "ABC":
                logos.append("https://assets-cdn.watchdisneyfe.com/delta/assets/abc/abc-nav.png")
    return logos