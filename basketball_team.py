class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]
        self.all_players = []

    def __repr__(self):
        player_infos = f"Name: {self.name} \nAge: {self.age} \nPosition: {self.position} \nTeam: {self.team}"
        return player_infos
    
"""
Given the example list of players, write a for loop that will populate an empty list with Player objects from the original list of dictionaries.
"""

players = [
{
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
},
{
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
},
{
    "name": "Kyrie Irving", 
    "age":32,
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
},
{
    "name": "Damian Lillard", 
    "age":33,
    "position": "Point Guard", 
    "team": "Portland Trailblazers"
},
{
    "name": "Joel Embiid", 
    "age":32,
    "position": "Power Foward", 
    "team": "Philidelphia 76ers"
},
{
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
}
]

new_team = []
for player_dict in players:
    new_team.append(Player(player_dict))
        
print(f"Check the new team: \n{new_team}")