
userInput = input("what day is today")

if userInput == ("Monday"):
    print('today is Monday')
elif userInput == "Tuesday":
    print("today is Tuesday")
elif userInput == "Thursday":
    print("Thursday is a good day")
else:
    print("Today is a holiday")

name = input("what is your name?" )

while name == "":
    print("You did not enter your name")
    name = input("Enter your name problem")

print(f'Hello {name}')




