# Linux File Permissions

Linux permissions control who can read, write, or execute files.

## Permission Types
- r (read)
- w (write)
- x (execute)

## User Categories
- u (user)
- g (group)
- o (others)

## Example
-rwxr-xr--

User can read, write and execute.
Group can read and execute.
Others can read only.

## chmod Examples
chmod u+x file.sh
chmod g-w file.txt
chmod o+r file.txt


