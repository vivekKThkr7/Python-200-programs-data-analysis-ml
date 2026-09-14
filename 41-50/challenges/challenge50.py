secret_number = 25
while True:
    n = int(input("Enter a guess: "))
    attempts += 1

    if n == secret_number:
        print("Correct guess.")
        print("Attempts: ", attempts)
        break
    elif n< secret_number:
        print("Too low")
    else:
        print("Too High")
