# Get input from user
n = int(input("Enter the number of terms: "))

# Initialize variables
a, b = 0, 1

# Generate and display Fibonacci sequence
print("Fibonacci sequence:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a+b
