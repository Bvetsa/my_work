class people:
    def __init__(self, fname, lname, fsport, fvgame):
        self.fname = fname
        self.lname = lname
        self.fsport = fsport
        self.fvgame = fvgame
    def fullname(self):
        fullname = self.fname + " " + self.lname
        print(fullname)
    def favideogame(self):
        if self.fvgame == "none":
            print(self.fname + " does not have a favorite video game.")
        else:
            print(self.fname + "'s favorite video game is " + self.fvgame)

def sport_favs(people, sport):

    bball_people = []
    for person in people:
        if person.fsport == sport:
            bball_people.append(person.fname)
    
    print( bball_people)


    
p1 = people("Bhargava", "Vetsa", "basketball", "Valorant")
p2 = people("Hari", "Vetsa", "baseball", "none")

p1.fullname()
p1.favideogame()

p2.fullname()
p2.favideogame()

sport_favs( [p1, p2], "baseball" )