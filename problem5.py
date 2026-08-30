import math
def maturity(time, temp, ratio):
  """ float, float, float -> float
  function that takes time, temp and ratio and calculates and prints the result of the maturity formula
  """
  calculation = 23.7 * time**3 + (temp / 273) + math.log(ratio)
  print(calculation)
