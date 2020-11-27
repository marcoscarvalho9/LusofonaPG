#!/usr/bin/python3
# coding: utf-8

# Exercício 1:
# * Criar um programa para converter um valor em segundos em horas, minutos e segundos

# Requisitos Exercício 1:
# * O programa deve pedir os segundos ao utilizador e guardar em uma variável
# * De seguida o programa deverá calcular o total de horas, minutos e segundos e imprimir o resultado na consola

# Exemplo Exercício 1:
# - 39050 segundos é igual a 10:50:50

import time
hour = 3600  # 1 hour = 3600 seconds
minute = 60  # 1 minute = 60 seconds

seconds = (input('Introduzir os segundos: '))
print(seconds)

conversion = int(seconds) / int(hour)
print(conversion)

conversion_1 = time.strftime("%S:%M:%H", time.gmtime(conversion))

print(conversion_1)

print('- ' + seconds + ' segundos é igual a ' + conversion_1)
