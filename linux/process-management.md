# Linux Process Management

A process is a running instance of a program.
Each process has a unique PID (Process ID).

## Viewing Processes
- `ps` – shows processes in the current terminal
- `ps aux` – shows all running processes on the system

## Running Processes in Background
Using `&` allows running a command in the background.

Example:
sleep 300 &

## Stopping Processes
Processes can be stopped using the `kill` command.

Example:
kill <PID>

## Monitoring Processes
The `top` command displays real-time information
about system processes and resource usage.
