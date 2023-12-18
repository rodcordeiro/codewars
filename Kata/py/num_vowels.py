# -*- coding: utf-8 -*-
# Author: Rodrigo Cordeiro

def getCount(inputStr):
    num_vowels = 0
    vowels = 'aeiou'
    return len([num_vowels + 1 for a in inputStr.lower() if a in vowels])

print(getCount("abracadabra"), 5)