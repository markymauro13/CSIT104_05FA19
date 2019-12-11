#1, write a program that will print only the odd index characters in a string starting from 0 index

x = input("Enter a string")

for i in range(0,len(x)):
     if i % 2 == 0:
         print(x[i], end='')

#2, What will be the output of the following code?

#a
x = 'A'
ch = chr(ord(x)+3)
print(ch)

#b
sum = 2+3
print(sum)
s = '2' + '3'
print(s)

#c
s1 = "Welcome to Python"
s2 = "to"

#What are the results of the following

print("Welco" in s1)     # prints true

print("Welco" not in s1) # prints true

#d

s1 = "Welcome to Python"

#What are the results of the following

print(s1.count("o"))     # prints 3
print(s1.count("ao"))    # prints 0
print(s1.find("Python")) # prints 11
print(s1.startswith("Welco")) # prints True
print(s1.endswith("on"))      # prints True
print(s1.replace("o", "abc")) # prints "Welcabcme tabc Pythabcn"
print(s1) # prints "Welcome to Python"

#e

number = 6
while number >0:
     number -= 3
     print(number, end = '')

#3 How many times the following loops will execute

#a

count = 5
while count < 50:
     count+=5
# executes 9 times, 45/5

for count in range(100):
     print(count)
     
#4 Write a program using nested loop to print 12345-1234-123-12-1

i = 5
while i >= 1:
     for j in range(i,i+1):
          print(j, end = '')
     print()
     i-=1
     
#5 What will be the output of the following program

#a

balance = 1000
while True:
     if balance < 9:
          break
     balance = balance - 9
print("Balance is", balance)

#b, Suppose a function is as follows:

def f(p1,p2=5,p3=5,p4=1):
     return p1+p2+p3+p4
print(f(1,p2=3,p3=4,p4=4))    #This is correct, OUTPUT = 12
print(f(1,p2=3,4,p4=4))       #This is incorrect, will result in error
print(f(p1=1,p2=3,4,p4=4))    #This is incorrect, will result in error
print(f(1,4,4))               #This is correct, OUTPUT = 10
print(f(p4=1,p2=3,p3=4,p1=4)) #This is correct, OUTPUT = 12

#c, What will be the output of the following code

def m(n):
     n+=1
def main():
     n = 1
     m(n)
     print(n)
main()

#6 Write a python program that will print the reverse of a string. For example, if the given string is "python", it will print "nohtyp"

x = input("Enter a string:")
print(x[::-1]) # reverses string

#7 Write a python function that will take a string as a parameter and then return that string in uppercase. For example if the given parameter
# is "msu" it will return "MSU" which will be printed by the caller

def toUpper(str):
     return str.upper()
print(toUpper("msu"))    # will return "MSU"





