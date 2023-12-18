# -*- coding: utf-8 -*-
# Author: Rodrigo Cordeiro

# Your task is to write a function which returns the sum of following series upto nth term(parameter).
# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
# Rules:
# You need to round the answer to 2 decimal places and return it as String.
# If the given value is 0 then it should return 0.00
# You will only be given Natural Numbers as arguments.
# Examples:
# SeriesSum(1) => 1 = "1.00"
# SeriesSum(2) => 1 + 1/4 = "1.25"
# SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"

def series_sum(n):
	div = 1
	soma = 1
	if n == 1:
		return ("%.2f" % n)
	elif n > 0:
		for a in range(n -1):
			div = div + 3
			result = 1/div
			soma = soma + result
		return ("%.2f" % soma)
	else:
		return ("%.2f" % n)

#Melhor pratica		
def series_sum2(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))


print(series_sum(1), "1.00")
print(series_sum(2), "1.25")
print(series_sum(3), "1.39")
print(series_sum(4), "1.49")
print(series_sum(5), "1.57")
print(series_sum(6), "1.63")
print(series_sum(7), "1.68")
print(series_sum(8), "1.73")
print(series_sum(9), "1.77")
print(series_sum(15), "1.94")
print(series_sum(39), "2.26")
print(series_sum(58), "2.40")
print(series_sum(0), "0.00")