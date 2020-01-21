# -*- coding: utf-8 -*-
# Author: Rodrigo Cordeiro

def duplicate_count(text):
    count = ''
    for a in text.lower():
    	if text.lower().count(a) > 1 and a not in count:
    		count = count + a
    return len(count)


print(duplicate_count("abcde"), 0)
print(duplicate_count("abcdea"), 1)
print(duplicate_count("indivisibility"), 1)
print(duplicate_count('Indivisibilities'),2)
print(duplicate_count('abcdeaB'),2)