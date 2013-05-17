#If you're new to Python, have fun with this code.

name = raw_input("What's your name? ")
name = name.capitalize()

if name.isalpha() and len(name) > 0:
    print "Hello " + name + "!"
else:
    print "Invalid input"
