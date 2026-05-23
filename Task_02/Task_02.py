import json

# Sample log data
logs = [
    "INFO User logged in",
    "ERROR Database timeout",
    "WARNING Memory usage high",
    "ERROR Invalid credentials"
]

# Write logs into file
with open("logs.txt", "w") as f:
    for log in logs:
        f.write(log + "\n")

# Count log types
count = {}

with open("logs.txt", "r") as f:
    for line in f:
        log_type = line.split()[0]

        if log_type in count:
            count[log_type] += 1
        else:
            count[log_type] = 1

# Save result in JSON file
with open("result.json", "w") as f:
    json.dump(count, f, indent=4)

# Print most frequent log type
most = max(count, key=count.get)

print("Log Counts:", count)
print("Most Frequent Log Type:", most)
