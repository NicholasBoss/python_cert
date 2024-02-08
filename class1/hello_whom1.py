#!/usr/bin/python

# Import the basic sys library.
import sys

# Assign command-line argument list to variable.
cmd_list = sys.argv

# Declare counter variable
counter = 0

# Loop through the command-line argument list and print it.
for element in cmd_list:
  print("[" + str(counter) + "][" + element + "]")
  counter = counter + 1
  
# Print dynamic output when two parameters are received.
print("\n")
print("Hello " + cmd_list[1] + "!\n")
