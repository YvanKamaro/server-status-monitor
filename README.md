# Server Status Monitor

A Python script that reads a list of servers, categorizes them by status (online/offline/manage), and writes the results to separate files with timestamps.

## Features

1. Interactive input – Add servers via command line with validation
2. Duplicate prevention – Automatically skips duplicate entries
3. Status categorization – Strips, Splits servers into online, offline, and manage groups
4. Timestamp tracking – Adds datetime to each entry for audit trail
5. Smart file handling – Only creates files when servers exist in that category
6. Console summary – Shows count of servers in each status

## Technologies

- Python 3.8
- File I/O (read/write/append modes)
- datetime module for timestamps
- F-strings for clean output formatting

## How to run

1. Clone the repository
git clone https://github.com/YvanKamaro/server-status-monitor

2. Run the script
python3 monitor.py

3. Check the output
cat online.txt
cat offline.txt
cat manage.txt

## What it does

- Reads server entries entered by the user via the command line
- Validates each entry to ensure it contains a valid status (online, offline, or manage)
- Prevents duplicate entries from being added
- Separates servers into three categories: online, offline, and manage
- Appends each category to its respective file with a timestamp:
  · online.txt
  · offline.txt
  · manage.txt
- Only creates files when there is at least one server in that category
- Prints a summary to the console showing how many servers are in each category

## What I learned
This project helped me understand how Python handles file 
reading and writing, how to organize data using lists and validating entries. 
I also learned the difference between using return and print 
inside functions, and how list comprehension makes code 
cleaner and more efficient.

## Future improvements

- Interactive menu system (Add/View/Search/Delete/Exit)
- view() function to display all servers in one place
- search() function to find a specific server across all files
- delete() function to remove a server from its category
- Export to CSV for spreadsheet compatibility
## Sample Session

```
======================
SERVER STATUS MONITOR
======================

Enter server details(e.g Mail01 online/offline/manage)
When finished enter q

> web01 online
> db01 offline
> mail01 manage
> q

➤ 3 Servers.

=======SERVER STATUS REPORT========
Online:      1 server(s)
Offline:     1 server(s)
Manage:      1 server(s)
================================
```

## Author

Yvan Kamaro – github.com/YvanKamaro
