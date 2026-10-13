#  Working wih Dates and Times
# Python's built-in datetime module helps us work with dates, times, and timestamps.
# Applications use for attendence, employee records, expense tracking invoices, and expiry dates.

from datetime import date, datetime

today = date.today()
current_time = datetime.now()

print("Today's date:", today)
print("Current time:", current_time.strftime("%H:%M"))
print("Formatted date:", today.strftime("%d-%m-%Y"))