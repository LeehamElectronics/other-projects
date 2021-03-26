type = 7

# Python Strings https://www.w3schools.com/python/python_strings.asp
if type == 1:
    a = """test 
    123"""  # multi line strings
    print(a)
    print(a[0])  # strings are arrays
    if len(a) > 1:  # length of a string, use the len() function.
        for x in a:  # Since strings are arrays, we can loop through the characters in a string, with a for loop.
            print(x)
        print("test" in a)  # Check if "free" is present or use not in to see if its not there
    if "free" in a:  # check can be used in if
        print("Yes, 'test' is present.")

# Slicing Strings
if type == 2:
    a = "hello, world!"  # first character has index 0.
    print(a[:5])  # gives the first five
    print(a[2:])  # from 2 to the end
    print(a[-5:-2])  # -2 removes 2 from the end and -5 means include form char 5 to the end

# modify Strings
if type == 3:
    a = "  hello, world!  "
    print(a.upper())  # all upper case
    print(a.lower())  # all lower case
    print(a.strip())  # removes white space from start and end
    print(a.replace("h", "J"))  # replaces first char with the second
    print(a.replace(" ", ""))  # can be used to remove blank space
    print(a.split(","))  # returns ['Hello', ' World!']

# String Concatenation
if type == 4:
    a = "Hello"
    b = "World"
    c = a + " " + b
    print(c)

# Format - Strings
if type == 5:
    quantity = 3  # index 1
    itemno = 567  # index 2
    price = 49.95  # index 3
    myorder = "I want to pay {2} dollars for {0} pieces of item {1}."  # {1} means put index one here so if makes sure they go in the write spots
    print(myorder.format(quantity, itemno,
                         price))  # grab variable and put it in the string if indexed put it there other wise first goes first

# Escape Character
if type == 6:
    txt = "We are the so-called \"Vikings\" from the north."  # The escape character allows you to use double quotes when you normally would not be allowed
    print(txt)  # there are other escape characters look them up

# String Methods
if type == 7:  # dont work just look and find what you want online
    a = "hello,  world!"
    a.capitalize() #  Converts the first character to uppercase
    a.casefold()
    a.center(20)
    a.count("hell")
    a.encode()
    a.endswith()
    a.expandtabs()
    a.find()
    a.format()
    a.format_map()
    a.index()
    a.isalnum()
    a.isalpha()
    a.isdecimal()
    a.isdigit()
    a.isidentifier()
    a.islower()
    a.isnumeric()
    a.isprintable()
    a.isspace()
    a.istitle()
    a.isupper()
    a.join()
    a.lstrip()
    a.maketrans()
    a.partition()
    a.replace()
    a.rfind()
    a.rindex()
    a.rpartition()
    a.rsplit()
    a.rstrip()
    a.split()
    a.splitlines()
    a.startswith()
    a.swapcase()
    a.title()
    a.translate()
    a.upper()
    a.zfill()