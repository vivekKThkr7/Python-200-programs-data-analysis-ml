username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    account_status = input("Enter account satus: ")
    if account_status == "active":
        print("Login Successful")
    else:
        print("Account is inactive")

else:
    print("Invalid username or password")
    