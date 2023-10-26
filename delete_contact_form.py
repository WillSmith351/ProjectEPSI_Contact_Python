import tkinter as tk
from tkinter import messagebox
import json

# Création de l'interface graphique.
screen = tk.Tk()
screen.title('Gestionnaire de contact')

fichier_json = 'database_maxime.json'

# Fonction pour sauvegarder les informations de l'utilisateur
def save_information_user():
    nom = name_input.get()
    prenom = surname_input.get()
    telephone = phone_input.get()
    contact_info = f"{nom} - {prenom} - {telephone}"

    titre = title_input.get()
    with open(fichier_json, 'w') as file_user:
        json.dump({titre: {"nom": nom, "prenom": prenom, "telephone": telephone}}, file_user)
    messagebox.showinfo("Sauvegarde réussie", "Le contact a bien été enregistré.")

    if contact_info:
        contact_listbox.insert(tk.END, contact_info)

def delete_user():
    selected_index = contact_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        contact_listbox.delete(index)

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

# Création du libellé pour la liste de contacts.
contact_label = tk.Label(screen, text="Liste de contact :")
contact_label.pack()

# Création de la liste de contacts.
contact_listbox = tk.Listbox(screen)
contact_listbox.pack()

# Création du bouton pour sauvegarder le contact.
contact_button = tk.Button(screen, text="Sauvegarder", command=save_information_user)
contact_button.pack()

supprimer_bouton = tk.Button(screen, text="Supprimer", command=delete_user)
supprimer_bouton.pack()

# Configuration de l'interface graphique.
screen.geometry('1920x1080')
screen.mainloop()