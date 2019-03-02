import re

run = True
hold = 0
print("Welcome to the Magical calculator")


def performcalculation():
    global run
    global hold
    equation = ''
    if hold == 0:
        equation = input("Enter Equation")
    else:
        equation = input(str(hold))

    if equation == "quit":
        print("Thanks for using the program and GoodBye")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:;&=()"]', '', equation)

        if hold == 0:
            hold = eval(equation)
        else:
            hold = eval((str(hold)) + equation)


while run:
    performcalculation()
