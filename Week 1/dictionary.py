# Preferences table links peoples key ID with a drink ID.

import os
os.system("clear")

people_tbl = {1: 'Billy', 2: 'Connor', 3: 'Chris'}
drinks_tbl = {1: 'Latte', 2: 'Mochiato', 3: 'Beer'}
preferences_tbl = {}

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
        6. Modifty preferences
        X. Exit
        '''
    print(menu_text)


def menuReturn():
    menu_return = input("Return to main menu? Y / N: ").upper()
    if menu_return == 'Y':
        os.system("clear")
    elif menu_return == 'N':
        print("Goodbye!")
        exit()

def display_table(rows,title):
    print(f"+{'=' * 25}+")
    print(title.upper())
    print(f"+{'=' * 25}+")
    for key, value in rows.items():
        # print("| " + row[key] + " " + row[value])
        print(f" | {key} - {value}")
    print(f"+{'=' * 25}+")


def addPerson(new_person):
    person_id = list(people_tbl.keys())[-1] + 1
    people_tbl[person_id] = new_person.capitalize()
    print(new_person.capitalize() + " has been added")


def addDrink(new_drink):
    drink_id = list(people_tbl.keys())[-1] + 1
    drinks_tbl[drink_id] = new_drink.capitalize()
    print(new_drink.capitalize() + " has been added")


def removePerson(remove_person):
    print(remove_person + " has been removed")


def removeDrink(remove_drink):
    print(remove_drink + " has been removed")


def stringCheck(input_string):
    stringIsAlpha = input_string.isalpha()
    while stringIsAlpha == False:
        input_string = input("None alphabetical characters entered - try again: ")
        stringIsAlpha = input_string.isalpha()
    return input_string


def addPreferences():
    return


def modifyPreferences():
    return


def clearScreen():
    os.system("clear")

while True:
    display_menu()
    user_input = input("Please enter your input: ")

    if user_input == "1":
        clearScreen()
        display_table(people_tbl, " People")
        menuReturn()

    elif user_input == "2":
        clearScreen()
        display_table(drinks_tbl, " Drinks")
        menuReturn()

    elif user_input == "3":
        clearScreen()
        new_person = input("What is the persons name, you\'d like to add? ")
        new_person = stringCheck(new_person)
        addPerson(new_person)

    elif user_input == "4":
        clearScreen()
        new_drink = input("What is the drink you\'d like to add? ")
        new_drink = stringCheck(new_drink)
        addDrink(new_drink)
    
    elif user_input == "5":
        clearScreen()
        display_table(preferences_tbl, " Preferences")

    elif user_input == "6":
        clearScreen()
        print("Updating preferences coming soon")

    elif user_input == "X":
        exit()

    else:
        print("Incorrect menu choice")
