# -*- coding: utf-8 -*-


def rot13(string):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    response = ''
    for char in string:
        if char.lower() in alphabet:
            response += alphabet[alphabet.index(char.lower()) +13].upper()  if char.isupper() else alphabet[alphabet.index(char.lower()) +13]
        else:
            response += char
    return response
    
        
print(rot13('Test'))
print(rot13('Avoid success at all costs!'))