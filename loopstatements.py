#looping statements in Python - used to execute a block of code repeatedly, types of loops include for loop and while loop
#for loop - used to iterate over a sequence (like a list, tuple, dictionary, set, or string), it is used when the number of iterations is known
for  number in range(3):
    print("Attempt")
    print("Attempt",number)
    print("Attempt",number + 1)
    print("Attempt",number + 1, (number + 1) * ".")
for number in range(1,4):
    print("Attempt",number, number * ".")
for number in range(1,10,2): #step value of 2
    print("Attempt",number, number * ".")
for number in range(10,0,-1): #counting backwards
    print("Attempt",number, number * ".")
for x in "Python":
    print(x)
for x in [1,2,3,4,5]:
    print(x)
for item in shopping_cart: # pyright: ignore[reportUndefinedVariable]
    print(item)

# for else loop - else block will be executed when the loop is completed normally without encountering a break statement
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# nested for loop - a loop inside another loop
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")
for x in range(5):
    print(x)

# while loop - used to execute a block of code as long as a condition is true, it is used when the number of iterations is not known
number = 100
while number > 0:
    print(number)
    number //= 2    
print("Done")

#command = ""
#while command != "quit":
#    command = input(">")
#    print("ECHO", command)'''

#command = ""
#while command != "quit" and command != "QUIT":
#    command = input(">")
#    print("ECHO", command)

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

# infinite loop - a loop that never ends, usually caused by a condition that is always true
while True:
    command = input(">")
    if command.lower() == "quit":
        break
    print("ECHO", command)

