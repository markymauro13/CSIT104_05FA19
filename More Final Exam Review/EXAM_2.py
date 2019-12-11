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
