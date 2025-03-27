from models.database import create_connection
from tkinter import Toplevel, Label, Entry, Button, StringVar, messagebox


def add_employe(tree):
    # Créer une nouvelle fenêtre
    form_window = Toplevel(bg="#DFF2FF")
    form_window.title("Employé")
    form_window.geometry("800x300")

    # Liste des champs
    fields = [
        "Nom", "Prénom", "Contact", "Date de naissance", "Genre", "CNIB"
    ]

    # Création d'une grille pour organiser les champs
    entries = {}  # Stocker les entrées pour validation
    col_count = 2  # Nombre de colonnes
    row, column = 0, 0

    for index, field in enumerate(fields):
        # Crée un champ (label et entrée)
        label = Label(form_window, text=f"{field} :", anchor="w", font=(9))
        label.grid(row=row, column=column * 2, padx=10, pady=5, sticky="w")

        entry_var = StringVar()
        entry = Entry(form_window, textvariable=entry_var, width=15, font=(9))
        entry.grid(row=row, column=(column * 2) + 1, padx=10, pady=5)
        entries[field] = entry_var  # Associe la variable au champ

        # Gestion de la disposition
        row += 1
        if row >= 3:  # Après 3 champs, passer à la colonne suivante
            row = 0
            column += 1

    # Bouton pour valider les données
    def submit_form():
        data = {field: var.get() for field, var in entries.items()}
        if data["CNIB"] and data["Contact"]:  # Exemple de validation basique
            try:
                # Insère dans la base de données
                with create_connection() as connection:
                    cursor = connection.cursor()
                    cursor.execute("""
                        INSERT INTO employes (nom, prenom, contact, date_naissance, genre, cnib)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (data["Nom"], data["Prénom"], data["Contact"], data["Date de naissance"],  data["Genre"],  data["CNIB"]))
                    connection.commit()
                    cursor.close()

                    # Ajoute au tableau
                    tree.insert("", "end", values=(cursor.lastrowid, data["Nom"], data["Prénom"], data["Contact"], data["Date de naissance"],  data["Genre"],  data["CNIB"]))
                    print("Employé ajouté avec succès :", data)
                    form_window.destroy()  # Ferme le formulaire
            except Exception as e:
                print("Erreur lors de l'ajout :", e)
        else:
            print("CNIB et Contact sont obligatoires.")
        
    submit_button = Button(form_window, text="Valider", command=submit_form, bg="green", font=(11))
    submit_button.grid(row=10, column=0, columnspan=3, pady=20)

    cancel_button = Button(form_window, text="Annuler", command=form_window.destroy, bg="gray", font=(11))
    cancel_button.grid(row=10, column=0, columnspan=6, pady=10)


def delete_employe(tree):
    # Vérifie qu'un employé est sélectionné
    selected_item = tree.selection()
    if not selected_item:
        print("Aucun employé sélectionné.")
        return

    # Boîte de confirmation
    confirm = messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir supprimer cet employé ?")
    if not confirm:
        return  # Si l'utilisateur clique sur "Non", annule l'opération

    # Récupère l'ID de employé sélectionné
    employe_id = tree.item(selected_item)["values"][0] 

    # Supprime le employe de la base de données
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM employes WHERE id = ?", (employe_id,))
        connection.commit()
        connection.close()

        # Supprime le employe de l'interface
        tree.delete(selected_item)
        print("employé supprimé avec succès.")
    except Exception as e:
        print("Erreur lors de la suppression :", e)


def edit_employe(tree):
    # Vérifie si un employe est sélectionné
    selected_item = tree.selection()
    if not selected_item:
        print("Aucun employe sélectionné")
        return

    # Récupère les données du employe sélectionné
    selected_values = tree.item(selected_item)["values"]
    employe_id = selected_values[0]  # ID du employe

    # Nouvelle fenêtre pour le formulaire
    form_window = Toplevel(bg="#DFF2FF")
    form_window.title("Employé")
    form_window.geometry("900x400")

    # Liste des champs à modifier
    fields = [
        "Nom", "Prénom", "Contact", "Date de naissance", "Genre", "CNIB"
    ]

    # Variables pour pré-remplir les champs existants
    entries = {}
    col_count = 2  # Nombre de colonnes
    row, column = 0, 0

    for index, field in enumerate(fields):
        # Crée un champ avec valeur existante (si applicable)
        label = Label(form_window, text=f"{field} :", anchor="w")
        label.grid(row=row, column=column * 2, padx=10, pady=15, sticky="w")

        entry_var = StringVar()
        # Pré-remplissage : utiliser les valeurs existantes si elles existent
        entry_var.set(selected_values[index + 1] if index + 1 < len(selected_values) else "")
        entry = Entry(form_window, textvariable=entry_var, width=25)
        entry.grid(row=row, column=(column * 2) + 1, padx=10, pady=15)
        entries[field] = entry_var

        # Gestion de la disposition
        row += 1
        if row >= 3:
            row = 0
            column += 1

    # Fonction de mise à jour
    def update_employe():
        data = {field: var.get() for field, var in entries.items()}
        if data["CNIB"] and data["Contact"]:  # Validation minimale
            try:
                # Mise à jour dans la base de données
                connection = create_connection()
                cursor = connection.cursor()
                cursor.execute("""
                    UPDATE employes
                SET nom = ?, prenom = ?, contact = ?, date_naissance = ?, genre = ?, cnib = ?
                WHERE id = ?
                """, (data["Nom"], data["Prénom"], data["Contact"], data["Date de naissance"],  data["Genre"],  data["CNIB"], employe_id))
                connection.commit()
                connection.close()

                # Mise à jour directe dans le tableau
                tree.item(selected_item, values=(employe_id, data["Nom"], data["Prénom"], data["Contact"], data["Date de naissance"],  data["Genre"],  data["CNIB"]))
                print("employé modifié avec succès :", data)
                form_window.destroy()  # Ferme le formulaire
            except Exception as e:
                print("Erreur lors de la mise à jour :", e)
        else:
            print("CNIB et Contact sont obligatoires.")

    # Bouton pour valider les modifications
    update_button = Button(form_window, text="Modifier", command=update_employe, bg="green", font=(11))
    update_button.grid(row=10, column=0, columnspan=3, pady=20)

    # Bouton pour annuler
    cancel_button = Button(form_window, text="Annuler", command=form_window.destroy, bg="gray", font=(11))
    cancel_button.grid(row=10, column=0, columnspan=6, pady=10)
