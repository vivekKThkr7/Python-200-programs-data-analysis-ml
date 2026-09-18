# Ask for a sentence and determine whether it is a palindrome.


sentence = input("Enter a sentence: ").strip().lower()

reverse = sentence[::-1]

if sentence == reverse:
    print("palindrome")
else:
    print("Not a palindrome")
    