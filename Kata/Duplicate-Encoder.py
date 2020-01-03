# -*- coding: utf-8 -*-
# Author: Rodrigo Cordeiro
# Decoda cada letra da palavra para ( ou ), de acordo com a quantidade de vezes que a palavra aparece.

texto = ["teste","din",'recede','Success','(( @']

# Minha Resposta
def duplicate_encode(word):
	word = word.lower()
	letras = []
	resultado = ''
	[letras.append(i) for i in word]
	for i in letras:
		if letras.count(i) >1:
			valor = ')'
		else:
			valor = '('
		resultado = resultado + valor
	return resultado

#Melhor Resposta
def duplicate_encode2(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])


[print(i,"= ",duplicate_encode(i)) for i in texto]
