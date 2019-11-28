#!/usr/bin/python3

def recherche():
	chaine = input("Entrez le compte a rechercher : ") 
	with open("liste_mdp","r") as fichier:
		for ligne in fichier:
			if chaine in ligne: 
				print(ligne)
