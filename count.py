num = int(input("Enter a positive integer: "))
number = num
count = 0

while num > 0:
    count += 1
    num //= 10 

print("Number of digits in ",number, "is", count)
