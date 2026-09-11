username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin" and password == "1234":
    account_status = input("Status of account (Active/Inactive): ")
    if account_status == "active":
        print("Login Successfully")
    else:
        print("Account is inactive or closed")
else:
    print("invalid inputs")