#Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double(a, b):
  # Store the sum as a variable
  sum = a + b
  
  # If a and b are the same, double the value
  if a == b:
    sum = sum * 2
  return sum