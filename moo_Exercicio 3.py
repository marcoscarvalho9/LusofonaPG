#!/usr/bin/python3
# coding: utf-8

# Exercício 3:
# * 2520 é o número mais pequeno que pode ser dividido por todos os números de 1 até 10 sem resto de divisão. Qual é o
# número positivo mais pequeno que é uniformemente divisivel por todos os números de 1 até 20?

# Requisitos Exercício 3:
# * O programa deve correr, efetuar os calculos e imprimir o resultado na consola.

a = range(10, 21)
b = 21
c = False

while not c:
    if b % 2520 == 0:
        if all(b % n == 0 for n in a):
            c = True
        else:
            b = b + 2520
    else:
        b = b + 1
print(b)
