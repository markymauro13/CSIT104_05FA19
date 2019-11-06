x = "Computational Concepts 1"
y = "MSU"

# What are the results of the following expressions?
# a. How many ‘o’ in string x?
# b. How can you find the substring “Concepts” in x?
# c. How can you check if y starts with “M”?
# d. How can you replace “MSU” in y with “Montclair State University”?

#a

print(x.count('o'))

#b

print(x.find("Concepts"))

#c

print(y.startswith('M'))

#d

print(y.replace("MSU", "Montclair State University"))



