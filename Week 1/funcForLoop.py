import sys

arguments = sys.argv

get_people = ['Billy', 'Connor', 'Bob']
get_drinks = ['Coffee', 'Corona', 'Motor oil']
get_chocobars = ["Kit Kat", "Snickers", "Mars"]


def display_table(rows,title):
    print("+============\n|" + title + "\n+============")
    for row in rows:
        print("| " + row)
    print("+============")

command = arguments[1]

if len(arguments) == 2:
    if command == "get-people":
        display_table(get_people, " People")
    elif command == "get-drinks":
        display_table(get_drinks, " Drinks")
    elif command == "get-chocobars":
        display_table(get_chocobars, " Choco bars")
    else:
        print("Incorrect argument")
else:
    print("Unexpected argument(s) - Too little too many")