print("************FOOD ORDERING************")
print("|Press|        |Food|         |Price|")
print("  [1]           Adobo         ₱ 80.00")
print("  [2]           Pancit        ₱ 70.00")
print("  [3]           Sinigang      ₱ 95.00")
print("  [4]           Shanghai      ₱ 60.00")
print("  [5]           Bulalo        ₱ 450  ")
print("______________________________________")
menu = {
    '1': 80.00,
    '2': 70.00,
    '3': 95.00,
    '4': 60.00,
    '5': 450,
}
order = {}


print("")
food = int(input("Choose your order: "))
quantity = int(input("How many order do you want?: "))
while True:
    other = input("Do you want to order another food? (y/n): ")
    if other == 'y':
        food = int(input("Choose your order: "))
        quantity = int(input("How many order do you want?: "))
    elif food == 1:
        total = quantity * 1
        print("Adobo: "+1)
        print("Quantity: "+ quantity)
        print("Total: ")        
        break
