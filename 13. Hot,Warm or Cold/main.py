# Define a function which takes a temperature as a parameter:

# returns Hot if the temperature is greater than 28
# returns Warm if the temperature is between 18 and 28, including both.
# returns Cold if the temperature is less than 18

# Input
    # 18
# Output
    # Warm



def check_temperature(temp):    
    if temp > 28:
        print("Hot")
    elif temp > 18 or temp <28:
        print("Warm")
    else: 
        print("Cold")

temp = float(input("Enter Temperture: "))

result = check_temperature(temp)