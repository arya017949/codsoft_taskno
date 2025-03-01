def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract y from x."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide x by y."""
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def calculator():
    print("Arithmetic Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    while True:
        choice = input("Enter your choice (1/2/3/4) or 'q' to quit: ")
        
        if choice.lower() == 'q':
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please choose a valid option.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            try:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ZeroDivisionError as e:
                print(e)

if __name__ == "__main__":
    calculator()
