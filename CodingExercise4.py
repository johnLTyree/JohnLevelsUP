#Salary calculator
#Ask the user for the number of hours they worked last month and their hourly rate (both numbers should be floats). Use the following prompts:

#How many hours did you work last month? << add a space at the end of this prompt
#What is your hourly rate? << add a space at the end of this prompt

#Then, show the following message with the calculated salary:

#Last month, you earned {hours * hourly_rate} dollars

#The salary should be shown as a float number. For example, for input 30 hours and hourly rate 10.5, show:

#Last month, you earned 315.0 dollars

#Watch out for typos: you must show the output in this particular format!

# Get input from the user: hours worked and hourly rate
hours = float(input('How many hours did you work last month? '))
rate = float(input('What is your hourly rate? '))

# Calculate total earnings by multiplying hours worked with the hourly rate
total_earnings = hours * rate

# Print the result
print('Last month, you earned', total_earnings, 'dollars')
