# -*- coding: utf-8 -*-
# Author: Rodrigo Cordeiro

# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others.
# Bob observed that one number usually differs from the others in evenness.
# Help Bob — to check his answers, he needs a program that among the given numbers finds one
# that is different in evenness, and return a position of this number.
# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
# ##Examples :
# iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even
# iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd

#Minha resposta
def iq_test(numbers):
	num = numbers.split(' ')
	par = []
	impar = []
	for i in num:
		if int(i) % 2 ==0:
			par.append(i)
		else:
			impar.append(i)
	if len(par) > len(impar):
		return num.index(impar[0]) + 1
	else:
		return num.index(par[0]) + 1

# Melhor resposta
def iq_test2(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]
    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1

print(iq_test("2 4 7 8 10"),3)
print(iq_test("1 2 2"), 1)
print(iq_test("43 28 1 91"), 2)
print(iq_test("20 94 56 50 10 98 52 32 14 22 24 60 4 8 98 46 34 68 82 82 98 90 50 20 78 49 52 94 64 36"),26)
print(iq_test("79 27 77 57 37 45 27 49 65 33 57 21 71 19 75 85 65 61 23 97 85 9 23 1 9 3 99 77 77 21 79 69 15 37 15 7 93 81 13 89 91 31 45 93 15 97 55 80 85 83"),48)
print(iq_test("100 100 1"),3)
print(iq_test("9 31 27 93 17 77 75 9 9 53 89 39 51 99 5 1 11 39 27 49 91 17 27 79 81 71 37 75 35 13 93 4 99 55 85 11 23 57 5 43 5 61 15 35 23 91 3 81 99 85 43 37 39 27 5 67 7 33 75 59 13 71 51 27 15 93 51 63 91 53 43 99 25 47 17 71 81 15 53 31 59 83 41 23 73 25 91 9"),32)
