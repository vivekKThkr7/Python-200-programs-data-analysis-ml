# Calcualte days Unitl Expiry
# Ask the user to enter date in this format: (Enter expiry date (DD-MM-YYYY): 31-12-2026)
# Program must calcualte how many days remain between today and the expiry date

# requirements:
# 1. if the date is in the future, display the number of remaining days.
# 2. If the date is in the past, print " This date has already passed. "
# 3. if the user enters an invalid data or the wrong format, display an appropriate error meeeage without crashing.
# 4. if the expiry date is today, report that it expires today.


from datetime import datetime, date

text = input("Enter expiry date (DD-MM-YYYY): ").strip()

try:
    expiry = datetime.strptime(text, "%d-%m-%Y").date()
except ValueError:
    print("Invalid date or wrong format. Please use DD-MM-YYYY, e.g. 31-12-2026.")
else:
    days_left = (expiry - date.today()).days
    if days_left > 0:
        print("Days until expiry:", days_left)
    elif days_left == 0:
        print("This product expires today.")
    else:
        print("This date has already passed.")