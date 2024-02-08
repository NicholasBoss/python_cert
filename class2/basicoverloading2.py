#!/usr/bin/python
 
# Call the hello() function without any arguments.
def hello():
  print("Hello World!")
 
# Call the hello() function with one argument.
def hello(whom):
  print("Hello", whom)
 
# Call the overloaded hello() functions.
hello()
hello("Henry")
