import math

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def power(num1, num2):
    return num1 ** num2

def square_root(num):
    return math.sqrt(num)

def calculate():
    print("Advanced Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("0. Exit")

    while True:
        choice = input("Enter operation number (0-6): ")

        if choice == '0':
            print("Calculator is closing...")
            break

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            if num2 == 0:
                print("Error: Cannot divide by zero")
            else:
                print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", power(num1, num2))
        elif choice == '6':
            if num1 < 0:
                print("Error: Cannot calculate square root of a negative number")
            else:
                print("Result:", square_root(num1))
        else:
            print("Invalid input. Please enter a number between 0 and 6.")

        print()  # Print an empty line for separation

calculate()
