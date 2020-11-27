#!/usr/bin/python3
# coding: utf-8

# Exercício 4
# * Criar um programa que consiga gerar uma password aleatória, com os seguintes parâmetros:
# - Tamanho da password (entre 8 a 32 caracteres, deve pedir input ao utilizador)
# - Uppercase and Lowercase
# - Caracteres especiais
# - Digitos

# Requisitos Exercício 4:
# * O programa deve guardar a password em um ficheiro de texto
# * Deve ser utilizado os módulos random e string

import random
import string

generate_password = input('Prima qualquer tecla para gerar nova password: ')

new_password = ''.join([random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation) for n in range(32)])

print('Nova password gerada: ' + new_password)
