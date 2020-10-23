#!/usr/bin/env python3
import datetime
import subprocess
import sys
import re

def hasNumbersPoint(inputString):
    stringLen=len(inputString)
    points=0
    numbers=0
    for character in inputString:
        if character.isdigit():
            numbers+=1
        elif character == ".":
            points+=1
    if points == 1 and numbers == stringLen - 1:
        return True
    else:
        return False

# Check input arguments;
if __name__ == "__main__":
    if len(sys.argv) == 3:
        print("Script starting! System started at %s" % (sys.argv[2]))
        path_to_file = sys.argv[1]
        print("Path to file: %s" % (path_to_file))
    else:
        print("Error: invalid input parameters!")
        print("Usage:\n ./dmesgTimeConverter.py <PATH_TO_FILE> <DATE_FORMAT>")
        print("Example: ./dmesgTimeConverter.py /var/log/dmesg 22-09-2020_07:55:37")
        sys.exit(1)

# Convert string to date; 22-10-2020_08:11:21
_data       =   sys.argv[2]
_day        =   int(_data[0:2])
_month      =   int(_data[3:5])
_year       =   int(_data[6:10])
_hours      =   int(_data[11:13])
_minutes    =   int(_data[14:16])
_seconds    =   int(_data[17:19])

# Set date object;
uptime_datetime = datetime.datetime(_year, _month, _day, _hours, _minutes,_seconds)

# Open file for read;
file = open(sys.argv[1], 'r')
lines = file.readlines()

# Open file for write;
outFile = open(path_to_file + ".edited", 'w')

for line in lines:
    # Get positions of seconds;
    pos_1 = line.find("[")
    pos_2 = line.find(']')
    # Remove spaces from seconds;
    check_for_seconds = line[pos_1 + 1:pos_2].strip()
    if (hasNumbersPoint(check_for_seconds)):
        # Round seconds;
        check_for_seconds = round(float(check_for_seconds) , 6)
        # Add seconds to date;
        process_started_date = uptime_datetime + datetime.timedelta(seconds=check_for_seconds)
        result = str((process_started_date.strftime("%Y/%m/%d %H:%M:%S")))
        result = "[" + result + "] " + line[pos_2+1:]
        outFile.write(result)
        print(result, end="")
    else:
        print(line, end="")
        outFile.write(line)


"""
    # Get seconds;
    process_started_sec = round(float(line[line.find('[')+1 : line.find(']')].strip()), 6)
    # Subtract seconds from datetime;
    process_started_date = uptime_datetime + datetime.timedelta(seconds=process_started_sec)
    result = str((process_started_date.strftime("%Y/%m/%d %H:%M:%S")))
    
    # Edit file time in seconds to date;
    new_line = "[" + result + "] " + line[pos_2+1:]
    #print(new_line, end="")

    # Write to file;
    outFile.write(new_line)
"""
outFile.close()
