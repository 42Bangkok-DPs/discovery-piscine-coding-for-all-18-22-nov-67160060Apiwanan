limit = input("Enter the limit for the multiplication tables: ")

try:
    limit = int(limit)

    for number in range(1, limit + 1):
        print(f"\nMultiplication table for {number}:")
        
        for i in range(1, 11):
            print(f"{number} x {i} = {number * i}")
    
except ValueError:
    print("Invalid input. Please enter a valid number.")