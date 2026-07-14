# Server Status Monitor

A Python script that reads a list of servers, categorizes them 
by status, and writes the results to separate files.

## Technologies
- Python 3
- File I/O
- List comprehension
- F-strings
- DateTime module

## How to run

1. Clone the repository
git clone https://github.com/YvanKamaro/server-status-monitor

2. Run the script
python3 monitor.py

3. Check the output
cat online.txt
cat offline.txt

## What it does
- Reads servers.txt containing server names and statuses
- Separates servers into online and offline categories
- Writes online servers to online.txt
- Writes offline servers to offline.txt
- Prints a summary to the console

## What I learned
This project helped me understand how Python handles file 
reading and writing, and how to organize data using lists. 
I also learned the difference between using return and print 
inside functions, and how list comprehension makes code 
cleaner and more efficient.

## Sample output
3 Server(s) online
1 Server(s) offline
