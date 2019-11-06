state1 = str(input("First State: "))    # ask for input from user
state2 = str(input("Second State: "))
state3 = str(input("Third State: "))

stateList = (state1.title(), state2.title(), state3.title())    # added lower() so there is no issue comparing captial and lowercase letters
newStateList = sorted(stateList)    # set the sorted list to a new list

print("The three states in alphabetic order are: " + str(newStateList[0]) + ", " + str(newStateList[1]) + ", " + str(newStateList[2]))  # print the result