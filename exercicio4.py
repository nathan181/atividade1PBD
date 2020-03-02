"""4 Sabe-se que:
1 pé = 12 polegadas
1 jarda = 3 pés
1 milha = 1.760 jardas
Faça um programa que obtém uma medida em pés, e faz as conversões a seguir, mostrando os
resultados logo ao final."""

pes = float (input("Informe o valor em pés: "))

res_polegada = pes * 12

res_jarda = pes/3

res_milha = res_jarda / 1760

print("Seu resultado: " + "\nEm polegadas " + str(res_polegada) + "\nEm jardas " + str(res_jarda) + "\nEm milhas " + str(res_milha) )
