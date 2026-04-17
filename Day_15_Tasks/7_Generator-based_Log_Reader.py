"""7. Generator-based Log Reader
Scenario: A large log file needs to be processed.
Task:
● Create a generator to read file line by line
● Use loop to process logs
● Use condition to filter errors
● Count occurrences using a dictionary"""

def read_logs(filename):
    f = open(filename, "r")
    for line in f:
        yield line.upper()
    f.close()

error_counts = {}

try:
    for line in read_logs("logs.txt"):
        if "ERROR" in line:
            words = line.split()
            err_name = words[-1]
            error_counts[err_name] = error_counts.get(err_name, 0) + 1
    print("Error Summary:", error_counts)

except FileNotFoundError:
    print("File not found! Please create logs.txt first.")
