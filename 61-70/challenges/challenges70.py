# buid a program that asks for a sentence and dispays:
# total characters
# total words
# total vowels
# total consonents
# number of spaces
# number of digits
# number of Uppercse letters
# numbr of lowercase letters
# whether "python" appears
# reversed sentence
text = input("Enter a sentence: ").strip()

vowels = 0
consonants = 0
spaces = 0
digits = 0
uppercase = 0
lowercase = 0

for char in text:
    # check vowel
    # check consonant
    # check space
    # check digit
    # check uppercase
    # check lowercase

    print("Characters:", len(text))
    print("Words:", len(text.split()))
    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Spaces:", spaces)
    print("Digits:", digits)
    print("Uppercase letters:", uppercase)
    print("Lowercase letters:", lowercase)

if "python" in text.lower():
    print("Python appears")
else:
    print("Python does not appear")

print("Reversed:", text[::-1])