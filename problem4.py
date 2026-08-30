def sum_coins(num_pennies, num_nickels, num_dimes, num_quarters):
  """ int, int, int, int -> None
  function that consumes the number of pennies, nickels, dimes, and quarters
  and returns the amount of money (in dollars).
  """
  return (num_pennies + (num_nickels * 5) + (num_dimes * 10) + (num_quarters * 25)) / 100

def return_amount(amount_paid, amount_owed):
  """ float, float -> float
  amount_paid and amount_owed are dollar amounts
  Takes in the amount of money paid, subtracts the amount owed, in order to calculate the amount due back to the customer
  """
  return amount_paid - amount_owed
