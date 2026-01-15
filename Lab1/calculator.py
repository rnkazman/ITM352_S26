"""
Simple Calculator Program
Performs basic math operations with error handling
"""

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers with zero division check"""
    if y == 0:
        return None
    return x / y

def main():
    """Main calculator function"""
    print("=" * 40)
    print("        Simple Calculator")
    print("=" * 40)
    
    try:
        # Get user input for numbers
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Display operation options
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        
        # Get operation choice
        choice = input("\nEnter operation (1/2/3/4): ")
        
        # Perform calculation based on choice
        if choice == '1':
            result = add(num1, num2)
            operation = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "*"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "/"
            if result is None:
                print("\nError: Cannot divide by zero!")
                return
        else:
            print("\nInvalid operation choice!")
            return
        
        # Display result
        print("\n" + "-" * 40)
        print(f"Result: {num1} {operation} {num2} = {result}")
        print("-" * 40)
        
    except ValueError:
        print("\nError: Please enter valid numbers!")

if __name__ == "__main__":
    main()
