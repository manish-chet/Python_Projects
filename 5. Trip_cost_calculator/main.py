
# Write a program which calculates trip cost for a user.

# Create a greeting for your program.
# Ask the user for number of days.
# Ask the user for hotel price.
# Ask the user for flight price.
# Ask the user for rental car price.
# Ask for other expenses.
# Combine all expenses together and print with 2 digits after decimal places.

# Input
    # Welcome to the Trip Cost Calculator!
    # How many days will you stay? 3
    # How much does hotel cost per night? $30
    # How much does flight cost? $50
    # If you need rental car please enter the price otherwise enter zero. $10
    # Enter other possible expenses $0

print("Welcome to the Trip Cost Calculator!")
number_days = int(input("How many days will you stay? "))
hotel_price = float(input("How much does hotel cost per night? $"))
flight_cost = float(input("How much does flight cost? $"))
car_rent = float(input("If you need rental car please enter the price otherwise enter zero. $"))
other_expenses = float(input("Enter other possible expenses $"))
total_cost = number_days * hotel_price + flight_cost + car_rent * number_days + other_expenses
print(f"Total Cost: ${total_cost}")