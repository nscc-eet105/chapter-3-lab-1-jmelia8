#Joe Melia
#EET-107
#6/17/2025

print("Numeric Workday Translator\n")

value = int(input("Enter the numeric value of the workday you wish to translate: "))
workday = ()
if value == 0:
    workday = "a weekend"
elif value == 1:
    workday = "Monday"
elif value == 2:
    workday = "Tuesday"
elif value == 3:
    workday = "Wednesday"
elif value == 4:
    workday = "Thursday"
elif value == 5:
    workday = "Friday"
elif value == 6:
    workday = "Saturday"
elif value == 7:
    workday = "Sunday"
else:
    workday = "is invalid"

print("The workday is", workday)
