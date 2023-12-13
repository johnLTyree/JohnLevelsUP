import random
import string
import sys

# Function to generate a random string
def string_generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Get the number of EC2 instances needed from user input
number = int(input("Enter the number of EC2 instances needed: "))

# Validate the input for a positive number
while number <= 0:
    print("Please enter a number greater than 0.")
    number = int(input("Enter the number of EC2 instances needed: "))

print("Successful\n")
print("--------------------------------")
print("EC2 Instance Names")
print("--------------------------------")

# Get the department from user input
department = input("Enter Your Department: Marketing, Accounting, FinOps: ")

# Validate the department input
while department.lower() not in ["marketing", "accounting", "finops"]:
    print("Error: You cannot continue. Please enter a valid department.")
    department = input("Enter Your Department: Marketing, Accounting, FinOps: ")

# Generate and print EC2 instance names based on the provided department
for _ in range(1, number + 1):
    unique_name = department
    EC2_unique_name = f"{unique_name}-{string_generator()}"
    print("Your EC2 Instance's unique name is:", EC2_unique_name)
