# Search for an item in the list

names = ["Ram", "Hari", "Mohan", "Sita", "Gita"]

search_name = input("Enter a name to search: ")

if search_name in names:
    print(search_name, " is exist in list")

else:
    print(search_name, " Not found")