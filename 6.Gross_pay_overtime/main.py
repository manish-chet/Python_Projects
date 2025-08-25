# Rewrite the Gross Pay Project (Project 3) program to give the employee 1.5 times the hourly rate for hours worked above 40 hours. Here again the program prompts the user for hours and rate per hour to compute gross pay. You need to take into account that the result has exactly two digits after the decimal place.

# Hint: overtime = hour - 40

# Input
    # Enter Hours: 45
    # Enter Rate: 5
# Output
    # Pay: 237.5

hour = input("Enter Hours: ")
rate = input("Enter Rate: ")
hour = float(hour)
rate = float(rate)


if hour <40:
    pay = round(hour*rate,2)
else: 
    overtime = hour - 40
    pay = round((40 * rate) + (overtime*rate*1.5), 2) 
print(f"Pay: {pay}")
    
