#1,
# 101 + 11 = ?
#   111 + 111= ?
#   1010 + 1010 = ?
#   11101 + 1010 = ?
#   11111 + 11111 = ?
#   (1111)_2 = (?)_10

#2,   Which of the following identifiers are valid? Which are Python Keywords
# miles, Test, a+b, b-a, 4#R, $4, #44, apps, if, elif, x, y, radius
print("valid: miles, Test, apps, x, y, radius")
print("invalid: a+b, b-a, 4#R, #44, if, elif")

print("----------------")
#3,
print(2*(5//2+5//2))    # prints 8
print(2*5//2+2*5//2)    # prints 10
print(2*(5//2))         # prints 4
print(2*5//2)           # prints 5

print("----------------")
#4    What is the value of i printed
j=i=1
i += j + j * 5
print("What is i?", i)  # i is equal to 7


print("----------------")
#5,   Write a program that obtains minutes and remaining seconds from seconds
x = int(input("Enter amount of seconds: "))
minutes = x // 60
seconds = x % 60
print(str(minutes) + " minutes and " + str(seconds) + " seconds")

print("----------------")

#6,
radius = 1
print(radius > 0)
lightsOn = True
print(lightsOn)
print(int(True))
print(bool(0))
b = (1 > 2)
print(b)
#Numerically True is represented as 1, False is represented as 0

print("----------------")
#7, Write a program that assigns a value to a variable. Then it checks if the value of the variable is even. If the value is even, it will print "EVEN"
x=2
if(x % 2 == 0):
    print("even")

print("----------------")
#8,  Write a program that checks if a number is positive. If the number is positive, it will print "Positive"
y = 2
if(y > 0):
    print("Positive")

print("----------------")
#9, Write a program that assigns a value to a variable. Then it checks if the value of the variable
# is even or odd. If the value is even, it will print "EVEN", otherwise, it will print "ODD"
z = 2
if(z % 2 == 0):
    print("EVEN")
else:
    print("ODD")


print("----------------")
#10, Set a variable temperature wtih a value. Then display the following message
#   "Too hot" if temperature is greater than 99
#   "Too cold" if the temperature is less 40
#   "Just right" otherwise

temperature = 60
if(temperature > 90):
    print("Too hot")
elif(temperature < 40):
    print("Too cold")
else:
    print("Just right")


print("----------------")
#11, Assuming that x is 1, show the result of the following Boolean expressions.

x=1
print(True and (3>4))   # False
print((not(x>0)) and (x>0)) # False
print((x>0) or (x<0))   # True
print((x!=0) or (x==0)) # True
print((x>=0) or (x<0))  # True
print((x!=1)==(not(x==1)))  # True



print("----------------")

#12, Rewrite the following if statements using a conditional expression.
ages = 0
if ages >= 16:
    ticketPrice = 20

else:
    ticketPrice = 10

# conditional version
print(ticketPrice, 0 if (ages >= 16) else 10)

print("----------------")

#13, what will be printed?
print(2 * 2 - 3 > 2 and 4 - 2 > 5)  # prints False
print(2 * 2 - 3 > 2 or 4 - 2 > 5)   # prints False


print("----------------")

#14, Which of the following statement prints smith\exam1\test.txt?
#print("smith\exam1\test.txt")
#print("smith\\exam1\\test.txt")
#print("smith\"exam1\"test.txt")
#print("smith"\exam1"\test.txt")

print("smith\\exam1\\test.txt")



print("----------------")

#15, What will be displayed by the following code?
print("A", end = '')
print("B", end = '')
print("C", end = '')
print("D", end = '')


print()
print("----------------")
#16, Suppose that s1 and s2 are two strings, given as follows:

s1 = "Welcome to Python"
s2 = "to"


print(s1==s2)   # prints False
print(s1<=s2)   # prints True, t comes before W in the dictionary
print(s1>=s2)   # prints False, W does not come before t in the dictionary
print(s1!=s2)   # prints True



print("----------------")
#17, Write a program that will check if a given string has even or odd number of characters.
string = "string"
if(len(string) % 2 == 0):
    print("even amount of characters")
else:
    print("odd amount of characters")


print("----------------")
#18, What are the results of the following expressions?
s1 = "Welcome to Python"
print(s1[4:8])  # prints everything from index 4 to 8-1
print(s1[4:4])  # prints everything from index 4 to 4 - 1, which is nothing
print(s1[-3:-1])    # prints everything from index -3, (len(s1) - 3) to -1, (len(s1)-1)
#print(len(s1)-1)
#print(len(s1)-3)



print("----------------")
#19, Write a program that will add ‘#’ at the beginning and end of a string.
print('#' + "string" + '#')


print("----------------")
#20, Write a program that will print only the even index characters in a string starting from 0 index.

# easy way
x = "string"
print(x[::2])

print()

# harder way
for i in range(0, len(x)):
    if i % 2 == 0:
        print(x[i], end = '')


print()
print("----------------")

#21, How many times are the following loop bodies repeated? What is the printout of each loop?

'''
i = 1
while i < 10:
    if i % 2 == 0:
        print(i)
'''

'''
i = 1
while i < 10:
    if i % 2 == 0:
    print(i)
    i += 1
'''
i = 1
while i < 10:
    if i % 2 == 0:      # this is the correct one
        print(i)
    i += 1


print("----------------")
#22, Can you always convert any while loop into a for loop? Convert the following while loop into a for loop.

i = 1
sum = 0
while sum < 10000:
    sum = sum + i
    i += 1
print(sum)

print('-')

sum = 0
for i in range(0, 10000):
    sum += i
print(sum)

print("----------------")
#23, Print the following pattern:

'''
1
12
123
1234
12345
123456

'''
for i in range(1, 7):
    for j in range(1, i+1):
        print(j, end = '')
    print()

print("----------------")
#24, Write a Python program to get the smallest number from a list

# easy way
list = [1,2,3]
print(min(list))

# hard way

list = [1,2,3]
smallest = list[0]
position = 0
for i in range(1,len(list)):
    if(smallest > list[i]):
        smallest = list[i]
        position = i

print("The smallest element in this list is " + str(smallest))
print("The Index position of the Smallest Element is : " + str(position))


print("----------------")
#25,Write a Python program to print the even index items in a list

# easy way
list = [1,2,3]
print(list[::2])    # printed as a list though


print("---")
# hard way

list = [1,2,3]
for i in range(0, len(list)):
    if i % 2 == 0:
        print(list[i], end = ' ')

print()
print("----------------")