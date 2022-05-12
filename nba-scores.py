from requests import get
from pprint import PrettyPrinter


BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()



def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    links = data['links']
    return links

def get_scoreboard():
    scoreboard = get_links()['currentScoreboard']
    games = get(BASE_URL + scoreboard).json()['games']
    
    for game in games:
        home_team = game['hTeam']
        away_team = game['vTeam']
        clock = game['clock']
        period = game['period']
        
        print("------------------------")
        print(
            f"{home_team['triCode']} vs {away_team['triCode']}")
        if home_team['score'] == "" and home_team['score'] == "":
            print("Game not started yet")
            print("")
            
        elif clock == "" and home_team['score'] == 0 and away_team['score'] == 0:
            print("Game starting soon")
            print("")
        elif clock == "":
            print(f"Final Score: {home_team['score']} - {away_team['score']}")
            print("")
           
            #FIGURE OUT WAY TO FIND GAME START TIME
        else:                        
            print(f"{home_team['score']} - {away_team['score']}")
            print(f"{clock} period {period['current']}")
            print("")


def get_stats():
    stats = get_links()['leagueTeamStatsLeaders']
    teams =get(BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']
    
    teams = list(filter(lambda x: x['name'] != "Team", teams))
    #sort teams by rank in ppg
    print("")
    print("Teams ranked by average PPG all season")
    print("--------------------------------------------")
    teams.sort(key=lambda x: int(x['ppg']['rank']))
    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        ppg = team['ppg']['avg']
        
        print(f"{i+1}. {name} {nickname} - Average PPG: {ppg}")
    

print("Games Today: ")
get_scoreboard()    
get_stats()
    


