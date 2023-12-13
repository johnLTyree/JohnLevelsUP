# List of connections between cities and their corresponding flight times
connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170)
]

# Initialize counters for the number of connections and total flight time
counter = 0
sum = 0.0

# Iterate through each connection in the list
for con in connections:
    # Check if the destination city is 'Rome'
    if con[1] == 'Rome':
        # Increment the counter by 1 and add the flight time to the total sum
        counter += 1
        sum += con[2]

# Print the results: number of connections to Rome and the average flight time
print(counter, 'connections lead to Rome with an average flight time of', sum/counter, 'minutes')
