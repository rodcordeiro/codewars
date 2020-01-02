# -*- coding: utf-8 -*-
# Author: Rodrigo Cordeiro
  # returns *True* if every element in an array is an integer or a float with no decimals.
  # returns *True* if array is empty.
  # returns *False* for every other input.

teste1 = [1,2,3,4,5]
teste2 = [1,2,3,"oi"]
teste3 = [1,2,3,4,3.5]
teste4 = []
teste5 = [13,8,3.0]
def is_int_array(arr):
    for item in arr:
    	x= type(item)
    	if x == int:
    		pass
    	else:
    		print(arr)
    		print(arr.index(item),item)
    		return False
    return True

def isfloat(arr):
	for item in arr:
		if type(item) == float and item > 0:
			print(item,"OK")
		else:
			print(item)


print(isfloat(teste3))
print(isfloat(teste5))


# print(is_int_array(teste1))

# print(is_int_array(teste2))

# print(is_int_array(teste3))

# print(is_int_array(teste4))

# print(is_int_array(teste5))
