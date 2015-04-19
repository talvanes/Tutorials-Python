# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from Operation import Operation

__author__ = "talba"
__date__ = "$10/04/2015 18:44:16$"  

operator_set = {
'+': Operation.make_increment,
'-': Operation.make_decrement, 
'*': Operation.make_multiplier, 
'/': Operation.make_divisor,
'%': Operation.make_modulus,
'**': Operation.make_power
}

if __name__ == "__main__":
  Operation.show('+', operator_set['+'])
  print("\n")
  Operation.show('-', operator_set['-'])
  print("\n")
  Operation.show('*', operator_set['*'])
  print("\n")
  Operation.show('/', operator_set['/'])
  print("\n")
  Operation.show('%', operator_set['%'])
  print("\n")
  Operation.show('**', operator_set['**'])