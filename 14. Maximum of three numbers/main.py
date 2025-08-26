# Define a function which takes three integer number as parameters and returns maximum of them.

# Input
    # max_of_three(4,5,3)
# Output
    # 5





def check_max(a,b,c):

    if (a>=b) and (a>=c):
        print(num1)
    elif (b>=c):
        print(num2)
    else:
        print(num3)

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))


result = check_max(num1,num2,num3)
