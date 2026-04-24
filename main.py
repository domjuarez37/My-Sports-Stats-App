from sports_stats import MLB, NFL_O, NFL_D, NBA
from add_player import player_database




def find_player(database, name):
    for player in database:
        if player.name.lower() == name.lower():
            return player
    # After I was done with code AI recommended adding the .lower so it becomes "caseinsensitive"


db = player_database()

while True:
    # AI recomenended using /n for better spacing 
    name = input("\nEnter player name (or type quit): ")

    if name.lower() == "quit":
        break

    player = find_player(db, name)

    if player:
        print("\n" + str(player))  # uses the str methods i built for each class
    else:
        print("Sorry, this player hasn't been added to the database.")