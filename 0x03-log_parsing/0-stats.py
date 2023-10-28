#!/usr/bin/python3
"""HTTP Request Log Parser

This script parses and analyzes HTTP request logs,
extracting information about each log entry and
generating statistics on status codes and total file size.

Usage:
1. Provide input by reading log entries from standard input.
2. The script will accumulate statistics and display
them in real-time every 10 log entries.

Example Log Entry:
192.168.1.1 [2023-10-28 14:30:45.123] "GET /page.html" 200 1234

Log Entry Structure:
- IP address
- Date and time
- Request details
- HTTP status code
- File size
"""

import sys

# Define a dictionary to store the count of status codes
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

total_file_size = 0
line_count = 0  # Keep track of the number of lines processed

try:
    for line in sys.stdin:
        # Split the input line by spaces
        line_parts = line.split(" ")

        # Check if the line contains enough elements
        if len(line_parts) > 4:
            status_code = line_parts[-2]
            file_size = int(line_parts[-1])

            # Check if the status code exists in the
            # dictionary and increment its count
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            # Update the total file size
            total_file_size += file_size

            # Update the line count
            line_count += 1

        # Print status code counts and total file size every 10 lines
        if line_count == 10:
            line_count = 0  # Reset the line count

            # Print the total file size
            print("Total File Size: {}".format(total_file_size))

            # Print out status code counts
            for code, count in sorted(status_code_counts.items()):
                if count != 0:
                    print("{}: {}".format(code, count))

except Exception as err:
    pass

finally:
    # Print the final total file size and status code counts
    print("Total File Size: {}".format(total_file_size))
    for code, count in sorted(status_code_counts.items()):
        if count != 0:
            print("{}: {}".format(code, count))
