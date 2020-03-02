"""2 Escreva um programa que recebe o salário base de um funcionário, calcula e mostra o salário a
receber, sabendo-se que esse funcionário tem gratificação de 5% sobre o salário base e paga
imposto de 7% sobre o salário base."""

salario_base = float (input("Informe o seu salario base: "))

gratificacao = salario_base * 0.05
imposto = salario_base * 0.07

total = salario_base + gratificacao - imposto

print("Seu salario total é: " + str(total))