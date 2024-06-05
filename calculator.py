def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def main():
    print("Simple Calculator")
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        operation = input("Enter the operation (1/2/3/4 or +/−/×/÷): ")
        if operation in ['1', '+', '2', '-', '3', '*', '×', '4', '/']:
            break
        else:
            print("Invalid input. Please select a valid operation.")
    
    if operation in ['1', '+']:
        result = add(num1, num2)
        op_symbol = '+'
    elif operation in ['2', '-']:
        result = subtract(num1, num2)
        op_symbol = '-'
    elif operation in ['3', '*', '×']:
        result = multiply(num1, num2)
        op_symbol = '*'
    elif operation in ['4', '/']:
        result = divide(num1, num2)
        op_symbol = '/'

    print(f"\nThe result of {num1} {op_symbol} {num2} = {result}")

if __name__ == "__main__":
    main()
