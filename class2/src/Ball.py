class Ball:
  # User-defined constructor with required parameters.
  def __init__(self, color = None, radius = None, direction = None):
    # Assign a default color value when the parameter is null.
    if color is None:
      self.color = "Blue"
    else:
      self.color = color.lower()
 
    # Assign a default radius value when the parameter is null.
    if radius is None:
      self.radius = 1
    else:
      self.radius = radius
 
    # Assign a default direction value when the parameter is null.
    if direction is None:
      self.direction = "down"
    else:
      self.direction = direction.lower()
 
    # Set direction switch values.
    self.directions = ("down","up")
 
  # User-defined standard function when printing an object type.
  def __str__(self):
    # Build a default descriptive message of the object.
    msg = "It's a " + self.color + " " + str(self.radius) + '"' + " ball"
 
    # Return the message variable.
    return msg
 
  # Define a bounce function.
  def bounce(self, direction = None):
    # Set direction on bounce.
    if not direction is None:
      self.direction = direction
    else:
      # Switch directions.
      if self.directions[0] == self.direction:
        self.direction = self.directions[1]
      elif self.directions[1] == self.direction:
        self.direction = self.directions[0]
 
  # Define a bounce function.
  def getDirection(self):
    # Return current direction of ball.
    return self.__format(self.direction)
 
  # User-defined pseudo-private function, which is available
  # to instances of the Ball object and any of its subtypes.
  def __format(self, msg):
    return "[" + msg + "]"
 
# This is the object subtype, which takes the parent class as an
# argument.
class FilledBall(Ball):
  def __init__(self, filler = None):
    # Instantiate the parent class and then any incremental 
    # parameter values.
    Ball.__init__(self,"Red",2)
 
    # Add a default value or the constructor filler value.
    if filler is None:
      self.filler = "Air".lower()
    else:
      self.filler = filler
 
  # User-defined standard function when printing an object type, which 
  # uses generalized invocation.
  def __str__(self):
    # Build a default descriptive message of the object.
    msg = Ball.__str__(self) + str(" filled with " + self.filler)
 
    # Return the message variable.
    return msg