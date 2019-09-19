#! /usr/bin/env python3
import os
import sys
from source.persist_data import *

arguments = sys.argv

people_id = {}
drinks_id = {}
round_id = {}


class Person:

    def __init__(self, firstname, lastname, team, id):
        self.firstname = firstname
        self.lastname = lastname
        self.team = team
        self.id = id

    def get_all_data(self):
        all_data = [self.firstname, self.lastname, self.team, self.id, self.preference, self.additions]
        return all_data

    def add_pref(self, drink_id, additions):
        self.preference = drink_id
        self.additions = additions

    def remove(self):
        pass

class Drink:

    def __init__(self, name, id, drink_type, contains=None):
        self.name = name
        self.id = id
        self.type = drink_type
        self.contains = contains

    def get_all_data(self):
        all_data = [self.name, self.id, self.type, self.contains]
        return all_data

class Round:

    def __init__(self, id, maker, people_ids_list, active=True):
        self.id = id
        self.maker = maker
        self.people_ids_list = people_ids_list
        people_ids_list.append(maker)
        self.active = active

    def add_person(self, person):
        people_ids_list += person

    def get_all_data(self):
        return [self.id, self.maker, self.people_ids_list, self.active]
        
def new_id(id_objects_dictionary):
    if len(id_objects_dictionary.keys()) == 0:
        return 1
    else:
        return len(id_objects_dictionary.keys()) + 1


def startOperation():
    people_tbl = load_dictionary("people_tbl")
    drinks_tbl = load_dictionary("drinks_tbl")
    preferences_tbl = load_dictionary("preferences_tbl")
    #  loadData("people_tbl",people_tbl)
    #  loadData("drinks_tbl",drinks_tbl)
    #  loadData("preferences_tbl",preferences_tbl)
    return [people_tbl, drinks_tbl, preferences_tbl]


def display_menu():
    menu_text = '''
                                    ▄▄▄▄· ▄▄▄  ▪  ▄▄▌ ▐ ▄▌
                                    ▐█ ▀█▪▀▄ █·██ ██· █▌▐█
                                    ▐█▀▀█▄▐▀▀▄ ▐█·██▪▐█▐▐▌
                                    ██▄▪▐█▐█•█▌▐█▌▐█▌██▐█▌
                                    ·▀▀▀▀ .▀  ▀▀▀▀ ▀▀▀▀ ▀▪
        Welcome to BrIW!
        Choose an option
        1. People who want a drink
        2. Drinks available
        3. Add a person
        4. Add a drink
        5. View preferences
        6. Modify preferences
        7. Delete Person
        8. Delete Drink
        9. Start BrIWing
        X. Exit & Save
        '''
    print(menu_text)


def menuReturn():
    menu_return = input("Return to main menu? Y / N: ").upper()
    if menu_return == 'Y':
        os.system("clear")
    elif menu_return == 'N':
        print("Goodbye!")
        exit()

def display_table(dictionary, title, is_preferences):
    print(f"+{'=' * 25}+")
    print(title.upper())
    print(f"+{'=' * 25}+")
    if is_preferences:
        for person, drink in dictionary.items():
            print(f" | {people_tbl[person]} - {drinks_tbl[int(drink)]}")
    else:
        for key, value in dictionary.items():
            print(f" | {key} - {value}")
    print(f"+{'=' * 25}+")


def add_person(new_person):
    person_id = list(people_tbl.keys())[-1] + 1
    people_tbl[person_id] = new_person.capitalize()
    print(new_person.capitalize() + " has been added")


def add_drink(new_drink):
    drink_id = list(people_tbl.keys())[-1] + 1
    drinks_tbl[drink_id] = new_drink.capitalize()
    print(new_drink.capitalize() + " has been added")


def remove_person(remove_person):
    try:
        removing_person = people_tbl.pop(remove_person)
        print(removing_person + " has been removed.")
    except:
        print("Person doesn't exist")


def remove_drink(remove_drink):
    try:
        removing_drink = drinks_tbl.pop(remove_drink)
        print(remove_drink + " has been removed")
    except:
        print("Drink doesn't exist")


def string_check_old(input_string):
    stringIsAlpha = input_string.isalpha()
    while stringIsAlpha == False:
        input_string = input("None alphabetical characters entered - try again: ")
        stringIsAlpha = input_string.isalpha()
    return input_string


def string_check(input_string):
    stringIsntDigit = input_string.isdigit()
    while stringIsntDigit == True:
        input_string = input("Please enter only alphabetical characters, not numbers - try again: ")
        stringIsntDigit = input_string.isdigit()
    return input_string


def modify_preferences(person_id, drinks_id):
    preferences_tbl[person_id] = drinks_id


def loadData(filename, dictionary):
    try:
        loadedData = open(filename + ".txt", "r")

    except FileNotFoundError as fnfe:
        print("File not found: " + str(fnfe))
        return []

    except Exception as e:
        print("An error occurred: " + str(e))

    for line in loadedData.readlines():
        items = line.split()
        if items[0].isnumeric():
            id = int(items[0])
        else:
            print(f"ID must be numeric - Skipping {items[0]}")
            continue
        dictionary[id] = items[1]
    loadedData.close()

