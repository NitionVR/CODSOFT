#basic arithmetic calculator

def add(number_1,number_2):
    return number_1+number_2

def substract(number_1,number_2):
    return number_1-number_2

def multiply(number_1,number_2):
    return number_1 * number_2

def divide(number_1,number_2):
    return number_1/number_2

def get_numbers_input():
    while True:
        try:
            number_1 = input("Enter the first number: ")
            if number_1 == "quit":
                break
            number_2 = input("Enter the second number: ")
            if number_2 == "quit":
                break
            return int(number_1),int(number_2)
        except ValueError:
            print("Incorrect input. Try again.")
            continue

def get_operation():
    valid_arithmetic_operators = {'-','+','/','x','*'}
    while True:
        operator = input("Enter operations ( + (add) or - (substract) or / (divide) or * (multiply)): ").strip()
        if operator == "quit":
                break
        if operator in valid_arithmetic_operators:
            return operator

def main():
    while True:
        first_number,second_number = get_numbers_input()
        operator = get_operation()

        if operator == "+":
            result = add(first_number,second_number)
            print(result)

        elif operator == "-":
            result = substract(first_number,second_number)
            print(result)

        elif operator == "*" or operator.lower == 'x':
            result = multiply(first_number,second_number)
            print(result)
        
        elif operator == "/":
            result = divide(first_number,second_number)
            print(result)

if __name__ == "__main__":
    print("Basic Arithmetic Calculator.")
    main()





