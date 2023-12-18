# -*- coding: utf-8 -*-
# Author: Rodrigo Cordeiro
  # returns *True* if every element in an array is an integer or a float with no decimals.
  # returns *True* if array is empty.
  # returns *False* for every other input.

# Minha Resposta
def is_int_array(arr):
	if type(arr) is list:
		for item in arr:
			if type(item) == int or type(item) == float and item.is_integer():
				pass
			else:
				return False
		return True
	else:
		return False

# Melhor prática
def is_int_array2(a):
    return isinstance(a, list) and all(isinstance(x, (int, float)) and x == int(x) for x in a)

print(is_int_array([]), True, "Input: []")
print(is_int_array([1, 2, 3, 4]), True, "Input: [1, 2, 3, 4]")
print(is_int_array([-11, -12, -13, -14]), True, "Input: [-11, -12, -13, -14]")
print(is_int_array([1.0, 2.0, 3.0]), True, "Input: [1.0, 2.0, 3.0]")
print(is_int_array([1, 2, None]), False, "Input: [1,2, None]")
print(is_int_array(None), False, "Input: None")
print(is_int_array(""), False, "Input: ''")
print(is_int_array([None]), False, "Input: [None]")
print(is_int_array([1.0, 2.0, 3.0001]), False, "Input: [1.0, 2.0, 3.0001]")
print(is_int_array(["-1"]), False, "Input: ['-1']")