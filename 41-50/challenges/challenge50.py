secret_number = 25
while True:
    n = int(input("Enter a guess: "))

    if n == secret_number:
        print("Correct guess.")
        break
    elif n< secret_number:
        print("Too low")
    else:
        print("Too High")
        