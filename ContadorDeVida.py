age = input("What is your current age?")

age_left = 90 - int(age)
days_left = age_left * 365
weeks_left = age_left * 52
months_left = age_left * 12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
