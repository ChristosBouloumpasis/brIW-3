
people = []

class Person:
    newvar = "bob"
    def __init__(self, firstname, lastname, team, id):
        self.firstname = firstname
        self.lastname = lastname
        self.team = team
        self.id = id

    def add_pref(self, drink_id):
        self.drinkpref  =   drink_id
        pass
        
    def remove(self):
        pass


firstname = "Connor"
lastname = "Avery"
team = "Academy"
id = 1

person = Person(firstname, lastname, team, id)

people1 = []
people1.append(person)
print(Person.newvar)

Person.newvar = "bob no more"

#  this is a new person
firstname = "David"
lastname = "Avery"
team = "Academy"
id = 2

person = Person(firstname, lastname, team, id)

Person(firstname, lastname, team)

people1.append(person)
print(people1[0].firstname, people1[1].firstname)
print(Person.newvar)

