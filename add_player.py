from sports_stats import All_Players, MLB, NFL_O, NFL_D, NBA





def player_database():
    database=[]
    # Used AI to help with creation of the file. Specifically the "parts" structure.

    with open("database.csv", "r") as file:
        for line in file:
            parts = line.strip().split(",")

            name = parts[0]
            sport = parts[1]
            stat1 = parts[2]
            stat2 = parts[3]
            stat3 = parts[4]

            if sport == "Baseball":
                player = MLB(name, int(stat1), int(stat2), int(stat3))
            elif sport == "Football O":
                player = NFL_O(name, int(stat1), int(stat2), int(stat3))
            elif sport == "Football D":
                player = NFL_D(name, int(stat1), float(stat2), int(stat3))
            elif sport == "Basketball":
                player = NBA(name, int(stat1), int(stat2), int(stat3))
            
            database.append(player)


    return database
                  




def add_player(database):

    name = input("Name: ")
    sport = input("Sport: ")

    # Used AI to help with the row= ... makes the csv easier

    if sport== "Baseball":
       Homeruns= int(input("Homeruns: ")) 
       RBIs= int(input("RBIs: "))
       SBs= int(input("SBs: "))
       player= MLB(name,Homeruns, RBIs,SBs)
       row = f"{name},{sport},{Homeruns},{RBIs},{SBs}\n"

    
    elif sport== "Football O":
        TDs= int(input("TDs: "))
        yards= int(input("yards: "))
        receptions= int(input("receptions: "))
        player= NFL_O(name,TDs,yards,receptions)
        row = f"{name},{sport},{TDs},{yards},{receptions}\n"
    
    elif sport== "Football D":
        tackles= int(input("tackles: "))
        sacks= float(input("sacks: "))
        INTs= int(input("INTs: "))
        player= NFL_D(name,tackles,sacks,INTs)
        row = f"{name},{sport},{tackles},{sacks},{INTs}\n"
    
    elif sport== "Basketball":
        points= int(input("points: "))
        rebounds= int(input("rebounds: "))
        assists= int(input("assists: "))
        player= NBA(name,points,rebounds,assists)
        row = f"{name},{sport},{points},{rebounds},{assists}\n"

    else:
        print("Try again that sport doesn't exsist")
        return

    database.append(player)


    with open("database.csv", "a") as file:
        file.write(row)

    print(f"Entry added: {name}:")

if __name__ == "__main__":
    db = player_database()
   
    while True:
      add_player(db)
      another = input("Add another player? (y/n): ")
      if another == "n":
        break