username = "balon"
password = "1234"

for i in range(3):
    name = input("Please Enter a username: ")
    pas = input("Please Enter a Password: ")
    if name == username and pas == password:
        print("Login successfully!")
        break

    else: 
        print("Login Failed")

else: 
 print("Too many attempts")