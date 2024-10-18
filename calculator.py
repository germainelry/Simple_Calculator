import argparse

# Define basic arithmetic functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Define the main calculator function
def calculator(operation, num1, num2):
    if operation == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif operation == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif operation == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif operation == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input")

# The main section of the script
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Calculator")

    # Define the arguments the script will accept
    parser.add_argument("operation", nargs='?', help="Operation: 1 (Add), 2 (Subtract), 3 (Multiply), 4 (Divide)")
    parser.add_argument("num1", nargs='?', type=float, help="First number for the calculation")
    parser.add_argument("num2", nargs='?', type=float, help="Second number for the calculation")

    # Parse the arguments from the command line
    args = parser.parse_args()

    # Check if arguments were provided
    if not args.operation or not args.num1 or not args.num2:
        # If arguments are missing, prompt the user for input interactively
        print("Simple Calculator~")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        
        operation = input("Enter choice (1/2/3/4): ")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    else:
        # If arguments are provided, use them
        operation = args.operation
        num1 = args.num1
        num2 = args.num2

    # Call the calculator function with the values (either from command line or input)
    calculator(operation, num1, num2)
