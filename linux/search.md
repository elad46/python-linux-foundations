# Searching in Linux

Searching for files and text is a common administrative task.

## find
Used to locate files and directories by name, type, or location.

Examples:
find /home -name file.txt
find . -type f

## grep
Used to search for text inside files.

Examples:
grep "error" file.log
grep -r "error" /var/log

Efficient searching helps troubleshoot issues
and locate configuration quickly.
