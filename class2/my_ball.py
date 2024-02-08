#!/usr/bin/python
 
# Import the Ball class into its own namespace.
import Ball
 
# Assign an instantiated class to a local variable.
myBall = Ball.Ball()
 
# Check whether the local variable holds a valid Ball instance.
if not myBall is None:
  print(myBall, "instance.")
else:
  print("No Ball instance.")
 
# Loop through 10 times changing bounce direction.
for i in range(1,10):
  # Find dirction of ball.
  print(myBall.getDirection())
 
  # Bounce the ball.
  myBall.bounce()
