"""3 Escreva um programa que calcula e mostra a área de um círculo, uma vez que o usuário
informe o raio. Use math.pi para obter um valor aproximado de pi. (Use import math antes)."""

import math

pi = math.pi

raio = float (input ("Informe o valor do raio: "))

area = pi * raio**2

print ("A área do círculo é " + str(area))

