#!/usr/bin/python3
# coding: utf-8

# Exercício 2:
# * Criar um programa que lê quatro valores inteiros e indica quantos são diferentes, quantos são pares e ímpares.

# Requisitos Exercício 2:
# * O programa deverá solicitar o primeiro valor e guarda-lo numa variável
# * O programa deverá solicitar o segundo valor e guarda-lo numa variável
# * O programa deverá solicitar o terceiro valor e guarda-lo numa variável
# * O programa deverá solicitar o quarto valor e guarda-lo numa variável
# * De seguida deverá validar quais são diferentes, pares e ímpares e imprimir o resultado na consola

# Exemplo Exercício 2:
# - Insira o 1º Valor: 32
# - Insira o 2º Valor: -3
# - Insira o 3º Valor: 32
# - Insira o 4º Valor: 234
# Diferentes = 3, Pares = 3, Ímpares = 1

num = [[], []]
value = 0

for a in range(1, 5):
    value = int(input(f' - Insira o {a}º Valor: '))
    if value % 2 == 0:
        num[0].append(value)
    else:
        num[1].append(value)

Pares = len(num[0])

Impares = len(num[1])

z = num[0] + num[1]

Diferentes = {i: z.count(i) for i in z}

print(str(Diferentes) + ' Pares = ' + str(Pares) + ' Ímpares = ' + str(Impares))
