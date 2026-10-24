# Import namedtuple to create a custom data type for log entries
# Import Counter to count how many times each item appears
from collections import namedtuple, Counter

# Import json to save the report in JSON format
import json

# Import os to work with file paths
import os


# Create a custom data type called LogEntry using namedtuple
# Each log entry contains four fields:
# timestamp, ip_address, endpoint, and status_code
LogEntry = namedtuple(
    "LogEntry",
    ["timestamp", "ip_address", "endpoint", "status_code"]
)


# Define a function that receives two file paths
# log_file_path: String, the path of the input log file
# json_file_path: String, the path of the output JSON file
def analyze_logs(log_file_path: str, json_file_path: str):

    # logs: List
    # An empty list used to store all log entries
    logs = []

    # file: TextIOWrapper
    # A file object opened in read mode
    with open(log_file_path, "r", encoding="utf-8") as file:

        # line: String
        # Read the input file one line at a time
        for line in file:

            # line: String
            # Remove whitespace and newline characters from both ends
            line = line.strip()

            # If the line is empty, skip it
            if not line:
                continue

            # timestamp_part: String
            # Contains the timestamp with the opening bracket
            # rest: String
            # Contains the remaining information in the log line
            timestamp_part, rest = line.split("] ")

            # timestamp: String
            # Remove the opening bracket from the timestamp
            timestamp = timestamp_part.lstrip("[")

            # ip_address: String, stores the visitor's IP address
            # endpoint: String, stores the requested endpoint
            # status_code: String, stores the response status code
            ip_address, endpoint, status_code = rest.split(" ")

            # entry: LogEntry
            # Create a LogEntry object containing the four log fields
            entry = LogEntry(
                timestamp=timestamp,
                ip_address=ip_address,
                endpoint=endpoint,
                status_code=status_code
            )

            # logs: List
            # Append the new LogEntry object to the list
            logs.append(entry)

    unique_ip = list({log.ip_address for log in logs})

    # endpoint_counter: Counter
    # Count how many times each endpoint appears in the logs
    endpoint_counter = Counter(log.endpoint for log in logs)

    # endpoint_counts: Dictionary
    # Convert the Counter object into a regular dictionary
    # Each key is an endpoint and each value is its count
    endpoint_counts = dict(endpoint_counter)

    # failed_request: List of Dictionaries
    # Store requests whose status code is not "200"
    failed_request = [

        # Each item in the list is a Dictionary
        # It contains the IP address, endpoint, and status code
        {
            "ip": log.ip_address,          # String: Visitor's IP address
            "endpoint": log.endpoint,      # String: Requested endpoint
            "status": log.status_code      # String: Response status code
        }

        # log: Represents one LogEntry object from the logs list
        for log in logs

        # Include only logs whose status code is not "200"
        if log.status_code != "200"
    ]

    # security_report: Dictionary
    # Store all analysis results in one dictionary
    security_report = {

        # total_requests: Integer
        # len() returns the total number of log entries
        "total_requests": len(logs),

        # unique_ips: List
        # A list of unique visitor IP addresses
        "unique_ips": unique_ip,

        # endpoint_counts: Dictionary
        # The number of requests for each endpoint
        "endpoint_counts": endpoint_counts,

        # failed_requests: List of Dictionaries
        # A list of requests whose status code is not "200"
        "failed_requests": failed_request
    }

    # file: TextIOWrapper
    # Open the output JSON file in write mode
    with open(json_file_path, "w", encoding="utf-8") as file:

        # json.dump: Function
        # Convert the security_report dictionary into JSON
        # Save the JSON data inside the output file
        # indent=4 makes the JSON file easier to read
        json.dump(security_report, file, indent=4)

    # Return the final report
    # The returned value is a Dictionary
    return security_report


# __name__: String
# __main__: String
# Run the following code only when this file is executed directly
if __name__ == "__main__":

    # Print a String to indicate that the program has started
    print("Script Start")

    # input_file: String
    # Store the absolute path of the input log file
    input_file = os.path.abspath("server_logs.txt")

    # output_file: String
    # Store the absolute path of the output JSON file
    output_file = os.path.abspath("security_report.json")

    # Print a String indicating that the file paths are ready
    print("Path found")

    # report: Dictionary
    # Call the function and store its returned report in report
    report = analyze_logs(input_file, output_file)

    # Print a String indicating that the function has finished
    print("Function End")

    # Print the final Dictionary report to the terminal
    print(report)