x = str(input("Enter a string: "))  # ask for input from user

if(len(x)>0):
    print("The length of string is: " + str(len(x)))  # print the length of the string
    print("The resulted string is: " + str(x[-1]) + str(x[1:len(x) - 1]) + str(x[0]))  # print the result of the modified string
else:
    print("Try again, enter a valid string.")   # need this because an error would happen if i didnt enter a string and just hit enter

