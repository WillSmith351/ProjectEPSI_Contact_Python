import tkinter as tk
from tkinter import ttk
import json 

app = tk.Tk()
app.title('Gestionnaire de contact')

app.geometry('1920x1080')


listeContacts = []  

try:
    with open('contacts.json', 'r') as fichier:
        contacts = json.load(fichier)

    if contacts:  # Vérifier si la liste de contacts n'est pas vide
        print("Liste des contacts :")
        for contact in contacts:
            print(f"Nom : {contact['Nom']}, Prénom : {contact['Prénom']}, Numéro de téléphone : {contact['Numéro de téléphone']}")
            listeContacts.append(contact)  # Ajouter le contact à la liste listeContacts
    else:
        print("Aucun contact n'a été ajouté pour le moment.")
except FileNotFoundError:
    print("Le fichier 'contacts.json' n'existe pas ou est vide.")

# Maintenant, listeContacts contient la liste des contacts et leurs informations








app.mainloop()