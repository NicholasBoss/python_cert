#!/usr/bin/python

# Import the basic sys library.
import sys
from input import parse_input

# Assign command-line argument list to variable.
whom = parse_input(sys.argv)

# Check if string isn't empty and use dynamic input.
if len(whom) > 0:

  # Print dynamic hello salutation.
  print("Hello " + whom + "!\n")
  
else:
  
  # Print default salutation.
  print("Hello World!")
