# Take list of integer as input
numbers = list(map(int,input("Enter the integers:").split()));

# Remove duplicates and sort the list
unique_sorted = sorted(set(numbers));

# Calculate the values
maximum = max(numbers);
minimum = min(numbers);
average = sum(numbers)/len(numbers);

frequency = {}

for num in numbers :
    if num in frequency :
        frequency[num] += 1;
    else:
        frequency[num] = 1;

# Create a dicitionary
result = {
    "Maximum Value" : maximum,
    "Minimum Value" : minimum,
    "Average Value" : average,
    "Frequency" : frequency,
}

# Print output
print("\n--- Final Output ---");
print("Unique Sorted List:",unique_sorted);
print("Maximum Value:", result["Maximum Value"]);
print("Minimum Value:", result["Minimum Value"]);
print("Average Value:", result["Average Value"]);
print("Frequency of Elements:")

for key, value in result["Frequency"].items():
    print(f"{key} -> {value}")
