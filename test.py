import string
import random

print("Entrer la longueur du mdp : ")
longueur = input()

mdp = ""

compteur = 0

for caractere in range(33,127):
    #    print(chr(caractere), end="")
