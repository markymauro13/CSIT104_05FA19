#5a

count = 0
n = 10

while count < n:    # runs n amount of times
    count += 1
    print(count)
print("count is: " + str(count))

#5b

for count in range(n):  # runs for n times
    print(count)
    count += 1

print("count is: " + str(count))

#5c

count = 5

while count < n:   # runs n - 5 times
     count += 1
