# Calculator logic Functions 

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def clear():
    print("\nCalculator cleared!")


# User Input & Menu

def get_number(Prompt):
    # Get a number from the user.
    while True:
        value = input(Prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid number! Please enter a valid numeric value.")


def calculate():
    """Handles one complete calculation cycle."""
    num1 = get_number("Enter first number: ")
    operator = input("Enter operator('+','-','*','/'): ")

    if operator not in ['+','-','*','/']:
        print("Invalid operator!")
        return
    
    num2 = get_number("Enter second number: ")

    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)

    print("Result:", result)

def menu():
    while True:
        print("\n Simple Calculator Menu ")
        print("1. Perform Calculation")
        print("2. Clear")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            calculate()
        elif choice == '2':
            clear()
        elif choice == '3':
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Start Program
menu()