def save_data_object(filename, object_class):
    try:
        with open(filename + ".txt", 'w') as objects_file:
            for instance in object_class:            
                objects_file.write(f"{instance.get_all_data()}\n")        
    except Exception as e:
        print("Unable to save: " + str(e))


# def save_data(filename, dictionary): 
#     try:
#         with open(filename + ".txt", 'w') as dictionary_file:
#             for key, value in dictionary.items():            
#                 dictionary_file.write(f"{key} {value}\n")        
#     except Exception as e:
#         print("Unable to save: " + str(e))
    
def clearScreen():
    os.system("clear")

#  Application start now
loaded_dictionaries = startOperation()
people_tbl = loaded_dictionaries[0]
drinks_tbl = loaded_dictionaries[1]
preferences_tbl = loaded_dictionaries[2]

if __name__ == "__main__":
    while True:
        display_menu()
        user_input = input("Please enter your input: ")

    #         1. People who want a drink
        if user_input == "1":
            clearScreen()
            display_table(people_tbl, " People", False)
            menuReturn()

    #         2. Drinks available
        elif user_input == "2":
            clearScreen()
            display_table(drinks_tbl, " Drinks", False)
            menuReturn()

    #         3. Add a person
        elif user_input == "3":
            clearScreen()
            new_person = input("What is the persons name, you\'d like to add? ")
            new_person = string_check(new_person)
            add_person(new_person)

    #         4. Add a drink
        elif user_input == "4":
            clearScreen()
            new_drink = input("What is the drink you\'d like to add? ")
            new_drink = string_check(new_drink)
            add_drink(new_drink)

        # elif user_input == "4":
        #     clearScreen()
        #     new_drink_name = input("What is the drink you\'d like to add? Give it a name: ")
        #     new_drink_name = string_check(new_drink_name)
        #     new_drink_id = new_id(drinks_id)
        #     new_drink_type = input("Is this a hot drink? (y/n): ").upper()
        #     if new_drink_type == "Y":
        #         new_drink_type = "Hot"
        #     else:
        #         new_drink_type = "Cold"
        #     new_drink_contains = input("Please enter any additions in this drink or hit enter for none: ")
        #     new_drink = Drink(new_drink_name, new_drink_id, new_drink_type, new_drink_contains)


    #         5. View preferences
        elif user_input == "5":
            clearScreen()
            display_table(preferences_tbl, " Preferences", True)
            menuReturn()


    #         6. Modify preferences
        elif user_input == "6":
            clearScreen()
            display_table(preferences_tbl, " Current Preferences", True)
            preference_update = input("Would you like to modify a preference? Y / N: ").upper()
            if preference_update == "Y":
                while True:
                    clearScreen()
                    display_table(people_tbl, " People", False)
                    person_id = int(input("Which persons preference would you like to update? "))
                    if person_id in people_tbl.keys():
                        while True:
                            clearScreen()
                            display_table(drinks_tbl, " Drinks", False)
                            incorrect_drink_id = False
                            if incorrect_drink_id == True:
                                print(f"The drink ID you choose {drinks_id} is not valid.")
                            drinks_id = int(input(f"Which drink is {people_tbl[person_id]}\'s preference? "))
                            if drinks_id in drinks_tbl.keys():
                                modify_preferences(person_id, drinks_id)
                                print(f"{people_tbl[person_id]}\'s preference of {drinks_tbl[drinks_id]} has been added.")
                                break
                            else:
                                input("Incorrect drink ID, press any key to try again.")
                    else:
                        input("Incorrect person ID, press any key to try again.")
            menuReturn()
    

        # Delete person
        elif user_input == "7":
            clearScreen()
            display_table(people_tbl, " Delete Person ", False)
            remove_person_input = input("Select ID to remove: ")
            remove_person(remove_person_input)

        # Delete drink
        elif user_input == "8":
            clearScreen()
            display_table(people_tbl, " Delete Drink", False)
            remove_drink_input = input("Select ID to remove: ")
            remove_drink(remove_drink_input)

        #  Create a round
        elif user_input == "9":
            clearScreen()
            round = Round()
            round.create()
        
        # Join a round
        elif user_input == "10":
            clearScreen()
            print("Join a round")
        
        elif user_input == "D":
            clearScreen()
            print("DEBUG")
            print("------")
            print("People: ")
            print(people_tbl)
            print("Drinks: ")
            print(drinks_tbl)
            print("Preferences: ")
            print(preferences_tbl)
            menuReturn()

        elif user_input == "X":
            save_dictionary("people_tbl",people_tbl)
            save_dictionary("drinks_tbl",drinks_tbl)
            save_dictionary("preferences_tbl", preferences_tbl)
            # save_data_object("round",round)
            exit()

        else:
            print("Incorrect menu choice")
