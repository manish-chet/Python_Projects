# Write a program to prompt the user for hours and rate per hour to compute gross pay. You need to take into account that the result has exactly two digits after the decimal place.

# Input
    # Enter Hours: 35
    # Enter Rate: 2.75

# Output
    # Pay: 96.25




hour = input("Enter Hours: ")
rate = input("Enter Rate: ")
hour = float(hour)
rate = float(rate)
pay = round(hour*rate,2)
print(f"Pay: {pay}")