sum = 0
i = 0

while i < 100:  # do this while i is less than 100
    i += 1  # add one to start at 1
    if i % 2 == 0:
        continue    # skips every other even number
    sum += i
    print(str(sum))


