# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "talba"
__date__ = "$10/04/2015 19:05:17$"

class Operation:
  """
  This is a static class with no objects
  """
  def make_increment(n):
    """
    Create an increment
    """
    return lambda x: x + n

  def make_decrement(n):
    """
    Create a decrement
    """
    return lambda x: x - n

  def make_multiplier(n):
    """
    Create a multiplier
    """
    return lambda x: x * n

  def make_divisor(n):
    """
    Create a divisor
    """
    return lambda x: x / n

  def make_modulus(n):
    """
    Create a modulus operation
    """
    return lambda x: x % n
  
  def make_power(n):
    """
    Create a power operation
    """
    return lambda x: x ** n

  def show(operator, function):
    """
    Show a complete table of an operation
    """
    for num in range(1,10):
      inc = function(num)
      for x in range(1,10):
        print("%d %s %d = %d" % (x, operator, num, inc(x)))