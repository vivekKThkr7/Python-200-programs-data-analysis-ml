secret_number = 7
while True:
    guess = int(input("Guess the number; "))

    if guess == secret_number:
        print("correct!")
        break
    elif guess < secret_number:
        print("Too Low")

    else:
        print("Too High")
