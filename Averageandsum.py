sum = 0

for i in range(10):
    num = float(input("Enter a number: "))
    ave = sum / 10
    sum = num + sum
    
print("The average: ", ave)
print("The sum: ", sum)

