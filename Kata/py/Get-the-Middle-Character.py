# -*- coding: utf-8 -*-
# Author: Rodrigo Cordeiro

# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

## Examples:
# Kata.getMiddle("test") should return "es"
# Kata.getMiddle("testing") should return "t"
# Kata.getMiddle("middle") should return "dd"
# Kata.getMiddle("A") should return "A"

def get_middle(s):
	a = len(s) #checar tamanho
	b = int(a/2)
	if a > 2:
		if a % 2 ==0:
			return s[b-1:-b+1]
		else:
			return s[b:-b]
	else:
		return s


print(get_middle("test"),"es")
print(get_middle("testing"),"t")
print(get_middle("middle"),"dd")
print(get_middle("A"),"A")
print(get_middle("of"),"of")