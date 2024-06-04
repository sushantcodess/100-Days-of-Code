#creating a simple calculator program
from logo import asciii
print(asciii)

#add
def add(n1, n2):
    return n1 + n2

#subtraction
def subtract(n1, n2):
    return n1 - n2

#multiplication
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2

dict = {}
dict["+"] = add
dict["-"] = subtract
dict["*"] = multiply
dict["/"] = divide

def calculator():
    n1 = float(input("What's the first number?\n "))
    to_continue = "yes"
    while to_continue == "yes":
        operations = []
        for i in dict:
            operations.append(i)
        operation_chosen = input(f"What operation would you like to perform? \n{operations}\n ")
        n2 = float(input("What's the next number?\n "))

        answer = dict[operation_chosen](n1=n1, n2=n2)
        print(f"{n1} {operation_chosen} {n2} = {answer}")

        option = input(f"Do you want to continue with {answer} or start a new calculation? Type 'c' for current or 'n' for new\n")

        if option == "current":
            n1 = answer
        elif option == "new":
            calculator()
        else:
            print("Enter a valid choice!")
            to_continue = "no"
calculator()
    