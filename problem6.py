def BMI(height, weight):
  """ float, float -> float
  Calculate BMI based on the height in inches and weight in pounds
  """
  calculation = 703 * weight / height**2
  return calculation