import datetime            

print("------------------FOOD ORDERING---------------------")
print(" Press              Food                  Price   ")
print("----------------------------------------------------")
print(" [F1]            Pork Adobo               ₱ 80.00")              
print(" [F2]              Pancit                 ₱ 70.00")           # menu of the ordering system
print(" [F3]           Pork Sinigang             ₱ 95.00")
print(" [F4]             Shanghai                ₱ 60.00")
print(" [F5]              Bulalo                 ₱ 450  ")
print(" [F6]              Rice                   ₱ 15.00")
print("----------------------------------------------------")
print("                    Drinks                          ")
print("----------------------------------------------------")
print(" [D1]              Iced tea                ₱ 55.00  ")
print(" [D2]             Mountain dew             ₱ 35.00  ")
print(" [D3]               Coke                   ₱ 35.00  ")
print(" [D4]               Water                  ₱ 00.00  ")
print("----------------------------------------------------")
menu = {
    'F1': 80.00,
    'F2': 70.00,
    'F3': 95.00,               # dictionary for the choices
    'F4': 60.00,
    'F5': 450,
    'F6': 15.00,
    'D1': 55.00,
    'D2': 35.00,
    'D3': 35.00,
    'D4': 00.00,
}

order = {}

current_datetime = datetime.datetime.now()              # sourcecode for the date and time

name = input("Enter Customer name: ")
while True:                    
    choice = input("Input your order or(Press E/e to end):  ")
    if choice == "E" or choice == "e":
        break
    if choice not in menu:
        print("Food not available")
        continue
    quantity = int(input("How many order do you want?: "))
    order[choice] = order.get(choice, 0) + quantity 

total = 0
for item, quantity in order.items():
    price = menu[item]                 # computation for the total order of the user
    amount = price * quantity
    total = amount + total

print("")
print("----------------------Receipt-----------------------")
print("Date: ",current_datetime.strftime("%m/%d/%y"))
print("Time: ", current_datetime.strftime("%H:%M %p"))
print("Customer name: ", name)
print("Your Order: ", order)                                  
print("Total: \u20B1",total)
print("Thank you for Order!!!")
print("----------------------------------------------------")