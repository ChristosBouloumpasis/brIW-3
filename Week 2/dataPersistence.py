# Preferences table links peoples key ID with a drink ID.

import os
os.system("clear")

people_tbl = {}
drinks_tbl = {}
preferences_tbl = {}

def startOperation():
    loadData("people_tbl",people_tbl)
    loadData("drinks_tbl",drinks_tbl)
    loadData("preferences_tbl",preferences_tbl)


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
    print(remove_drink + " has been removed")


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


def addPreferences(people_id, drinks_id):
    return


def modify_preferences(person_id, drinks_id):
    return


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


def save_data(filename, dictionary): 
    try:
        with open(filename + ".txt", 'w') as dictionary_file:
            for key, value in dictionary.items():            
                dictionary_file.write(f"{key} {value}\n")        
    except Exception as e:
        print("Unable to save: " + str(e))
    
def clearScreen():
    os.system("clear")

#  Applications start now
startOperation()

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
            clearScreen()
            display_table(people_tbl, " People", False)
            person_id = input("Which persons preference would you like to update? ")
            clearScreen()
            display_table(drinks_tbl, " Drinks", False)
            drinks_id = input(f"Which drink is {people_tbl.get[person_id]} preference? ")
        else:
            menuReturn()

    elif user_input == "7":
        clearScreen()
        display_table(people_tbl, "Delete Person ", False)
        remove_person_input = input("Select ID to remove: ")
        remove_person(remove_person_input)


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
        save_data("people_tbl",people_tbl)
        # save_data("drinks_tbl",drinks_tbl)
        # save_data("preferences_tbl",preferences_tbl)
        exit()

    else:
        print("Incorrect menu choice")
