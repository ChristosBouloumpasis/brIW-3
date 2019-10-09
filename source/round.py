from source.load_database import *

class Round:

    def __init__(self, maker, people_ids_list, active=True):
        self.maker = maker
        self.people_ids_list = people_ids_list
        self.active = active

    def add_person(self, person):
        people_ids_list += person

    def add_id(self, id):
        self.id = id
    
    def remove_person_round(self, person):
        people_ids_list.remove(person)
    
    def get_maker(self):
        return self.maker
    
    def get_orders(self):
        return self.people_ids_list
    
    def get_status(self):
        return self.active