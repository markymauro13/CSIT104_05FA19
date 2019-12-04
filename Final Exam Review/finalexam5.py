
# wrong

'''user = ""
sumOfThem = ""
while user != 'Q':
    user = input("Enter something: ")
    sumOfThem += user

print(sumOfThem)    
'''

# good


num = str(input("Enter a number: "))
sum = 0

while("Q" not in num):
    sum+= eval(num)
    print(sum)
    num = str(input("Enter a number: "))

# good

total = 0

while True:
    num = input("Enter a number, Q to stop: ").strip()
    if num.upper() == "Q":
        break
    else:
        total += int(num)
        print("Total is", total)
