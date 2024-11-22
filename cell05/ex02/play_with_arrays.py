original_array = [1, 2, 3, 4, 5, 6, 7, 8]

new_array = [num + 2 for num in original_array if num > 5]

print(f"{original_array}")
print(f"{new_array}")
