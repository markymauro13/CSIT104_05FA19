# Author: Mark Mauro    9/26/19

num = int(input("Enter a number: "))

# was not sure if negative numbers needed to be included

if num <= -1 and num >= -9:     # checks amount of digits for negative numbers. restraints: digits > 4 are ot allowed
    print(str(num) + " is a 1-digit number")
elif num <= -10 and num >= -99:
    print(str(num) + " is a 2-digit number")
elif num <= -100 and num >= -999:
    print(str(num) + " is a 3-digit number")
elif num <= -1000 and num >= -9999:
    print(str(num) + " is a 4-digit number")
elif num >= 0 and num <= 9:     # checks amount of digits for positive numbers. restraints: digits > 4 are ot allowed
    print(str(num) + " is a 1-digit number")
elif num >= 10 and num <= 99:
    print(str(num) + " is a 2-digit number")
elif num >= 100 and num <= 999:
    print(str(num) + " is a 3-digit number")
elif num >= 1000 and num <= 9999:
    print(str(num) + " is a 4-digit number")
else:
    print(str(num))    # prints invalid user input
          
