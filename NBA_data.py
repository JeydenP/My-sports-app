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


with open("../NBA/past-games-archive/BOS_vs_MIA_2023-05-23.json","r") as f:
    bos_vs_mia = json.loads(f.read())
    home_team_abbr = bos_vs_mia['teams_normalized'][1]['abbreviation']
    away_team_abbr = bos_vs_mia['teams_normalized'][0]['abbreviation']
    print("event id:",bos_vs_mia['event_id'])
    print(away_team_abbr+":",bos_vs_mia['score']['score_home'])
    print(home_team_abbr+":",bos_vs_mia['score']['score_away'])

print("complete")
