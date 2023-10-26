import tkinter as tk
from tkinter import messagebox
import json

# Création de l'interface graphique.
screen = tk.Tk()
screen.title('Gestionnaire de contact')

# Création de la base de données en fichier JSON
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


# Affichage des contacts.
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
                contact_info = f"Nom : {nom},\n Prénom : {prenom},\n Numéro de téléphone : {telephone}\n\n"
                listeContacts.insert(tk.END, contact_info)
        else:
            listeContacts.insert(tk.END, "Aucun contact n'a été ajouté pour le moment.")
    except FileNotFoundError:
        listeContacts.insert(tk.END, "Le fichier 'database.json' n'existe pas ou est vide.")


# Suppresion d'un contact
def supprimer_contact():
    def supprimer():
        prenom = contact_input.get()
        try:
            with open('database.json', 'r') as fichier:
                data = json.load(fichier)

            if prenom in data:
                del data[prenom]
                with open('database.json', 'w') as fichier:
                    json.dump(data, fichier, indent=4)
                messagebox.showinfo("Suppression réussie", f"Le contact {prenom} a été supprimé avec succès.")
            else:
                messagebox.showwarning("Avertissement", f"Le contact {prenom} n'existe pas dans la base de données.")

            popup.destroy()

        except FileNotFoundError:
            messagebox.showerror("Erreur", "Le fichier 'database.json' n'existe pas ou est vide.")

    popup = tk.Tk()
    popup.title("Supprimer un contact")

    label = tk.Label(popup, text="Quel contact voulez-vous supprimer?")
    label.pack()

    contact_input = tk.Entry(popup)
    contact_input.pack()

    delete_button = tk.Button(popup, text="Supprimer", command=supprimer)
    delete_button.pack()

    popup.geometry('400x300')
    popup.mainloop()


# ~~ Création des items de l'application : ~~

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

contact_button = tk.Button(screen, text="Sauvegarder", command=save_information_user)
contact_button.pack()

listeContacts = tk.Text(screen, height=10, width=40)
listeContacts.pack()

bouton_afficher_contacts = tk.Button(screen, text="Afficher Contacts", command=afficher_liste_contacts_tkinter)
bouton_afficher_contacts.pack()

delete_contact_button = tk.Button(screen, text="Supprimer un contact", command=supprimer_contact)
delete_contact_button.pack()


#creation du bouton pour edit le contact
edit_button = tk.button(screen, text="Modifier", command=modifier_contact)
edit_button.pack()
# EndEdit_button = tk.button(screen, text="Terminé", command=sauvegarder_contact)
# EndEdit_button.pack()


# ~~ Configuration de l'interface graphique : ~~

screen.geometry('1920x1080')
screen.mainloop()

