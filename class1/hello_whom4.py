#!/usr/bin/python

# Import the basic sys library.
import sys

# Parse and convert to string.
def parse_input(input_list):
  
  # Assign command-line argument list to variable.
  cmd_list = input_list[1:]
  
  # Declare return variable.
  result = ""

  # Check whether or not there are parameters beyond the file name.
  if isinstance(input_list, list) and len(input_list) != 0:
    
    # Loop through the command-line argument list and print it.
    for element in cmd_list:
      if len(result) == 0:
        result = element
      else:
        result = result + " " + element
    
  # Return result variable as string.
  return result

# Assign command-line argument list to variable.
whom = parse_input(sys.argv)

# Check if string isn't empty and use dynamic input.
if len(whom) > 0:

  # Print dynamic hello salutation.
  print("Hello " + whom + "!\n")
  
else:
  
  # Print default salutation.
  print("Hello World!")
