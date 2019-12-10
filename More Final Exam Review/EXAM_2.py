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
