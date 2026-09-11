# # Ask for the age print
# 0–12   → Child
# 13–19  → Teenager
# 20–59  → Adult
# 60+    → Senior

age = int(input("Enter age: "))

if age <=12:
    print("Child")

elif age >=13 and age <=19:
    print("Teenager")

elif age >= 20 and age < 60:
    print("Adult")

else:
    print("Senior")
