import random

# Generate a random number between 0 and 10 (inclusive).
number = random.randint(0, 10)

# Initialize a counter to track the number of attempts to get the desired number.
counter = 0

# Execute a loop until the generated number is 7 or until the counter reaches 13.
while number != 7:
    number = random.randint(0, 10)
    counter = counter + 1

    # Break the loop if the counter exceeds or equals 13.
    if counter >= 13:
        break

# Print the number of attempts and the final generated number.
print(counter, number)

# Iterate through a loop with values from 0 to 9.
for i in range(10):
    # Check if the square of the current value is less than 50.
    if i**2 < 50:
        print(i, i**2)
    else:
        # Break the loop if the square exceeds or equals 50.
        break

    # This line is only executed if the square is less than 50.
    print(i)