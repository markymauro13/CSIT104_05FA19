def addition(x,y):
    return x+y
    
def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    if y == 0:
        print("Error. Division by zero")
    else:
        return x/y

print(" 1. Add 2. Subtract 3. Multiply 4. Division ")

choice = int(input("Pick your category by typing 1-4: "))   # first show menu to user

while choice != 0:  # if 0 entered exit the program
    if (choice == 1):
        x = int(input("Enter a number: "))
        y = int(input("Enter a number: "))
        print(addition(x,y))
    elif(choice == 2):
        x = int(input("Enter a number: "))
        y = int(input("Enter a number: "))
        print(subtract(x,y))
    elif(choice == 3):
        x = int(input("Enter a number: "))
        y = int(input("Enter a number: "))
        print(multiply(x,y))
    elif(choice == 4):
        x = int(input("Enter a number: "))
        y = int(input("Enter a number: "))
        print(divide(x,y))

    choice = int(input("Pick your category by typing 1-4: "))
