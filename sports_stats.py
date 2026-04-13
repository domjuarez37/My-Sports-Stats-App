class MLB:
    def __init__(self, name, Homeruns, RBIs, SBs):
        self.name= name
        self.Homeruns= Homeruns
        self.RBIs= RBIs
        self.SBs= SBs

    def __str__(self):
        return f"{self.name} has {self.Homeruns} home runs, {self.RBIs} RBIs, and {self.SBs} stolen bases in his career "





class NFL_O:
    def __init__(self, name, TDs, yards, receptions ):
        self.name= name
        self.TDs= TDs
        self.yards= yards
        self.receptions= receptions 
    def __str__(self):
        return f"{self.name} has {self.TDs} touchdowns, {self.yards} yards, and {self.receptions} receptions in his career"




class NFL_D:
    def __init__(self, name, tackles, sacks, INTs):
        self.name= name
        self.tackles= tackles
        self.sacks= sacks
        self.INTs= INTs
    def __str__(self):
        return f"{self.name} has {self.tackles} tackes, {self.sacks} sacks, and {self.INTs} interceptions in his career" 




class NBA:
    def __init__(self, name, points, rebounds, assists):
        self.name= name
        self.points= points
        self.rebounds= rebounds
        self.assists= assists
    def __str__(self):
        return f"{self.name} has {self.points} points, {self.rebounds} rebounds, and {self.assists} assists in his career"

