# Rewrite Gross Pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.

# Example Input
    # Enter Hours: 20
    # Enter Rate: ten
# Example Output
    # Error, please enter numeric input for Rate
# Hint
    # The quit() function is used to exit a python program. 
#When it encounters the quit() function in the system, it terminates the execution of the program completely.
# It is possible to write programs that handle selected exceptions.
#In Python, a value is the information that is stored within a certain object. 
#To encounter a ValueError in Python means that is a problem with the content of the object you tried to assign the value to.


hour = input("Enter Hours: ")
try:
    hour = float(hour)
except ValueError:
    print(f"Error, please enter numeric input for Rate")
    quit()


rate = input("Enter Rate: ")
try:
    rate = float(rate)
except ValueError:
    print(f"Error, please enter numeric input for Rate")
    quit()




if hour <40:
    pay = round(hour*rate,2)
else: 
    overtime = hour - 40
    pay = round((40 * rate) + (overtime*rate*1.5), 2) 
print(f"Pay: {pay}")
    