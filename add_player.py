from sports_stats import MLB, NFL_O, NFL_D, NBA

players= {}

def add_player():
  sport = input("Choose sport (MLB, NFL_O, NFL_D, NBA): ")  
  name= input("Name of player: ")
  players[name]= sport
while True:
    add_player()
    another = input("Add another player? (y/n): ")
    if another == "n":
        break


print(players)
   
