# conditional statements - used to make decisions in code, here we use if, elif, and else statements and sometimes switch
#if statements - used to execute a block of code if a specified condition is true
age = 18
if age >= 18:
    print("You are an adult.")  
temperature = 35
if temperature > 30:
    print("It's warm")
    print("Drink water")
print("Done")
# if-else statements - used to execute one block of code if a condition is true, and another block if it is false
age = 16    
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")   
number = 10
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")  
#elif statements - used to check multiple conditions
temperature = 35
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")
#if-elif-else statements - used to check multiple conditions and provide a default action if none are met
score = 85
if score >= 90:
    print("Grade: A")   
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")   
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
# switch statements - Python does not have a built-in switch statement, but we can use dictionaries to simulate one
def switch_example(day):
    switcher = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return switcher.get(day, "Invalid day") 
day = 3
print(switch_example(day))  # Output: Wednesday 
day = 8
print(switch_example(day))  # Output: Invalid day
day = 5
print(switch_example(day))  # Output: Friday
day = 1
print(switch_example(day))  # Output: Monday
day = 10
print(switch_example(day))  # Output: Invalid day
day = 6
print(switch_example(day))  # Output: Saturday
day = 2
print(switch_example(day))  # Output: Tuesday
day = 4
print(switch_example(day))  # Output: Thursday
day = 7
print(switch_example(day))  # Output: Sunday
day = 0
print(switch_example(day))  # Output: Invalid day
day = 9
print(switch_example(day))  # Output: Invalid day
# End of conditionalstatements