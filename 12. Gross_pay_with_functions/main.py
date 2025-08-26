# Rewrite Gross Pay with Overtime Project (Project 6) and create a function called compute_pay which takes two parameters (hours and rate). Additionally, we need to create another function which checks if the type of "input" is a float or not. If the values for hour or rate is not float we will return error.

# Input
    # Enter Hours: 45
    # Enter Rate: 5
# Output
    # Pay: 237.5
# Input
    # Enter Hours: five
# Output
    # Error, please enter numeric input

def compute_pay(p_hour,p_rate):
    if p_hour <40:
        pay = round(p_hour*p_rate,2)
    else: 
        overtime = p_hour - 40
        pay = round((40 * p_rate) + (overtime*p_rate*1.5), 2)
    return pay

def check_input(pinput):
    
    try:
        pinput = float(pinput)
        return pinput
    except ValueError:
        print(f"Error, please enter numeric input for Rate")
        quit()

    return hour, rate   

hour = input("Enter Hours: ")
hour =  check_input(hour)
rate = input("Enter Rate: ")
rate = check_input(rate)
ouput = compute_pay(hour,rate)
print(ouput)