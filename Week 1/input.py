import os
os.system("clear")

get_people = ['Billy', 'Connor', 'Bob']
get_drinks = ['Coffee', 'Corona', 'Motor oil']


def display_menu():
    # os.system("clear")
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
        5. Exit BrIW :(
        '''
    print(menu_text)


def menuReturn():
    menu_return = input("Return to main menu? Y / N: ").upper()
    if menu_return == 'Y':
        os.system("clear")
    else:
        print("Goodbye!")
        exit()

def display_table(rows,title):
    print("+============\n|" + title + "\n+============")
    for row in rows:
        print("| " + row)
    print("+============")

# print(f"+{'=' * 25}+")

def addPerson(new_person):
    get_people.append(new_person.capitalize())
    print(new_person.capitalize() + "has been added")


def addDrink(new_drink):
    get_drinks.append(new_drink.capitalize())
    print(new_drink.capitalize() + "has been added")


def stringCheck(input_string):
    stringIsAlpha = input_string.isalpha()
    while stringIsAlpha == False:
        input_string = input("None alphabetical characters entered - try again: ")
        stringIsAlpha = input_string.isalpha()
    return input_string


while True:
    display_menu()
    user_input = input("Please enter your input: ")

    if user_input == "1":
        os.system("clear")
        display_table(get_people, " People")
        menuReturn()

    elif user_input == "2":
        os.system("clear")
        display_table(get_drinks, " Drinks")
        menuReturn()

    elif user_input == "3":
        os.system("clear")
        new_person = input("What is the persons name, you\'d like to add? ")
        new_person = stringCheck(new_person)
        addPerson(new_person)

    elif user_input == "4":
        os.system("clear")
        new_drink = input("What is the drink you\'d like to add? ")
        new_drink = stringCheck(new_drink)
        addDrink(new_drink)

    elif user_input == "5":
        exit()
    else:
        print("Incorrect menu choice")
