unit = float(input("Enter a units: "))
if unit <= 100:
    print("No charges")
elif unit + 5 <= 200:
    print("5 Per unit")
elif unit + 10 >= 200:
    print("10 per unit")
else:
    print(unit)