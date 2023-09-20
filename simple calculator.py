def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select Operation: \n1. add\n2. subtract\n3. multiply\n4. divide")


while True:
    choice = input("Enter choice (1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except valuError:
            print("Invalid input. Prease enter a number.")
            continue
        if choice == '1':
            print("The summation of", num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print("The subtract of", num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print("The multiply of", num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print("The divide of", num1, "/", num2, "=", divide(num1, num2))

        next_calculation = input("Let's do next calculation(yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input.")


