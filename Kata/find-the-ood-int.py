# -*- coding: utf-8 -*-
# Author: Rodrigo Cordeiro
# Goal: Find the integer that shows an odd number times. Each list has just 1 integer that do this.
# Meta: Achar o número inteiro que aparece um número ímpar de vezes. Cada lista tem apenas um inteiro que faz isso.

def find_it(seq):
	return ([ x for x in seq if seq.count(x) % 2 == 1][0])
	


print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1); 
print(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
print(find_it([10]), 10);
print(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10);
print(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1);