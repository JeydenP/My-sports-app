from utilities import *
from flask import Flask, render_template, jsonify
from datetime import date,timedelta
import time
import os
import json

app = Flask(__name__)
today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

folder_path = "../NBA/past-games-archive/"

# Get the list of files in the folder
files = os.listdir(folder_path)
# Sort the files based on their modified time
sorted_files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
# Get the path of the last file (most recently modified)
last_file_path = os.path.join(folder_path, sorted_files[-1])



events_url = f"https://api.apilayer.com/therundown/sports/4/events/{date(2025,6,22)}"
all_events_details = get_data(events_url,{"include":"scores","affiliate_ids":"19","offset":"240"},3)



print("test")
specific_game_details = []

event_id = all_events_details['events'][0]['event_id']
specific_game_url = f"https://api.apilayer.com/therundown/events/{event_id}"
specific_game_details.append(get_data(specific_game_url,{"include":"scores","affiliate_ids":"19","offset":"240"},3))

with open(folder_path+sorted_files[-2],"r") as file1, open(folder_path+sorted_files[-3],"r") as file2:
    past_game1 = json.loads(file1.read())
    past_game2 = json.loads(file2.read())
    specific_game_details.append(past_game1)
    specific_game_details.append(past_game2)

away_teams = []
away_team_abbr = []
away_score = []
away_team_id = []

home_teams = []
home_team_abbr = []
home_score = []
home_team_id = []
broadcast = []

for game in specific_game_details:
    broadcast.append(game['score']['broadcast'])
    for team in game['teams']:
        if(team['is_away']):
            away_teams.append(team['name'])
            away_team_abbr.append(game['teams_normalized'][0]['abbreviation'])
            away_score.append(game['score']['score_away'])
            away_team_id.append(team['team_normalized_id'])
        else:
            home_teams.append(team['name'])
            home_team_abbr.append(game['teams_normalized'][1]['abbreviation'])
            home_score.append(game['score']['score_home'])
            home_team_id.append(team['team_normalized_id'])
        
def get_live_score(home_score,away_score):
    new_scores = []
    live_score = get_data(specific_game_url,{"include":"scores","affiliate_ids":"19","offset":"240"},2)
    if(live_score['score']['event_status'] == "STATUS_FINAL"):
        print("Game is over")
        make_json(away_team_abbr[0]+"_vs_"+home_team_abbr[0]+"_"+str(today),live_score)
        exit()
    elif(live_score['score']['event_status'] == "STATUS_HALFTIME"):
            print("Game is at halftime")
            time.sleep(60*16)
    while(live_score['score']['event_status'] != "STATUS_FINAL"):
        live_away = live_score['score']['score_away']
        live_home = live_score['score']['score_home']
        if(live_away != away_score[0] or live_home != home_score[0]):
            away_score[0] = live_away
            home_score[0] = live_home
            new_scores.append(away_score[0])
            new_scores.append(home_score[0])
            new_scores.append(live_score['score']['display_clock'])
            new_scores.append(live_score['score']['game_period'])
            new_scores.append(live_score['score']['event_status'])
            return new_scores
        else:
            time.sleep(120)
            live_score = get_data(specific_game_url,{"include":"scores","affiliate_ids":"19","offset":"240"},2)
    return

time_clock = specific_game_details[0]['score']['display_clock']
quarter = specific_game_details[0]['score']['game_period']

@app.route('/')
def index():
    away_team_logo = get_team_logo(away_team_id)
    home_team_logo = get_team_logo(home_team_id)
    broadcast_logo = get_broadcast_logo(broadcast)
    
    return render_template('index.html',
                            away_team = away_teams,
                            away_team_abbr = away_team_abbr,
                            home_team = home_teams,
                            home_team_abbr = home_team_abbr,
                            broadcast = broadcast,
                            away_team_logo = away_team_logo,
                            home_team_logo = home_team_logo,
                            broadcast_logo = broadcast_logo,
                            quarter = quarter,
                            
                            home_score = home_score,
                            away_score = away_score,
                            time_clock = time_clock,
                           )
 
@app.route('/get_live_scores')   
def get_live_scores():
    global home_score
    global away_score
    
    
    new_scores = get_live_score(home_score[0], away_score[0])
    away_score[0] = new_scores[0]  
    home_score[0] = new_scores[1]
    time_clock = new_scores[2]
    quarter = new_scores[3]
    game_status = new_scores[-1]

    # Return the updated scores as JSON
    return jsonify({
        'home_score': home_score[0],
        'away_score': away_score[0],
        'time_clock': time_clock,
        'game_status': game_status,
        'quarter': quarter
    })

app.run(host="0.0.0.0",port=80,threaded=True,debug=True)