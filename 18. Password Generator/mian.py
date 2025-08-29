# Password Generator
# Instruction
# Create a program will generate a password based on user inputs. Initial variables are already provided.

# letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# nums = "1234567890"
# symbols = "-+=!@#$%^&*"
# Your program should ask for number of letters, symbols and numbers initially

# Then based on these inputed values it will generate password

# Output can be like this:

    # How many letters do you want in your password? 8
    # How many numbers do you want in your password? 2
    # How many symbols do you want in your password? 2
    # Your password is: EDUpEYIG67*@
# Hint
# Use choice() function from random module to select random character from letters, nums or symbols.

import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
symbols = "-+=!@#$%^&*"
letter= int(input("How many letters do you want in your password"))
number = int(input("How many numbers do you want in your password"))
symbol = int(input("How many symbols do you want in your password"))
password = ""

for letter in range(1,letter+1):
    password += random.choice(letters)

for num in range(1,number+1):
    password +=random.choice(nums)

for num in range(1,symbol+1):
    password +=random.choice(symbols)

passowrdlist = list(password)

random.shuffle(passowrdlist)

advancepas = ""
for i in passowrdlist:
    advancepas +=i

print(f"Your password is {advancepas}")