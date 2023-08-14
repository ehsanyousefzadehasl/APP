import random

class Human:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Football_player(Human):
    def team_assignment(self, team):
        self.team = team
    
    def get_name_team(self):
        return "Name: %*s,  Team: %*s"%(12, self.name, 2, self.team)

    def get_team(self):
        return self.team

names = [
    'Hossein',
    'Maziar',
    'Akbar',
    'Nima',
    'Mahdi',
    'Farhad',
    'Mohammad',
    'Khashayar',
    'Milad',
    'Mostafa',
    'Amin',
    'Saeed',
    'Pouya',
    'Pouriya',
    'Reza',
    'Ali',
    'Behzad',
    'Soheil',
    'Behrooz',
    'Shahrouz',
    'Saman',
    'Mohsen'
]

numbers = [0, 1]

footballers = []
for i in range(22):
    tmp_ftb = Football_player(names[i])
    
    randomness = random.choice(numbers)

    if(randomness == 1):
        tmp_ftb.team_assignment("A")
    else:
        tmp_ftb.team_assignment("B")
    footballers.append(tmp_ftb)


for footballer in footballers:
    print(footballer.get_name_team())

team_A_players_num = 0
team_B_players_num = 0
for element in footballers:
    if element.get_team() == "A":
        team_A_players_num = team_A_players_num + 1
    else:
        team_B_players_num = team_B_players_num + 1

print("Team A: ", team_A_players_num, ", Team B: ", team_B_players_num)