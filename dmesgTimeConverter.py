#!/usr/bin/env python3
from datetime import datetime
import subprocess
import sys

# Get seconds from system uptime file;
cmd = subprocess.check_output(['cat', '/proc/uptime'])
data = cmd.decode("utf-8").split(".", 1)

# Get date with date function;
print("[_Kernel started %s seconds ago.]" % (data[0]))

print(datetime.fromtimestamp(int(data[0])).strftime("%A, %B %d, %Y %I:%M:%S"))
print(len(sys.argv))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Script starting!")
    else:
        if len(sys.argv) != 2:
            print("Error. Invalid parameters.")
            sys.exit(1)
        else:
            path_to_file = sys.argv[1]
            print(path_to_file)

