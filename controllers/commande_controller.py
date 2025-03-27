from tkinter import Toplevel, Label, Entry, Button, StringVar, IntVar, messagebox, ttk
from datetime import datetime
import sqlite3
from models.database import create_connection


def get_clients():
    connection = sqlite3.connect("couture.db")
    cursor = connection.cursor()
    cursor.execute("SELECT nom || ' ' || prenom AS full_name FROM clients")
    clients = [row[0] for row in cursor.fetchall()]
    connection.close()
    return clients

def get_employes():
    connection = sqlite3.connect("couture.db")
    cursor = connection.cursor()
    cursor.execute("SELECT nom || ' ' || prenom AS full_name FROM employes")
    employes = [row[0] for row in cursor.fetchall()]
    connection.close()
    return employes


def add_commande(tree):
    # Fenêtre pour créer une commande
    form_window = Toplevel()
    form_window.title("Commande")
    form_window.geometry("600x400")

    # Charger les clients et employés depuis la base de données
    clients = get_clients()
    employes = get_employes()

    # Variables
    client_var = StringVar()
    modele_var = StringVar()
    detail_var = StringVar()
    qte_var = IntVar()
    date_debut_var = StringVar(value=datetime.now().strftime("%Y-%m-%d"))
    date_fin_var = StringVar()
    montant_var = StringVar()
    employe_var = StringVar()
    avancement_var = StringVar()
    statut_var = StringVar()

    # Widgets
    Label(form_window, text="Client :").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    ttk.Combobox(form_window, textvariable=client_var, values=clients, state="readonly", font=(9)).grid(row=0, column=1, padx=10, pady=5)

    Label(form_window, text="Modèle de vêtement :").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    ttk.Combobox(form_window, textvariable=modele_var, font=(9), values=["Chemise", "Pantalon", "Complet", "Tenue", "Robe", "Jupe", "Traditionnel"]).grid(row=1, column=1, padx=10, pady=5)

    Label(form_window, text="Détail :").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    Entry(form_window, textvariable=detail_var, font=(9)).grid(row=2, column=1, padx=10, pady=5)

    Label(form_window, text="Quantité :").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    Entry(form_window, textvariable=qte_var, font=(9)).grid(row=3, column=1, padx=10, pady=5)

    Label(form_window, text="Date début :").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    Entry(form_window, textvariable=date_debut_var, font=(9)).grid(row=4, column=1, padx=10, pady=5)

    Label(form_window, text="Date fin :").grid(row=5, column=0, padx=10, pady=5, sticky="w")
    Entry(form_window, textvariable=date_fin_var, font=(9)).grid(row=5, column=1, padx=10, pady=5)

    Label(form_window, text="Montant :").grid(row=6, column=0, padx=10, pady=5, sticky="w")
    Entry(form_window, textvariable=montant_var, font=(9)).grid(row=6, column=1, padx=10, pady=5)

    Label(form_window, text="Employé :").grid(row=7, column=0, padx=10, pady=5, sticky="w")
    ttk.Combobox(form_window, textvariable=employe_var, values=employes, state="readonly", font=(9)).grid(row=7, column=1, padx=10, pady=5)

    Label(form_window, text="Avancement :").grid(row=8, column=0, padx=10, pady=5, sticky="w")
    ttk.Combobox(form_window, textvariable=avancement_var, font=(9), values=["Pas commencée", "En cours", "Annulée", "Terminée"]).grid(row=8, column=1, padx=10, pady=5)

    Label(form_window, text="Statut :").grid(row=9, column=0, padx=10, pady=5, sticky="w")
    ttk.Combobox(form_window, textvariable=statut_var, font=(9), values=["Non payé", "En partie payé", "Payé"]).grid(row=9, column=1, padx=10, pady=5)

    # Fonction pour enregistrer la commande
    def save_commande():
        connection = sqlite3.connect("couture.db")
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO commandes (client_id, modele_vetement, detail, qte, date_debut, date_fin, montant, employe_id, avancement, statut)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            client_var.get(), modele_var.get(), detail_var.get(), qte_var.get(), date_debut_var.get(),
            date_fin_var.get(), montant_var.get(), employe_var.get(), avancement_var.get(), statut_var.get()
        ))
        connection.commit()
        connection.close()
        print("Commande enregistrée avec succès !")
        form_window.destroy()

    # Bouton Enregistrer
    Button(form_window, text="Valider", command=save_commande, bg="green", font=(11)).grid(row=10, column=0, columnspan=2, pady=10)

    cancel_button = Button(form_window, text="Annuler", command=form_window.destroy, bg="gray", font=(11))
    cancel_button.grid(row=10, column=1, columnspan=2, pady=10)



def delete_commande(tree):
    # Vérifie qu'un employé est sélectionné
    selected_item = tree.selection()
    if not selected_item:
        print("Aucune commande sélectionnée")
        return

    # Boîte de confirmation
    confirm = messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir supprimer cette commande ?")
    if not confirm:
        return  # Si l'utilisateur clique sur "Non", annule l'opération

    # Récupère l'ID de commade sélectionné
    commande_id = tree.item(selected_item)["values"][0] 

    # Supprime la commande de la base de données
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM commandes WHERE id = ?", (commande_id,))
        connection.commit()
        connection.close()

        # Supprime le employe de l'interface
        tree.delete(selected_item)
        print("commande supprimé avec succès.")
    except Exception as e:
        print("Erreur lors de la suppression :", e)


