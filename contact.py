import tkinter as tk
from tkinter import messagebox
import json
import re

# Création de l'interface graphique.
screen = tk.Tk()
screen.title('Gestionnaire de contacts')

# Création de la base de données en fichier JSON
fichier_json = 'database.json'

# Sauvegarde des informations de l'utilisateur
def save_information_user():
    if len(name_input.get()) <= 2 or len(surname_input.get()) <= 2:
        messagebox.showwarning("Attention", "Le nom et le prénom doivent comporter plus de 3 caractères.")
    elif not re.match("^[0-9]*$", phone_input.get()):
        messagebox.showwarning("Attention", "Le numéro de téléphone ne peut contenir que des chiffres.")
    elif not re.match("^\d{10}$", phone_input.get()):
        messagebox.showwarning("Attention", "Le numéro de téléphone doit contenir exactement 10 chiffres.")
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

# Suppression d'un contact
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

    popup.geometry('400x100')
    popup.mainloop()

def modifier_contact():
    def open_modify_window(contact):
        modify_screen = tk.Tk()
        modify_screen.title("Modifier Contact")
        modify_screen.geometry('400x200')

        label_nom = tk.Label(modify_screen, text="Nom:")
        label_nom.pack()
        nom_input = tk.Entry(modify_screen, width=30)
        nom_input.pack()
        nom_input.insert(0, contact["nom"])

        label_telephone = tk.Label(modify_screen, text="Numéro de téléphone:")
        label_telephone.pack()
        telephone_input = tk.Entry(modify_screen, width=30)
        telephone_input.pack()
        telephone_input.insert(0, contact["telephone"])

        def save_modifications():
            modified_contact = {
                "nom": nom_input.get(),
                "prenom": contact["prenom"],
                "telephone": telephone_input.get()
            }
            with open(fichier_json, 'r') as file:
                data = json.load(file)
            data[contact["prenom"]] = modified_contact
            with open(fichier_json, 'w') as file_user:
                json.dump(data, file_user)
            messagebox.showinfo("Sauvegarde réussie", "Le contact a été modifié avec succès.")
            modify_screen.destroy()

        save_button = tk.Button(modify_screen, text="Enregistrer les modifications", command=save_modifications)
        save_button.pack()

        modify_screen.mainloop()

    def get_contact_to_modify():
        prenom = contact_input.get()
        with open(fichier_json, 'r') as file:
            data = json.load(file)
        if prenom in data:
            contact = data[prenom]
            open_modify_window(contact)
        else:
            messagebox.showwarning("Avertissement", f"Le contact {prenom} n'existe pas dans la base de données.")

    screen_modify = tk.Tk()
    screen_modify.title("Modifier Contact")
    screen_modify.geometry('400x100')

    label = tk.Label(screen_modify, text="Quel contact voulez-vous modifier?")
    label.pack()
    contact_input = tk.Entry(screen_modify)
    contact_input.pack()

    modify_button = tk.Button(screen_modify, text="Modifier", command=get_contact_to_modify)
    modify_button.pack()

    screen_modify.mainloop()

def delete_all_users():
    try:
        with open(fichier_json, 'w') as file:
            file.write("{}") 
        messagebox.showinfo("Suppression réussie", "Tous les contacts ont été supprimés avec succès.")
    except FileNotFoundError:
        messagebox.showerror("Erreur", "Le fichier 'database.json' n'existe pas ou est vide.")

# Création des éléments de l'application :
contact_title = tk.Label(screen, text="Entrez les informations du contact :", bg="white", font=("Helvetica", 16, "bold"))
contact_title.pack(pady=10)

name_label = tk.Label(screen, text="Nom :", font=("Helvetica", 12))
name_label.pack()
name_input = tk.Entry(screen, font=("Helvetica", 12), borderwidth=2, relief="solid")
name_input.pack()

surname_label = tk.Label(screen, text="Prénom :", font=("Helvetica", 12))
surname_label.pack()
surname_input = tk.Entry(screen, font=("Helvetica", 12), borderwidth=2, relief="solid")
surname_input.pack()

phone_label = tk.Label(screen, text="Numéro de téléphone :", font=("Helvetica", 12))
phone_label.pack()
phone_input = tk.Entry(screen, font=("Helvetica", 12), borderwidth=2, relief="solid")
phone_input.pack()

contact_button = tk.Button(screen, text="Sauvegarder", borderwidth=5, relief='raised', bg="green", fg="white", font=("Helvetica", 12, "bold"), padx=10, pady=5, command=save_information_user)
contact_button.pack(pady=10)

contact_label = tk.Label(screen, text="Liste de contacts :", bg="white", font=("Helvetica", 16, "bold"))
contact_label.pack(pady=10)

listeContacts = tk.Text(screen, height=10, width=40, fg="black", borderwidth=2, padx=5, pady=5)
listeContacts.pack()

bouton_afficher_contacts = tk.Button(screen, text="Afficher Contacts", borderwidth=5, relief='raised', bg="blue", fg="white", font=("Helvetica", 12, "bold"), padx=10, pady=5, command=afficher_liste_contacts_tkinter)
bouton_afficher_contacts.pack(pady=10)

delete_contact_button = tk.Button(screen, text="Supprimer un contact", borderwidth=5, relief='raised', bg="red", fg="white", font=("Helvetica", 12, "bold"), padx=10, pady=5, command=supprimer_contact)
delete_contact_button.pack(pady=10)

delete_all_users_button = tk.Button(screen, text="Supprimer tous les contacts", borderwidth=5, relief='raised', bg="Black", fg="white", font=("Helvetica", 12, "bold"), padx=10, pady=5, command=delete_all_users)
delete_all_users_button.pack(pady=10)

bouton_editer = tk.Button(screen, text="Éditer", borderwidth=5, relief='raised', bg="white", fg="blue", font=("Helvetica", 12, "bold"), padx=10, pady=5,  command=modifier_contact)
bouton_editer.pack()

# Configuration de l'interface graphique :
screen.geometry('600x800')
screen.configure(bg="#ECF8F6")
screen.mainloop()
