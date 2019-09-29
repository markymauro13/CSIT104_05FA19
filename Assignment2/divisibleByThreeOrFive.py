# Author: Mark Mauro        9/26/19
# This is a fizzbuzz program

num = int(input("enter a number: "))   # let user enter a number

if num % 3 == 0 and num % 5 == 0:   # checks if num is both a multiple by 3 and 5
    print(str(num) + " is a multiple of both 3 and 5")
elif num % 3 == 0:  # checks if num is only divisible by 3
    print(str(num) + " is a multiple of 3")
elif num % 5 == 0:  # checks if num is only divisible by 3
    print(str(num) + " is a multiple of 5")
else:
    print(str(num) + " is not a multiple of 3 and 5")   # prints when num is not a multiple of either 3 or 5
