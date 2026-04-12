class Baseball:
    def __init__(self, name, Homeruns, RBIs, SBs):
        self.name= name
        self.Homeruns= Homeruns
        self.RBIs= RBIs
        self.SBs= SBs
    def __str__(self):
        return f"{self.name} has {self.Homeruns} home runs, {self.RBIs} RBIs, and {self.SBs} stolen bases in his career "





player= Baseball("Gunnar Henderson",92,272,64)
print(player) 


class Football_O:
    def __init__(self, name, TDs, yards, receptions ):
        self.name= name
        self.TDs= TDs
        self.yards= yards
        self.receptions= receptions 
    def __str__(self):
        return f"{self.name} has {self.TDs} touchdowns, {self.yards} yards, and {self.receptions} receptions in his career"


football_player= Football_O("Zay Flowers", 14, 3128, 237)
print(football_player)
        
