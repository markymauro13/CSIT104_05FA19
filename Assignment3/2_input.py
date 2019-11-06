x = str(input("What's your favorite novel: "))  # ask use for input
line = str(input("Enter a line: "))

print("My favorite novel is: " + x.upper())    # change x to uppercase
print("MY favorite novel is: " + x.lower())    # change x to lowercase
print("The result string after split is: " + str(line.split())) # print the result of the split
print("The result string after replacing e with & is: " + line.replace('e','&'))    # replace the 'e''s in variable line with '&'