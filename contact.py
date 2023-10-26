import tkinter as tk
from tkinter import messagebox
import json

# Création de l'interface graphique.
screen = tk.Tk()
screen.title('Gestionnaire de contact')

fichier_json = 'database.json'

# Sauvegarde des informations de l'utilisateur
def save_information_user():
    if len(name_input.get()) <= 2 or len(surname_input.get()) <= 2:
        messagebox.showwarning("Attention", "Le nom et le prénom doivent comporter plus de 3 caractères.")
    else:
        contact = {
            "nom": name_input.get(),
            "prenom": surname_input.get(),
            "telephone": phone_input.get()
        }
        title = surname_input.get()

        with open(fichier_json, 'r') as file:
            data = json.load(file)
            
        data[title] = contact
        with open(fichier_json, 'w') as file_user:
            json.dump(data, file_user)
        messagebox.showinfo("Sauvegarde réussie", "Le contact a bien été enregistré.")


# Fonction pour charger les données de la base de données JSON
def charger_base_de_donnees():
    try:
        with open("database.json", "r") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return []
    
    
def modifier_contact():
    # Création de la fenêtre principale
    fenetre = tk.Tk()
    fenetre.title("Modifier Contact")

    # Création de variables tkinter pour stocker les détails du contact
    nom_var = tk.StringVar()
    numero_var = tk.StringVar()
    
    # Fonction pour sauvegarder les données de la base de données JSON
def sauvegarder_base_de_donnees(data):
    with open("database.json", "w") as fichier:
        json.dump(data, fichier, indent=4)


# Création des titres, labels, inputs et boutons.
contact_title = tk.Label(screen, text="Entrez les informations du contact :")
contact_title.pack()

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

#creation du bouton pour edit le contact
edit_button = tk.button(screen, text="Modifier", command=modifier_contact)
edit_button.pack()
EndEdit_button = tk.button(screen, text="Terminé", command=sauvegarder_contact)
EndEdit_button.pack()

# Configuration de l'interface graphique.
screen.geometry('1920x1080')
screen.mainloop()
