#alinea 1) Dada uma linha de texto, define um programa que determina se a palavra "hello" aparece no início da linha.

import re

line1 = "hello world"
line2 = "goodbye world"
line3 = "hi, hello there"

for line in [line1, line2, line3]:
    print (re.match(r"hello", line)!= None) #imprime true ou false
    
#alinea 2) Dada uma linha de texto, define um programa que determina se a palavra "hello" aparece em qualquer posição da linha.


line1 = "hello world"
line2 = "goodbye world"
line3 = "hi, hello there"

for line in [line1, line2, line3]:
    print (re.search(r"hello", line)!= None) #imprime true ou false

#alinea 3) Dada uma linha de texto, define um programa que pesquisa por todas as ocorrências da palavra "hello" dentro da linha, admitindo que a palavra seja escrita com maiúsculas ou minúsculas.

line = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
print (re.findall(r"hello",line))

#só imprime 2 ocorrencias porque tamos a procurar só hello em minusculas

#opções para imprimir de qualquer das formas:
line = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
print (re.findall(r"[hH][eE][lL][lL][oO]",line))

#ou
line = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
print (re.findall(r"(i?hello)",line))

#alinea 4) Dada uma linha de texto, define um programa que pesquisa por todas as ocorrências da palavra "hello" dentro da linha, substituindo cada uma por "*YEP*".
line = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
print(re.sub(r"(i?hello)", "*YEP*",line))


#alinea 5) Dada uma linha de texto, define um programa que pesquisa por todas as ocorrências do caracter vírgula, separando cada parte da linha por esse caracter.
line = "bananas, laranjas, maçãs, uvas, melancias, cerejas, kiwis, etc."
print (re.split(r",",line))
