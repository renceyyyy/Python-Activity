num = int(input("Enter a number: "))
p = 0

for i in range(1, num+1):
    if num % i == 0:
        p += 1
if p == 2:
    print("is a prime number: ", num)
else:
    print("is not a prime number: ", num)
