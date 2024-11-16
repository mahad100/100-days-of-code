#import art
#create 4 functions: add subtract,multiply and divide
import art


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# add these four functions into a dictionary
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
# not using parenthesis because we are not triggering the functions
# just storing them
}
def calculator():
    print(art.logo)
    again = True
    num1 = float(input("What's the first number?"))
    while again:
        operator = input("+\n-\n*\n/\npick an operation")
        num2 = float(input("Whats the next number"))


        if operator == "+":
            print(f"{num1}+{num2} = {operations["+"](num1, num2)})")
            answer = operations["+"](num1, num2)
        elif operator == "-":
            print(f"{num1}-{num2} = {operations["-"](num1, num2)})")
            answer = operations["-"](num1, num2)
        elif operator == "*":
            print(f"{num1}*{num2} = {operations["*"](num1, num2)})")
            answer = operations["*"](num1, num2)
        elif operator == "/":
            print(f"{num1}/{num2} = {operations["/"](num1, num2)})")
            answer = operations["/"](num1, num2)
        next_operation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation")
        if next_operation == 'y':
            num1 = answer
        else:
            calculator()
calculator()



######








# def add(n1, n2):
#     return n1 + n2
#
# def subtract(n1, n2):
#     return n1 - n2
#
# def multiply(n1, n2):
#     return n1 * n2
#
# def divide(n1, n2):
#     return n1 / n2
#
# operations = {
#     "+" : add,
#     "-" : subtract,
#     "*" : multiply,
#     "/" : divide
#
# }
# def calculator():
#     should_accumulate = True
#     num1 = float(input("What is your first number?:"))
#
#     while should_accumulate:
#         for symbol in operations:
#             print(symbol)
#         operation_symbol = input("Pick an operation:")
#         num2 = float(input("What is your next number?:"))
#         answer = operations[operation_symbol](num1, num2)
#         print(f"{num1} {operation_symbol} {num2} = {answer}")
#         choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation")
#         if choice == 'y':
#             num1 = answer
#         else:
#             should_accumulate = False
#             print("\n" * 20)
#             calculator()
#
# calculator()