def edit_commande(tree):

     # Vérifie qu'un élément est sélectionné
    selected_item = tree.selection()
    if not selected_item:
        print("Erreur : Aucune commande sélectionnée.")
        return

    # Récupère l'ID de la commande depuis la ligne sélectionnée
    commande_id = tree.item(selected_item)["values"][0]
    print("Commande sélectionnée avec ID :", commande_id)

    # Connexion pour récupérer les informations actuelles de la commande
    connection = sqlite3.connect("couture.db")
    cursor = connection.cursor()
    cursor.execute("SELECT client_id, modele_vetement, detail, qte, date_debut, date_fin, montant, employe_id, avancement, statut FROM commandes WHERE id = ?", (commande_id,))
    commande = cursor.fetchone()
    connection.close()

    if not commande:
        print(f"Commande avec l'ID {commande_id} introuvable.")
        return

    # Variables pour les champs
    client_var = StringVar(value=commande[0])
    modele_var = StringVar(value=commande[1])
    detail_var = StringVar(value=commande[2])
    qte_var = IntVar(value=commande[3])
    date_debut_var = StringVar(value=commande[4])
    date_fin_var = StringVar(value=commande[5])
    montant_var = StringVar(value=commande[6])
    employe_var = StringVar(value=commande[7])
    avancement_var = StringVar(value=commande[8])
    statut_var = StringVar(value=commande[9])

    # Fenêtre de modification
    form_window = Toplevel()
    form_window.title("Commande")
    form_window.geometry("600x400")

    clients = get_clients()
    employes = get_employes()

    # Widgets du formulaire
    Label(form_window, text="Client :").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    ttk.Combobox(form_window, textvariable=client_var, values=clients, state="readonly", font=(9)).grid(row=0, column=1, padx=10, pady=5)

    Label(form_window, text="Modèle de vêtement :").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    ttk.Combobox(form_window, textvariable=modele_var, font=(9), state="readonly", values=["Chemise", "Pantalon", "Complet", "Tenue", "Robe", "Jupe", "Traditionnel"]).grid(row=1, column=1, padx=10, pady=5)

    Label(form_window, text="Détail :").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    Entry(form_window, textvariable=detail_var, font=(9)).grid(row=2, column=1, padx=10, pady=5)

    Label(form_window, text="Quantité :").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    Entry(form_window, textvariable=qte_var, font=(9)).grid(row=3, column=1, padx=10, pady=5)

    Label(form_window, text="Date début :").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    Entry(form_window, textvariable=date_debut_var, font=(9)).grid(row=4, column=1, padx=10, pady=5)

    Label(form_window, text="Date fin :").grid(row=5, column=0, padx=10, pady=5, sticky="w")
    Entry(form_window, textvariable=date_fin_var, font=(9)).grid(row=5, column=1, padx=10, pady=5)

    Label(form_window, text="Montant :").grid(row=6, column=0, padx=10, pady=5, sticky="w")
    Entry(form_window, textvariable=montant_var, font=(9)).grid(row=6, column=1, padx=10, pady=5)

    Label(form_window, text="Employé :").grid(row=7, column=0, padx=10, pady=5, sticky="w")
    ttk.Combobox(form_window, textvariable=employe_var, values=employes, state="readonly", font=(9)).grid(row=7, column=1, padx=10, pady=5)

    Label(form_window, text="Avancement :").grid(row=8, column=0, padx=10, pady=5, sticky="w")
    ttk.Combobox(form_window, textvariable=avancement_var, font=(9), state="readonly", values=["Pas commencée", "En cours", "Annulée", "Terminée"]).grid(row=8, column=1, padx=10, pady=5)

    Label(form_window, text="Statut :").grid(row=9, column=0, padx=10, pady=5, sticky="w")
    ttk.Combobox(form_window, textvariable=statut_var, font=(9), state="readonly", values=["Non payé", "En partie payé", "Payé"]).grid(row=9, column=1, padx=10, pady=5)

    # Fonction pour enregistrer les modifications
    def save_changes():
        connection = sqlite3.connect("couture.db")
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE commandes
            SET client_id = ?, modele_vetement = ?, detail = ?, qte = ?, date_debut = ?, date_fin = ?, montant = ?, employe_id = ?, avancement = ?, statut = ?
            WHERE id = ?
        """, (
            client_var.get(), modele_var.get(), detail_var.get(), qte_var.get(), date_debut_var.get(),
            date_fin_var.get(), montant_var.get(), employe_var.get(), avancement_var.get(), statut_var.get(),
            commande_id
        ))
        connection.commit()
        connection.close()
        #print(f"Commande {commande_id} modifiée avec succès !")
        form_window.destroy()

    # Bouton Enregistrer
    Button(form_window, text="Valider", command=save_changes, bg="green", font=(11)).grid(row=10, column=0, columnspan=2, pady=20)

    cancel_button = Button(form_window, text="Annuler", command=form_window.destroy, bg="gray", font=(11))
    cancel_button.grid(row=10, column=1, columnspan=2, pady=10)