from utilities import *
from flask import Flask, render_template
from datetime import date,timedelta
import time

app = Flask(__name__)
today = date.today()
yesterday = today - timedelta(days=1)


events_url = f"https://api.apilayer.com/therundown/sports/4/events/{yesterday}"
all_events_details = get_data(events_url,{"include":"scores","affiliate_ids":"19","offset":"240"})

event_id = all_events_details['events'][0]['event_id']
specific_game_url = f"https://api.apilayer.com/therundown/events/{event_id}"
specific_game_details = get_data(specific_game_url,{"include":"scores","affiliate_ids":"19","offset":"240"})


for team in specific_game_details['teams']:
    if(team['is_away']):
        away_team = team['name']
        away_team_abbr = specific_game_details['teams_normalized'][0]['abbreviation']
        away_score = specific_game_details['score']['score_away']
    else:
        home_team = team['name']
        home_team_abbr = specific_game_details['teams_normalized'][1]['abbreviation']
        home_score = specific_game_details['score']['score_home']

def get_live_score(home_score,away_score):
    new_scores = []
    live_score = get_data(specific_game_url,{"include":"scores","affiliate_ids":"19","offset":"240"})
    if(live_score['score']['event_status'] != "STATUS_FINAL"):
        print("Game finished \nfinal score:",live_away,"-",live_home)
        make_json(away_team_abbr+"_vs_"+home_team_abbr+"_"+str(today),live_score)
        return
    while(live_score['score']['event_status'] == "STATUS_FINAL"):
        live_away = live_score['score']['score_away']
        live_home = live_score['score']['score_home']
        if(live_away != away_score or live_home != home_score):
            away_score = live_away
            home_score = live_home
            new_scores.append(away_score)
            new_scores.append(home_score)
            new_scores.append(live_score['score']['event_status'])
            return new_scores
        else:#recursion might not be good idea
            time.sleep(120)
            get_live_score(home_score,away_score)
    return new_scores

new_scores = get_live_score(home_score,away_score)
print("new scores:",new_scores)
away_score = new_scores[0]
home_score = new_scores[1]


print("away scoooore:",away_score)
print("home score:",home_score)

time_clock = specific_game_details['score']['display_clock']
broadcast = specific_game_details['score']['broadcast']
print("complete")

        
        


@app.route('/')
def index():
    
        return render_template('index.html',
                               away_team = away_team,
                               away_team_abbr = away_team_abbr,
                               home_team = home_team,
                               home_team_abbr = home_team_abbr,
                               broadcast = broadcast,
                               
                               away_score = away_score,
                               home_score = home_score,
                               time_clock = time_clock,
                               )
        
app.run(host="0.0.0.0",port=80)