# Create an empty set to store the data
data_set = set()

# Define the number of data points you want to collect
num_data_points = int(input("How many data points do you want to enter? "))

# Loop to get data from users
for i in range(num_data_points):
    data = input(f"Enter data point {i + 1}: ")
    data_set.add(data)  # Add the data to the set

# Print the set
print("Data entered by users:")
for data in data_set:
    print(data)