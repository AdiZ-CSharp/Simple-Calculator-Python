import sys

def do_calc(operation, num1, num2):
    
    match operation:
        
        case "a" | "add":
            return num1 + num2
        case "s" | "subtract":
            return num1 - num2
        case "m" | "multiply":
            return num1 * num2
        case "d" | "divide":
            return num1 / num2

def print_answer(answer):
    
    print("The answer to your calculation is " + str(answer))
    sys.exit()

def square_or_cube(operation, num1):
    
    match operation:
        
        case "square":
            return num1 * num1
        case "cube":
            return num1 * num1 * num1

def wrong_operation(operation):
    
    print("Sorry, " + operation + " is not a valid operation.")