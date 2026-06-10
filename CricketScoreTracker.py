class player:
    def __init__(self,name,runs):
        self.name=name
        self.runs=runs
class Match:
    def __init__(self,played):
        self.played=played
class Tournament:
    def __init__(self):
        pass
    def calculate_average_runs(self,runs,played):
        return runs/played
    def display_player_stats(self):
        print("="*50)
        print("Player perform reports")
        print("="*50)
        print(f"Player Name : {p.name} \n Total Runs : {p.runs} \n Matches Played : {m.played} \n Average Runs : {t.calculate_average_runs(p.runs,m.played)}")
        print("="*50)
p=player("Virat Kohli",12000)
m=Match(25)
t=Tournament()
t.display_player_stats()