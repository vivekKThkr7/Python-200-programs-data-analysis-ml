# Ask for a number and search for it in:
# do it without using ' in' 
# Use a loop and a flag.

numbers = [10, 20, 15, 20, 35, 40, 50, 65]

search_number = int(input("Enter a number to search: "))

found = False

for number in numbers:
    if number ==search_number:
        found = True
        break

if found:
    print(search_number, "- Found")

else:
    print(search_number, "- Not found")
