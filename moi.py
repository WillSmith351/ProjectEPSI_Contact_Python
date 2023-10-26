import tkinter as tk
from tkinter import messagebox
import json

# Création de l'interface graphique.
screen = tk.Tk()
screen.title('Gestionnaire de contact')

fichier_json = 'database.json'

# Sauvegarde des informations de l'utilisateur
def save_information_user():
    if len(name_input.get()) <= 3 or len(surname_input.get()) <= 3:
        messagebox.showwarning("Attention", "Le nom et le prénom doivent comporter plus de 3 caractères.")
    else:
        contact = {
            "nom": name_input.get(),
            "prenom": surname_input.get(),
            "telephone": phone_input.get()
        }
        titre = title_input.get()

        with open(fichier_json, 'r') as file:
            data = json.load(file)
            
        data[titre] = contact
        with open(fichier_json, 'w') as file_user:
            json.dump(data, file_user)
        messagebox.showinfo("Sauvegarde réussie", "Le contact a bien été enregistré.")

# Création des titres, labels, inputs et boutons.
contact_title = tk.Label(screen, text="Entrez les informations du contact :")
contact_title.pack()

title_label = tk.Label(screen, text="Titre du contact :")
title_label.pack()
title_input = tk.Entry(screen)
title_input.pack()

name_label = tk.Label(screen, text="Nom :")
name_label.pack()
name_input = tk.Entry(screen)
name_input.pack()

surname_label = tk.Label(screen, text="Prénom :")
surname_label.pack()
surname_input = tk.Entry(screen)
surname_input.pack()

phone_label = tk.Label(screen, text="Numéro de téléphone :")
phone_label.pack()
phone_input = tk.Entry(screen)
phone_input.pack()

# Création du bouton pour sauvegarder le contact. 
contact_button = tk.Button(screen, text="Sauvegarder", command=save_information_user)
contact_button.pack()



listeContacts = tk.Text(screen, height=10, width=40)
listeContacts.pack()

def afficher_liste_contacts_tkinter():
    listeContacts.delete(1.0, tk.END)  # Effacer le contenu précédent

    try:
        with open('database.json', 'r') as fichier:
            data = json.load(fichier)

        if data:  # Vérifier si le fichier JSON n'est pas vide
            listeContacts.insert(tk.END, "Liste des contacts :\n")
            for key, contact in data.items():
                nom = contact.get('nom', 'N/A')
                prenom = contact.get('prenom', 'N/A')
                telephone = contact.get('telephone', 'N/A')
                contact_info = f"Nom : {nom},\n Prénom : {prenom},\n Numéro de téléphone : {telephone}\n"
                listeContacts.insert(tk.END, contact_info)
        else:
            listeContacts.insert(tk.END, "Aucun contact n'a été ajouté pour le moment.")
    except FileNotFoundError:
        listeContacts.insert(tk.END, "Le fichier 'database.json' n'existe pas ou est vide.")

bouton_afficher_contacts = tk.Button(screen, text="Afficher Contacts", command=afficher_liste_contacts_tkinter)
bouton_afficher_contacts.pack()


screen.geometry('1920x1080')
screen.mainloop()