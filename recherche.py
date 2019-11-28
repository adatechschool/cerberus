#!/usr/bin/python3

chaine = input("Entrez le compte a rechercher : ") 
with open("liste_mdp","r") as fichier:
	for ligne in fichier:
		if chaine in ligne: 
			print(ligne)
