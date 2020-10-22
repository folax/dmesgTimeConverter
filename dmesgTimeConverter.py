#!/usr/bin/env python3
from datetime import datetime
import subprocess
import sys

# Get seconds from system uptime file;
cmd_res = subprocess.check_output(['cut', '-d', ' ', '-f', '1', '/proc/uptime'])
kernel_started_sec = cmd_res.decode("utf-8")

# Check input arguments;
if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("Script starting! Kernel started %s seconds ago." % (kernel_started_sec))
        path_to_file = sys.argv[1]
        print("Path to file: %s" % (path_to_file))
    else:
        print("Error. Invalid input parameters.")
        sys.exit(1)

# Open file;
file = open(sys.argv[1], 'r')
Lines = file.readlines()

for line in Lines:
    # Get positions of seconds;
    pos_1 = line.find("[")
    pos_2 = line.find(']')
    # Get seconds;
    process_started_sec = line[line.find('[')+1 : line.find(']')].strip()
    _date = round(float(kernel_started_sec), 2) - round(float(process_started_sec), 2)
    #print(_date)
    cmd = subprocess.check_output(['date', '-d', '%f seconds ago' % (_date)])
    print(cmd.decode("utf-8"), end=' ')

    #date -d "$(</proc/uptime awk '{print $1}') seconds ago"

    # Get line without seconds;
    #line_without_sec = line[pos_2+1:]
    #print(line_without_sec)

