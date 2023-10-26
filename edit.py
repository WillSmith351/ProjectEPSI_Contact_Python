import tkinter as tk
import json

# Fonction pour charger les données de la base de données JSON
def charger_base_de_donnees():
    try:
        with open("database.json", "r") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return []

# Fonction pour sauvegarder les données de la base de données JSON
def sauvegarder_base_de_donnees(data):
    with open("database.json", "w") as fichier:
        json.dump(data, fichier, indent=4)

def modifier_contact():
    # Création de la fenêtre principale
    fenetre = tk.Tk()
    fenetre.title("Modifier Contact")

    # Création de variables tkinter pour stocker les détails du contact
    nom_var = tk.StringVar()
    numero_var = tk.StringVar()

    # Chargement de la base de données existante

def modifier_contact():
    # Création de la fenêtre principale
    screen = tk.Tk()
    screen.title("Modifier Contact")

    # Création de variables tkinter pour stocker les détails du contact
    nom_var = tk.StringVar()
    numero_var = tk.StringVar()
    
    # Fonction pour mettre à jour les détails du contact
    def sauvegarder_contact():
        nom = nom_var.get()
        numero = numero_var.get()
        
        # Vous pouvez ajouter du code pour enregistrer les détails du contact dans une base de données ou un fichier ici
        print("Contact modifié :")
        print("Nom:", nom)
        print("Numéro de téléphone:", numero)
        
        screen.destroy()  # Ferme la fenêtre après avoir sauvegardé les modifications

    # Création des libellés et des champs de saisie
    label_nom = tk.Label(screen, text="Nom:")
    label_nom.pack()
    entry_nom = tk.Entry(screen, textvariable=nom_var)
    entry_nom.pack()
    label_numero = tk.Label(screen, text="Numéro de téléphone:")
    label_numero.pack()
    entry_numero = tk.Entry(screen, textvariable=numero_var)
    entry_numero.pack()
    # Bouton pour enregistrer les modif
    bouton_sauvegarder = tk.Button(screen, text="Enregistrer", command=sauvegarder_contact)
    bouton_sauvegarder.pack()


