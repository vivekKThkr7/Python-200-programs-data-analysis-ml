# Create a lsit of 5 names and report.
# Ask the user for a name and report - Found / Not Found

names = ["Vivek", "Bikash", "Roshan", "Prem", "Bhola"]

search_name = input("Enter a name to search: ")

if search_name in names:
    print(search_name, "- Found")

else:
    print(search_name, '- Not found')
    
