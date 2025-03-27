from models.database import create_connection
from tkinter import Toplevel, Label, Entry, Button, StringVar, messagebox


def add_client(tree):
    # Créer une nouvelle fenêtre
    form_window = Toplevel(bg="#DFF2FF")
    form_window.title("Client")
    form_window.geometry("900x400")

    # Liste des champs
    fields = [
        "Nom", "Prénom", "Contact", "Epaule", "Poitrine",
        "Pince", "Long_taille", "Tour_taille", "Long_camisole",
        "Long_manche", "Tour_manche", "Poignet", "Ceinture",
        "Bassin", "Long_genou", "Long_jupe", "Long_robe",
        "Frappe", "Cuisse", "Long_chemise", "Long_pantalon", "Bas"
    ]

    # Création d'une grille pour organiser les champs
    entries = {}  # Stocker les entrées pour validation
    col_count = 3  # Nombre de colonnes
    row, column = 0, 0

    for index, field in enumerate(fields):
        # Crée un champ (label et entrée)
        label = Label(form_window, text=f"{field} :", anchor="w")
        label.grid(row=row, column=column * 2, padx=10, pady=5, sticky="w")

        entry_var = StringVar()
        entry = Entry(form_window, textvariable=entry_var, width=15, font=(7))
        entry.grid(row=row, column=(column * 2) + 1, padx=10, pady=5)
        entries[field] = entry_var  # Associe la variable au champ

        # Gestion de la disposition
        row += 1
        if row >= 8:  # Après 8 champs, passer à la colonne suivante
            row = 0
            column += 1

    # Bouton pour valider les données
    def submit_form():
        data = {field: var.get() for field, var in entries.items()}
        if data["Prénom"] and data["Contact"]:  # Exemple de validation basique
            try:
                # Insère dans la base de données
                with create_connection() as connection:
                    cursor = connection.cursor()
                    cursor.execute("""
                        INSERT INTO clients (nom, prenom, contact, epaule, poitrine, pince, long_taille, tour_taille, long_camisole, long_manche, tour_manche, poignet, ceinture, bassin, long_genou, long_jupe, long_robe, frappe, cuisse, long_chemise, long_pantalon, bas)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (data["Nom"], data["Prénom"], data["Contact"], data["Epaule"],  data["Poitrine"],  data["Pince"],  data["Long_taille"],  data["Tour_taille"],  data["Long_camisole"],  data["Long_manche"],  data["Tour_manche"],  data["Poignet"],  data["Ceinture"],  data["Bassin"],  data["Long_genou"],  data["Long_jupe"],  data["Long_robe"],  data["Frappe"],  data["Cuisse"],  data["Long_chemise"],  data["Long_pantalon"],  data["Bas"]))
                    connection.commit()
                    cursor.close()

                    # Ajoute au tableau
                    tree.insert("", "end", values=(cursor.lastrowid, data["Nom"], data["Prénom"], data["Contact"], data["Epaule"],  data["Poitrine"],  data["Pince"],  data["Long_taille"],  data["Tour_taille"],  data["Long_camisole"],  data["Long_manche"],  data["Tour_manche"],  data["Poignet"],  data["Ceinture"],  data["Bassin"],  data["Long_genou"],  data["Long_jupe"],  data["Long_robe"],  data["Frappe"],  data["Cuisse"],  data["Long_chemise"],  data["Long_pantalon"],  data["Bas"]))
                    print("Client ajouté avec succès :", data)
                    form_window.destroy()  # Ferme le formulaire
            except Exception as e:
                print("Erreur lors de l'ajout :", e)
        else:
            print("Prénom et Contact sont obligatoires.")
        
    submit_button = Button(form_window, text="Valider", command=submit_form, bg="green", font=(11))
    submit_button.grid(row=10, column=0, columnspan=5, pady=20)

    cancel_button = Button(form_window, text="Annuler", command=form_window.destroy, bg="gray", font=(11))
    cancel_button.grid(row=10, column=0, columnspan=6, pady=10)


def delete_client(tree):
    # Vérifie qu'un client est sélectionné
    selected_item = tree.selection()
    if not selected_item:
        print("Aucun client sélectionné.")
        return

    # Boîte de confirmation
    confirm = messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir supprimer ce client ?")
    if not confirm:
        return  # Si l'utilisateur clique sur "Non", annule l'opération

    # Récupère l'ID du client sélectionné
    client_id = tree.item(selected_item)["values"][0] 

    # Supprime le client de la base de données
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM clients WHERE id = ?", (client_id,))
        connection.commit()
        connection.close()

        # Supprime le client de l'interface
        tree.delete(selected_item)
        print("Client supprimé avec succès.")
    except Exception as e:
        print("Erreur lors de la suppression :", e)


def edit_client(tree):
    # Vérifie si un client est sélectionné
    selected_item = tree.selection()
    if not selected_item:
        print("Aucun client sélectionné")
        return

    # Récupère les données du client sélectionné
    selected_values = tree.item(selected_item)["values"]
    client_id = selected_values[0]  # ID du client

    # Nouvelle fenêtre pour le formulaire
    form_window = Toplevel(bg="#DFF2FF")
    form_window.title("Client")
    form_window.geometry("900x400")

    # Liste des champs à modifier
    fields = [
        "Nom", "Prénom", "Contact", "Epaule", "Poitrine",
        "Pince", "Long_taille", "Tour_taille", "Long_camisole",
        "Long_manche", "Tour_manche", "Poignet", "Ceinture",
        "Bassin", "Long_genou", "Long_jupe", "Long_robe",
        "Frappe", "Cuisse", "Long_chemise", "Long_pantalon", "Bas"
    ]

    # Variables pour pré-remplir les champs existants
    entries = {}
    col_count = 3  # Nombre de colonnes
    row, column = 0, 0

    for index, field in enumerate(fields):
        # Crée un champ avec valeur existante (si applicable)
        label = Label(form_window, text=f"{field} :", anchor="w")
        label.grid(row=row, column=column * 2, padx=10, pady=5, sticky="w")

        entry_var = StringVar()
        # Pré-remplissage : utiliser les valeurs existantes si elles existent
        entry_var.set(selected_values[index + 1] if index + 1 < len(selected_values) else "")
        entry = Entry(form_window, textvariable=entry_var, width=25)
        entry.grid(row=row, column=(column * 2) + 1, padx=10, pady=5)
        entries[field] = entry_var

        # Gestion de la disposition
        row += 1
        if row >= 8:
            row = 0
            column += 1

    # Fonction de mise à jour
    def update_client():
        data = {field: var.get() for field, var in entries.items()}
        if data["Prénom"] and data["Contact"]:  # Validation minimale
            try:
                # Mise à jour dans la base de données
                connection = create_connection()
                cursor = connection.cursor()
                cursor.execute("""
                    UPDATE clients
                SET nom = ?, prenom = ?, contact = ?, epaule = ?, poitrine = ?, pince = ?, long_taille = ?, tour_taille = ?, long_camisole = ?, long_manche = ?, tour_manche = ?, poignet = ?, ceinture = ?, bassin = ?, long_genou = ?, long_jupe = ?, long_robe = ?, frappe = ?, cuisse = ?, long_chemise = ?, long_pantalon = ?, bas = ?
                WHERE id = ?
                """, (data["Nom"], data["Prénom"], data["Contact"], data["Epaule"],  data["Poitrine"],  data["Pince"],  data["Long_taille"],  data["Tour_taille"],  data["Long_camisole"],  data["Long_manche"],  data["Tour_manche"],  data["Poignet"],  data["Ceinture"],  data["Bassin"],  data["Long_genou"],  data["Long_jupe"],  data["Long_robe"],  data["Frappe"],  data["Cuisse"],  data["Long_chemise"],  data["Long_pantalon"],  data["Bas"], client_id))
                connection.commit()
                connection.close()

                # Mise à jour directe dans le tableau
                tree.item(selected_item, values=(client_id, data["Nom"], data["Prénom"], data["Contact"], data["Epaule"],  data["Poitrine"],  data["Pince"],  data["Long_taille"],  data["Tour_taille"],  data["Long_camisole"],  data["Long_manche"],  data["Tour_manche"],  data["Poignet"],  data["Ceinture"],  data["Bassin"],  data["Long_genou"],  data["Long_jupe"],  data["Long_robe"],  data["Frappe"],  data["Cuisse"],  data["Long_chemise"],  data["Long_pantalon"],  data["Bas"]))
                print("Client modifié avec succès :", data)
                form_window.destroy()  # Ferme le formulaire
            except Exception as e:
                print("Erreur lors de la mise à jour :", e)
        else:
            print("Prénom et Contact sont obligatoires.")

    # Bouton pour valider les modifications
    update_button = Button(form_window, text="Modifier", command=update_client, bg="green", font=(11))
    update_button.grid(row=10, column=0, columnspan=5, pady=20)

    # Bouton pour annuler
    cancel_button = Button(form_window, text="Annuler", command=form_window.destroy, bg="gray", font=(11))
    cancel_button.grid(row=10, column=0, columnspan=6, pady=10)
