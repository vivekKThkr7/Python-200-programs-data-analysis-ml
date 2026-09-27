# Safe Number Input

while True:

    try: 
        number = int(input("Enter a number: "))
        print("You entered: ", number)
        break

    except ValueError:
        print("Invalid input. Please enter a number.")
    