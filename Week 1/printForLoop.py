import sys

arguments = sys.argv

get_people = ['Billy', 'Connor', 'Bob']
get_drinks = ['Coffee', 'Corona', 'Motor oil']

if len(arguments) == 2:
    if arguments[1] == "get-people":
        print("+============\n| People\n+============")
        for person in get_people:
            print("| " + person)
        print("+============")
    elif arguments[1] == "get-drinks":
        print("+============\n| Drinks\n+============")
        for drink in get_drinks:
            print("| " + drink)
        print("+============")
    else:
        print("Incorrect argument")
else:
    print("Unexpected argument(s) - Too little too many")