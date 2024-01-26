#!/usr/bin/python

# Import the basic sys library.
import sys

# Assign command-line argument list to variable.
cmd_list = sys.argv[1:]

# Check whether or not there are parameters beyond the file name.
if isinstance(cmd_list, list) and len(cmd_list) != 0:

  # Print length of command-line argument list
  print("List of arguments is greater than zero.\n")
  
  # Declare counter variable
  counter = 0

  # Loop through the command-line argument list and print it.
  for element in cmd_list:
    print("[" + str(counter) + "][" + element + "]")
    counter = counter + 1
  
  # Print dynamic hello salutation
  print("Hello " + cmd_list[len(cmd_list) - 1] + "!\n")
else:
  
  #Print program name and message for zero arguments
  print("List of arguments for [" + sys.argv[len(sys.argv) - 1] + "] is zero!\n")
  
  # Print default salutation
  print("Hello World!")
