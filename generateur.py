#!/usr/bin/python3

from random import *
from string import *

def generateur():
    url = input("Entrez le nom/url : ")
    identifiant = input("Entrez votre identifiant : ")
    taille = int(input("Choisir la taille du mdp : "))

    caracteres = []
    mdp = ""
    compteur = 0

    for i in range(33,127):
	    caracteres.append(chr(i))

    while compteur < taille:
	    lettre = choice(caracteres)
	    mdp += lettre
	    compteur += 1

    print("\nVotre mdp est :",mdp,"\n")

    with open ("liste_mdp", "a") as liste_mdp:
	    liste_mdp.write(url + " , " + identifiant + " , " + mdp + "\n")
