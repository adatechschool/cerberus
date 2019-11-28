#!/usr/bin/python3

from generateur import generateur
from recherche import recherche
fin = True

while fin: 
    menu = input("Entrez 1 pour une recherche ou 2 pour generer ou 3 pour quitter : ")
    if menu == '1':
        recherche()
    elif menu == '2':
        generateur()
    elif menu == '3':
        fin = False
    else:
        print("ERROR 404 : Command not found")
