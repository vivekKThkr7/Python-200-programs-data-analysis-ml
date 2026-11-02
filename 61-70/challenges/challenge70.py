# Analyze a sentence: count characters, words, vowels, consonants, spaces,
# digits, uppercase letters, lowercase letters, check for "python", and reverse it.

text = input("Enter a sentence: ")

vowels = 0
consonants = 0
spaces = 0
digits = 0
uppercase = 0
lowercase = 0

for char in text:
    if char.isalpha():
        if char.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

    if char == " ":
        spaces += 1
    if char.isdigit():
        digits += 1
    if char.isupper():
        uppercase += 1
    if char.islower():
        lowercase += 1

print("Characters:", len(text))
print("Words:", len(text.split()))
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", spaces)
print("Digits:", digits)
print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)
print("Python appears" if "python" in text.lower() else "Python does not appear")
print("Reversed:", text[::-1])
