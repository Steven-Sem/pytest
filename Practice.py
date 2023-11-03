# Programming with Python
x = (5)
print(x)
      
#Area of a Circle
pi = 3.14159
radius = 2.2
area = pi*(radius**2)
print(area)

## EXAMPLE: input
#######################
text = input("Type anything... ")
print(5*text)
num = int(input("Type a number... "))
print(5*num)

Monday = 1000
Tuesday = 2000
Wednesday = 3000

print("Monday's sales are", Monday,
      "and Tuesday's sales are", Tuesday,
      "and Wednesday's sales are", Wednesday)

firstname = "Steven"
lastname = "Sem"
message = "My name is" + " " + firstname + " " + lastname
print(message)

firstname = input("Enter your firstname")
lastname = input("Enter your lastname")
message = "My name is" +" " + firstname + " " + lastname
print(message)

##EXAMPLE: conditionals/branching
x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
    print("x and y are equal")
    if y != 0:
        print("therefore, x / y is", x/y)
elif x < y:
    print("x is smaller")
elif x > y:
    print("y is smaller")
print("thanks")


userInput = input("Give me the first string")
userInput2 = input("Give me the second string")

if userInput == "Monday" and userInput2 == 'Sunny':
    print("today is a sunny day")
else:
    print('haha dem dem')


    #for fruits looping
    fruits = ['orange' 'mango' 'banana']

    for fruit in fruits: 
        print (f'{fruit}')


name = input("what is your name?" )

while name == "":
    print("You did not enter your name")
    name = input("Enter your name problem")

print(f'Hello {name}')