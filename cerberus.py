#!/usr/bin/python

from random import *
from string import *
from csv import *

print("Entrez le nom/url :")
url = input()
print("\nEntrez votre identifiant :")
identifiant = input()
print("\nChoisir la taille du mdp :")

caracteres = []
taille = input()
conv = int(taille)
mdp = ""
compteur = 0

for i in range(33,127):
	caracteres.append(chr(i))

while compteur < conv:
	lettre = choice(caracteres)
	mdp += lettre
	compteur += 1

print("\nVotre mdp est :",mdp,"\n")

with open ("liste_mdp", "w") as liste_mdp:
	liste_mdp.write(url + "\n" + identifiant + "\n" + mdp)
