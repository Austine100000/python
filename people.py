class people:
    def __init__(self, name, age, gender):
        self.peoplename = name
        self.peopleage = age
        self.peoplegender = gender

    def display(self):
        print(self.peoplename, self.peopleage, self.peoplegender)


myobj = people("caroline", "30", "female")
myobj1 = people("Peter", "25", "male")
myobj2 = people("Linda", "28", "female")
myobj3 = people("John", "19", "male")
myobj.display()
myobj1.display()
myobj2.display()
myobj3.display()
