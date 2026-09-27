import math

# Task (2/12): Define a class Vec

class vec:
  __init__(self, x, y):
    self.x = x
    self.y = y
  #initialize the vector self at the given coordinates.

  __repr__(self):
    return "(" + self.x + ", " + self.y + ")"
  #return a string which is a suitable representation of the vector. For instance "(1.34,45.7)" if the self has coordinates x=1.34 and y=45.7.

  __rmul__(self, factor):
    self.x *= factor
    self.y *= factor
  #return a new vector scaled by the given factor

  __add__(self, other):
    return vec(self.x + other.x, self.y + other.y)
  #return a new vector which is the addition of self and other.

  __sub__(self, other):
    return vec(self.x - other.x, self.y - other.y)
  #return a new vector which is the subtraction of self and other.

  norm(self):
    return sqrt(self.x**2 + self.y**2)
  #return the Euclidean norm of self.

  get_coords(self):
    return (self.x, self.y)
  #return the coordinates of self as the tuple (x,y).


# Task (3/12): Additionally define a function dot(u, v)
def dot(u, v):
  return u.x * v.x + u.y * v.y

# Task (4/12): Create a class Particle
class particle:
  __init__(self, mass, position, velocity, radius):
    self.m = mass
    self.p = position
    self.v = velocity
    self.r = radius
  
# Task (5/12): In the Particle class, implement a method inertial_move(self, dt).
  inertial_move(self, dt):
    self.p = self.p +  dt * self.v 
# Task (6/12): In the Particle class, implement a method apply_force(self, dt, f)
  apply_force(self, dt, f):
    self.v = (dt / self.m) * f  + self.v
##########################################
### NB. Tasks 7–8 are done in view.py. ###
##########################################


# Task (9/12): In the Particle class, add a method bounding_box(self)






###########################################
### When you're done with all 12 tasks: ###
### forces/other features in this file! ###
###########################################
