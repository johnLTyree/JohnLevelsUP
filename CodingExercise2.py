#Variables and Operators
#In a fictional country named Lowtaxland, the income tax is 5%. In another fictional country, Ripoffland, the income tax is 43%. You are given a sample variable named income with the value of 250,000.

#1. Create two additional variables: lowtaxland_rate with the value of 0.05 (which is the same as 5%) and ripoffland_rate with the value of 0.43 (which is the same as 43%).

#2. Print to the output the following (all output on a single line):

#Your income is {income} and you would pay {tax amount in Lowtaxland} income tax in Lowtaxland or {tax amount in Ripoffland} income tax in Ripoffland. You would save {difference between the tax amounts} by paying taxes in Lowtaxland!

#Your solution must replace the curly brackets (e.g. {income}) with the actual values (e.g. 250000). The values must be calculated correctly. The tax amount should be calculated as {income * lowtaxland_rate} for Lowtaxland, and {income * ripoffland_rate} for Ripoffland, respectively.


# Income and tax rates for Lowtaxland and Ripoffland
income = 250_000
lowtaxland_rate = 0.05
ripoffland_rate = 0.43

# Calculate income tax in Lowtaxland and Ripoffland
tax_lowtaxland = income * lowtaxland_rate
tax_ripoffland = income * ripoffland_rate

# Calculate the tax savings by paying taxes in Lowtaxland instead of Ripoffland
tax_savings = tax_ripoffland - tax_lowtaxland

# Print the results
print('Your income is', income, 'and you would pay', tax_lowtaxland, 'income tax in Lowtaxland or', tax_ripoffland, 'income tax in Ripoffland.')
print('You would save', tax_savings, 'by paying taxes in Lowtaxland!')

