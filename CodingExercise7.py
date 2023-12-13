# List of monthly spendings
spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]

# Initialize counters for low, normal, and high spendings
low = 0
normal = 0
high = 0

# Iterate through each month's spending
for month in spendings:
    # Categorize spendings into low, normal, or high
    if month < 1000.0:
        low += 1
    elif month <= 2500.0:
        normal += 1
    else:
        high += 1

# Print the results: number of months with low, normal, and high spendings
print('Numbers of months with low spendings: ' + str(low) + ', normal spendings: ' + str(normal) + ', high spendings: ' + str(high) + '.')
