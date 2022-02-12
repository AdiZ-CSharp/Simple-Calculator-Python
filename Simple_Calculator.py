from Functions import *

answer = 0.0

num1 = float(input("Enter a starting number: "))

operation = input("Add:     \"Add\" or \"a\"\nSubtract:     \"Subtract\" or \"s\"\nMultiply:     \"Multiply\" or \"m\"\nDivide:     \"Divide\" or \"d\"\nSquare:     \"Square\"\nCube:     \"Cube\"\n\nEnter an operation: ").lower()

if operation == "square" or operation == "cube":
    answer = square_or_cube(operation, num1)
    print_answer(answer)

num2 = float(input("Enter a second number: "))

if operation in ("a", "add", "s", "subtract", "m", "multiply", "d", "divide"):
    answer = do_calc(operation, num1, num2)
    print_answer(answer)
else:
    wrong_operation(operation)