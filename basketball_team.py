"""
Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.
"""
class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]

    def __repr__(self):
        player_infos = f"Name: {self.name} \nAge: {self.age} \nPosition: {self.position} \nTeam: {self.team}"
        return player_infos

"""
Given these variables, create Player instances for each of the following dictionaries. Be sure to instantiate these outside the class definition, in the outer scope.
"""
kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
        }
jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
        }
kyrie = {
        "name": "Kyrie Irving", 
        "age":32, 
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
        }
    
# Create your Player instances here!
player_kevin = Player(kevin)
print(player_kevin)
player_jason = Player(jason)
print(player_jason)
player_kyrie = Player(kyrie)
print(player_kyrie)

