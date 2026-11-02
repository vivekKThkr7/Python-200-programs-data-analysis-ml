# Ask for the age and whether the person has an ID.
# The result is True only when the person is at least 18 and has an ID.

age = int(input("Enter your age: "))
has_id_text = input("Do you have an ID? (True/False): ").strip().lower()
has_id = has_id_text == "true"

print(age >= 18 and has_id)
