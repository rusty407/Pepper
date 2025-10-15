import sys
import pyfiglet
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("Pepper Scanner")
print(ascii_banner)

# example is: python3 pepper.py example.com it checks if both arguments are reffered
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("invalid amount of argument! make sure you passed 2 arguments instead of 1")

print("-" * 50)
print("Scanning target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("-" * 50)
