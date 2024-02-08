#!/usr/bin/python
 
# Call the hello() function with an optional parameter; and
# manage the inner workings with and without a parameter.
def hello(whom = None):
  if whom is None:
    print("Hello World!")
  else:
    print("Hello", whom + "!")
 
# Call the overloaded hello() functions.
hello()
hello("Henry")
