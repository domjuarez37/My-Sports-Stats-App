from sports_stats import All_Players


def player_database():
    database=[]
    # Used AI to help with creation of the file
    with open("database.csv","a+") as file:
      file.seek(0)
      for line in file:
          name, sport = line.strip().split(",")
          database.append(All_Players(name, sport))
    return database
                  




def add_player(database):

    name = input("Name: ")
    sport = input("Sport: ")

    player= All_Players(name,sport)
    database.append(player)


    with open("database.csv", "a") as file:
        file.write(f"{name},{sport}\n")

    print(f"Entry added: {name}:")

db = player_database()
   
while True:
      add_player(db)
      another = input("Add another player? (y/n): ")
      if another == "n":
        break