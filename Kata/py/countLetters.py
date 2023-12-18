# -*- coding: utf-8 -*-

# The main idea is to count all the occurring characters(UTF-8) in string. If you have string like this aba then the result should be { 'a': 2, 'b': 1 }
# What if the string is empty ? Then the result should be empty object literal { }

def count(string):
    counter={}
    for a in string:
        if a in counter.keys():
            counter[a] += 1
        else:
    	    counter[a] = 1
    return counter


print(count('aba'), {'a': 2, 'b': 1})
print(count(''), {})