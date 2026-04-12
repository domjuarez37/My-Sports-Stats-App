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