# We want to find:

# total characters
# total words
# uppercase version
# lowercase version
# whether "python" appears
# reversed sentence

text = input("Enter a sentence: ").strip()

print("Characters: ", len(text))

words = text.split()
print("Words: ", len(words))

print("Uppercase: ", text.upper())
print("lowercase: ", text.lower())


if "python" in text.lower():
    print("The sentence contains python")
else:
    print("The sentence does not contains Python")

print("Reversed: ", text[::-1])