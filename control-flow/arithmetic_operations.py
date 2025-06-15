def main():
    print("Arithmetic operations")
    num1 = float(input("Entre First Number: "))
    num2 = float(input("Entre Second Number: "))
    operation = input("Enter Operation:(add,subtract,multiply,divide)  ").strip().lower()
    Result = perform_operation(num1, num2, operation)
    print(Result)
