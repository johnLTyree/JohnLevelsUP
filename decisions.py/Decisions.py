import random

# Generate a random number between 0 and 10 (inclusive).
number = random.randint(0, 10)

# The following line is commented out due to a syntax error.
# print("Hello") # syntax error, Unexpected Indent

# Set threshold values for comparison.
threshold = 6
threshold2 = 4

# Check if the generated number is less than the threshold.
if number < threshold:
    print("Small Number")
# Check if the generated number is greater than the threshold.
elif number > threshold:
    print("Big Number")
else:  # This block is executed if the number is equal to the threshold.
    print("Number is", threshold)

# Check if the generated number is less than the second threshold.
if number < threshold2:
    print("Really Small Number")

# This line will always be executed, regardless of the conditions above.
print("detented")

# Print the generated number.
print(number)

# The following line is commented out to avoid a runtime error.
# 1/0 # runtime error. Cant compute the valid syntax instruction