#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import re

def extract_request_info(log_line):
    '''Extracts sections of a line of an HTTP request log.
    '''
    # Regular expressions to match different parts of the log line
    patterns = (
        r'\s*(?P<ip>\S+)\s*',  # IP address
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',  # Date and time
        r'\s*"(?P<request>[^"]*)"\s*',  # Request details
        r'\s*(?P<status_code>\S+)',  # Status code
        r'\s*(?P<file_size>\d+)'  # File size
    )
    
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    
    # Construct a log format using the patterns
    log_format = '{}\\-{}{}{}{}\\s*'.format(patterns[0], patterns[1], patterns[2], patterns[3], patterns[4])
    
    # Attempt to match the log line with the log format
    match = re.fullmatch(log_format, log_line)
    
    # If a match is found, extract status code and file size
    if match is not None:
        status_code = match.group('status_code')
        file_size = int(match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info

def print_http_stats(total_file_size, status_code_stats):
    '''Prints the accumulated statistics of the HTTP request log.
    '''
    print('Total File Size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_code_stats.keys()):
        num = status_code_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)

def update_metrics(log_line, total_file_size, status_code_stats):
    '''Updates the metrics from a given HTTP request log.

    Args:
        log_line (str): The line of input from which to retrieve the metrics.

    Returns:
        int: The new total file size.
    '''
    line_info = extract_request_info(log_line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_code_stats.keys():
        status_code_stats[status_code] += 1
    return total_file_size + line_info['file_size']

def run_log_parser():
    '''Starts the log parser.
    '''
    line_num = 0
    total_file_size = 0
    status_code_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    
    try:
        while True:
            log_line = input()
            total_file_size = update_metrics(
                log_line,
                total_file_size,
                status_code_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_http_stats(total_file_size, status_code_stats)
    except (KeyboardInterrupt, EOFError):
        print_http_stats(total_file_size, status_code_stats)

if __name__ == '__main__':
    run_log_parser()
