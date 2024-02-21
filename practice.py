# Prompt the user to enter a list of numbers separated by spaces
numbers = input("Enter a list of numbers separated by spaces: ").split()

# Convert the input strings to integers
numbers = [int(num) for num in numbers]

# Find the highest, middle, and lowest numbers
highest = max(numbers)
lowest = min(numbers)
sorted_numbers = sorted(numbers)
n = len(sorted_numbers)
middle = sorted_numbers[n // 2] if n % 2 == 1 else (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2

# Print the results
print("Highest number:", highest)
print("Middle number:", middle)
print("Lowest number:", lowest)