import sys
arguments = sys.argv
print(arguments)

person = arguments[1]
drink  = arguments[2]
message = person + "'s favourite drink is " + drink
print(message)