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
