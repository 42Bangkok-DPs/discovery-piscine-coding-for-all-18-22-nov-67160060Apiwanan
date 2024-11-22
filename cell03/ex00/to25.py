number = input("Enter a number: ")

try:
    number = int(number)
    
    if number > 25:
        print("Error")
    else:
        for i in range(number, 26):
            print(i)

except ValueError:
    print("Invalid input. Please enter a valid number.")