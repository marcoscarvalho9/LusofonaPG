#!/usr/bin/python3
# coding=utf-8

y = ["Windows", "Macos", "Linux", "Solaris", "Android", "IOS"]

Ficheiro = "excercio2.1.txt"
file = open(Ficheiro, "w")

for item in y:
    if item != "Solaris":
        print(item)
        file.write(item)
file.close()

h = "excercio2.2.txt"

file = open(h, "w")

i = 0
while i < len(y):
    item = y[i]
    if item != "Solaris":
        print(item)
        file.write(item + "\n")
    i += 1
file.close()
