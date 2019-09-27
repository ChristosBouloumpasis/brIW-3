#! /usr/bin/env python3
import os
import sys
from source.load_database import *
from source.round import Round

arguments = sys.argv

def startOperation():
    people_tbl = populate_dict_from_db("people_tbl")
    drinks_tbl = populate_dict_from_db("drinks_tbl")
    preferences_tbl = populate_dict_from_db("preferences_tbl")
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
        10. Join a round
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

def string_check(input_string):
    stringIsntDigit = input_string.isdigit()
    while stringIsntDigit == True:
        input_string = input("Please enter only alphabetical characters, not numbers - try again: ")
        stringIsntDigit = input_string.isdigit()
    return input_string

    
def clearScreen():
    os.system("clear")

#  Application start now
loaded_dictionaries = startOperation()
people_tbl = loaded_dictionaries[0]
drinks_tbl = loaded_dictionaries[1]
preferences_tbl = loaded_dictionaries[2]

round = Round(0, ['auto'], active=False)
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
            people_tbl = populate_dict_from_db("people_tbl")


    #         4. Add a drink
        elif user_input == "4":
            clearScreen()
            new_drink = input("What is the drink you\'d like to add? ")
            new_drink = string_check(new_drink)
            drinks_tbl = add_drink(new_drink)

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
                                preferences_tbl = modify_preferences(person_id, drinks_id)
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
            remove_person_input = int(input("Select ID to remove: "))
            people_tbl = remove_person(remove_person_input)

        # Delete drink
        elif user_input == "8":
            clearScreen()
            display_table(drinks_tbl, " Delete Drink", False)
            remove_drink_input = int(input("Select ID to remove: "))
            drinks_tbl = remove_drink(remove_drink_input)

        #  Create a round
        elif user_input == "9":
            clearScreen()
            if round.active:
                print("A round is already in progress.")
            else:
                display_table(people_tbl, " People", False)
                maker = int(input("What is your person ID? "))
                round = Round(maker, [maker])
                print(f"{people_tbl[maker]} a round has been created.")
            menuReturn()
        
        # Join a round
        elif user_input == "10":
            clearScreen()
            if round.active:
                print("Join a round")
            else:
                print("No round is active at present - create one.")
            menuReturn()

        
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

        elif user_input == "X" or "x":
            exit()

        else:
            print("Incorrect menu choice")
