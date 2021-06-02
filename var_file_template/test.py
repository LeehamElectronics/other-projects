# input text
input_dictionary = {"one": 1, "two": 2}

# open file
file = open("Python.txt", "w")

# convert variable to string
str = repr(input_dictionary)
file.write("input_dictionary = " + str + "\n")

# close file
file.close()

f = open('Python.txt', 'r')
if f.mode == 'r':
    contents = f.read()