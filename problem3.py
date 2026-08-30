import math

def circle_area(radius):
  ### type your solution here
  """ float -> float
  function circle_area takes in radius and returns the area of circle
  """
  return math.pi * radius ** 2

def square_area(side):
  ### type your solution here
  """ float -> float
  function square_area takes in side and returns the area of a square
  """
  return side * side

def inscribed_area(sqr_area, cir_area):
  ### type your solution here
  """ float -> None
  function inscribed_area takes in sqr_area and cir_area
  and returns the area between a square and an inscribe circle
  """
  print(sqr_area - cir_area)