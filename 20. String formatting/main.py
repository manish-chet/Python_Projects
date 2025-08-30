# Create a program which prints out student names and their score as shown below

# names and scores lists are given

# names = ['John', 'Edy', 'Jane', 'Kane']
# scores = [90, 95, 80, 75]
# Sample Output:
    # Name Score
    # John 90
    # Edy 95
    # Jane 80
    # Kane 75

# Hint
# Use format() function to format output as shown.

names = ['John', 'Edy', 'Jane', 'Kane']
scores = [90, 95, 80, 75]

print('{0:<10} {1:<5}'.format("Name","Score"))
for index in range(0,len(names)):
    name = names[index]
    result = scores[index]
    print('{0:<10} {1:<5}'.format(name,result))
