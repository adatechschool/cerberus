#!/usr/bin/python3

chaine = input("Choisissez le compte à rechercher : ") 
with open("liste_mdp","r") as fichier:
	for ligne in fichier:
		if chaine in ligne: 
			print(ligne)
