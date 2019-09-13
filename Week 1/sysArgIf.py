import sys
arguments = sys.argv

get_people = ['Billy', 'Connor', 'Bob']
get_drinks = ['Coffee', 'Corona', 'Motor oil']

if len(arguments) == 2:
    if arguments[1] == "get-people":
        print(get_people)
    elif arguments[1] == "get-drinks":
        print(get_drinks)
    else:
        print("Incorrect argument")
else:
    print("Unexpected argument(s) - Too little too many")