from source.load_database import *

class Round:

    def __init__(self, maker, people_ids_list, active=True):
        self.maker = maker
        self.people_ids_list = people_ids_list
        self.active = active

    def add_person(self, person):
        people_ids_list += person
    
    def remove_person_round(self, person):
        people_ids_list.remove(person)

    def get_all_data(self):
        return [self.id, self.maker, self.people_ids_list, self.active]