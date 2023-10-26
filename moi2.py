import tkinter as tk
import json

fenetre = tk.Tk()
fenetre.title("Gestionnaire de Contacts")
fenetre.geometry("1920x1080")
fichier_json = 'databasewill.json'


def charger_base_de_donnees():
    try:
        with open("databasewill.json", "r") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return []

def sauvegarder_base_de_donnees(data):
    with open("databasewill.json", "w") as fichier:
        json.dump(data, fichier, indent=4)

def ajouter_contact():
    nom = nom_var.get()
    numero = numero_var.get()
    adresse = adresse_var.get()

    if nom and numero:
        contact = {
            "Nom": nom,
            "Numéro de téléphone": numero,
            "Adresse": adresse
        }

        base_de_donnees.append(contact)
        sauvegarder_base_de_donnees(base_de_donnees)
        actualiser_liste_contacts()
        effacer_champs()
    else:
        label_message.config(text="Veuillez remplir les champs Nom et Numéro de téléphone.")

def actualiser_liste_contacts():
    liste_contacts.delete(0, tk.END)
    for contact in base_de_donnees:
        liste_contacts.insert(tk.END, contact["Nom"])

def charger_details_contact(event):
    selection = liste_contacts.curselection()
    if selection:
        contact_index = selection[0]
        contact = base_de_donnees[contact_index]
        nom_var.set(contact["Nom"])
        numero_var.set(contact["Numéro de téléphone"])
        adresse_var.set(contact["Adresse"])

def editer_contact():
    selection = liste_contacts.curselection()
    if selection:
        contact_index = selection[0]
        nom = nom_var.get()
        numero = numero_var.get()
        adresse = adresse_var.get()

        if nom and numero:
            base_de_donnees[contact_index]["Nom"] = nom
            base_de_donnees[contact_index]["Numéro de téléphone"] = numero
            base_de_donnees[contact_index]["Adresse"] = adresse
            sauvegarder_base_de_donnees(base_de_donnees)
            actualiser_liste_contacts()
            effacer_champs()
        else:
            label_message.config(text="Veuillez remplir les champs Nom et Numéro de téléphone.")

def supprimer_contact():
    selection = liste_contacts.curselection()
    if selection:
        contact_index = selection[0]
        base_de_donnees.pop(contact_index)
        sauvegarder_base_de_donnees(base_de_donnees)
        actualiser_liste_contacts()
        effacer_champs()

def effacer_champs():
    nom_var.set("")
    numero_var.set("")
    adresse_var.set("")

def ouvrir_fenetre_modification():
    selection = liste_contacts.curselection()
    if selection:
        contact_index = selection[0]
        contact = base_de_donnees[contact_index]

        # Création d'une nouvelle fenêtre pour la modification
        fenetre_modification = tk.Toplevel()
        fenetre_modification.title("Modifier Contact")

        # Création des variables tkinter pour la fenêtre de modification
        nom_modif_var = tk.StringVar()
        numero_modif_var = tk.StringVar()
        adresse_modif_var = tk.StringVar()

        # Fonction pour sauvegarder la modification
        def sauvegarder_modification():
            nom_modif = nom_modif_var.get()
            numero_modif = numero_modif_var.get()
            adresse_modif = adresse_modif_var.get()

            if nom_modif and numero_modif:
                base_de_donnees[contact_index]["Nom"] = nom_modif
                base_de_donnees[contact_index]["Numéro de téléphone"] = numero_modif
                base_de_donnees[contact_index]["Adresse"] = adresse_modif
                sauvegarder_base_de_donnees(base_de_donnees)
                fenetre_modification.destroy()
                actualiser_liste_contacts()
            else:
                label_message_modif.config(text="Veuillez remplir les champs Nom et Numéro de téléphone.")

        # Création des libellés et des champs de saisie pour la fenêtre de modification
        label_nom_modif = tk.Label(fenetre_modification, text="Nom:")
        entry_nom_modif = tk.Entry(fenetre_modification, textvariable=nom_modif_var)
        label_numero_modif = tk.Label(fenetre_modification, text="Numéro de téléphone:")
        entry_numero_modif = tk.Entry(fenetre_modification, textvariable=numero_modif_var)
        label_adresse_modif = tk.Label(fenetre_modification, text="Adresse:")
        entry_adresse_modif = tk.Entry(fenetre_modification, textvariable=adresse_modif_var)

        # Libellé pour afficher des messages de modification
        label_message_modif = tk.Label(fenetre_modification, text="")

        # Bouton pour enregistrer la modification
        bouton_sauvegarder_modif = tk.Button(fenetre_modification, text="Enregistrer", command=sauvegarder_modification)

        # Placement des éléments dans la fenêtre de modification
        label_nom_modif.pack()
        entry_nom_modif.pack()
        label_numero_modif.pack()
        entry_numero_modif.pack()
        label_adresse_modif.pack()
        entry_adresse_modif.pack()
        bouton_sauvegarder_modif.pack()
        label_message_modif.pack()

        # Remplir les champs de la fenêtre de modification avec les données existantes
        nom_modif_var.set(contact["Nom"])
        numero_modif_var.set(contact["Numéro de téléphone"])
        adresse_modif_var.set(contact["Adresse"])


nom_var = tk.StringVar()
numero_var = tk.StringVar()
adresse_var = tk.StringVar()

base_de_donnees = charger_base_de_donnees()

label_liste_contacts = tk.Label(fenetre, text="Liste des Contacts")
label_liste_contacts.pack()

liste_contacts = tk.Listbox(fenetre, selectmode=tk.SINGLE)
liste_contacts.pack()

liste_contacts.bind('<<ListboxSelect>>', charger_details_contact)

label_details_contact = tk.Label(fenetre, text="Détails du Contact")
label_details_contact.pack()

label_nom = tk.Label(fenetre, text="Nom:")
entry_nom = tk.Entry(fenetre, textvariable=nom_var)
label_numero = tk.Label(fenetre, text="Numéro de téléphone:")
entry_numero = tk.Entry(fenetre, textvariable=numero_var)
label_adresse = tk.Label(fenetre, text="Adresse:")
entry_adresse = tk.Entry(fenetre, textvariable=adresse_var)

label_message = tk.Label(fenetre, text="")
label_message.pack()

bouton_ajouter = tk.Button(fenetre, text="Ajouter", command=ajouter_contact)
bouton_editer = tk.Button(fenetre, text="Éditer", command=ouvrir_fenetre_modification)
bouton_supprimer = tk.Button(fenetre, text="Supprimer", command=supprimer_contact)

bouton_effacer = tk.Button(fenetre, text="Effacer", command=effacer_champs)

label_nom.pack()
entry_nom.pack()
label_numero.pack()
entry_numero.pack()
label_adresse.pack()
entry_adresse.pack()
bouton_ajouter.pack()
bouton_editer.pack()
bouton_supprimer.pack()
bouton_effacer.pack()


fenetre.mainloop()
