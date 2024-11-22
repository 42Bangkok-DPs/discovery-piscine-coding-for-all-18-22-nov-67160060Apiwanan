num1 = input("Give me the first number: ")
num2 = input("Give me the second number: ")

try:
    num1 = float(num1)
    num2 = float(num2)
    
    print("Thank you!")
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Division by zero is not allowed!")
        
    print(f"{num1} * {num2} = {num1 * num2}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
