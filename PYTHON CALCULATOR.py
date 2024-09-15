# Basic Calculator in Python with Controlled Input Loop

print("This is a basic Python calculator so you can expand upon this as you please.")
print("All functions are listed as actions, which will show on the terminal upon F5 or ctrl + F5 command.")
# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

# Main function that runs the calculator
def calculator():
    while True:  # This loop keeps the program running until the user exits
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        # Take input from the user
        choice = input("Enter choice (1/2/3/4/5): ")
        
        # Exit if the user selects '5'
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break  # Stops the loop and exits the program
        
        # Handle valid inputs
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

# Call the calculator function to start the program
calculator()
