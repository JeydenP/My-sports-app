from utilities import *
from datetime import date


today = date.today()

events_url = f"https://api.apilayer.com/therundown/sports/4/events/{today}"
teams_url = "https://api.apilayer.com/therundown/sports/4/teams"
sports_url = "https://api.apilayer.com/therundown/sports"
affiliates_url = "https://api.apilayer.com/therundown/affiliates"

# all_nba_events = get_data(events_url,{"include":"scores","affiliate_ids":"19","offset":"240"})
# nba_teams = get_data(teams_url)
# all_sports = get_data(sports_url)
# all_affiliates = get_data(affiliates_url)

# event_id = all_nba_events['events'][0]['event_id']
# specific_game_url = f"https://api.apilayer.com/therundown/events/{event_id}"
# specific_game_details = get_data(specific_game_url,{"include":"scores","affiliate_ids":"19","offset":"240"}) 


# make_json("all_NBA_events_details"+"_"+str(today),all_nba_events)
# make_json("nba_teams",nba_teams)
# make_json("specific_game_details",specific_game_details)


with open("../NBA/source/all_NBA_events_details.json","r") as f:
    game_event_and_score = json.loads(f.read())
    print("event id:",game_event_and_score['events'][0]['event_id'])
    print("Home:",game_event_and_score['events'][0]['score']['score_away'])
    print("away:",game_event_and_score['events'][0]['score']['score_home'])

print("complete")

