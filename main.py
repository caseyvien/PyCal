import re

run = True
previous = 0

def compute(equation):
    global run
    global previous
    if equation == "quit":
        run = False
    elif previous == 0:
        previous = ""
    else:
        equation = re.sub("[A-Za-z]","",equation)
    previous = eval(str(previous)+equation)
    print(previous)

print("WELCOME TO PyCAL\n")
print("Enter text:")

while run:
    equation = input()
    compute(equation)

print("Thank you for using PyCal")

