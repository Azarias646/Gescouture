from tkinter import Toplevel, Label, Entry, Button, StringVar, IntVar, ttk
from datetime import datetime
import sqlite3

def open_create_order_form():
    # Fenêtre pour créer une commande
    form_window = Toplevel()
    form_window.title("Créer une commande")
    form_window.geometry("600x400")

    # Variables
    client_var = StringVar()
    modele_var = StringVar()
    qte_var = IntVar()
    date_debut_var = StringVar(value=datetime.now().strftime("%Y-%m-%d"))
    date_fin_var = StringVar()
    montant_var = StringVar()
    employe_var = StringVar()
    avancement_var = StringVar(value="En attente")
    statut_var = StringVar(value="En cours")

    # Widgets
    Label(form_window, text="Client :").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    Entry(form_window, textvariable=client_var).grid(row=0, column=1, padx=10, pady=5)

    Label(form_window, text="Modèle de vêtement :").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    Entry(form_window, textvariable=modele_var).grid(row=1, column=1, padx=10, pady=5)

    Label(form_window, text="Quantité :").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    Entry(form_window, textvariable=qte_var).grid(row=2, column=1, padx=10, pady=5)

    Label(form_window, text="Date début :").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    Entry(form_window, textvariable=date_debut_var).grid(row=3, column=1, padx=10, pady=5)

    Label(form_window, text="Date fin :").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    Entry(form_window, textvariable=date_fin_var).grid(row=4, column=1, padx=10, pady=5)

    Label(form_window, text="Montant total :").grid(row=5, column=0, padx=10, pady=5, sticky="w")
    Entry(form_window, textvariable=montant_var, state="readonly").grid(row=5, column=1, padx=10, pady=5)

    Label(form_window, text="Employé :").grid(row=6, column=0, padx=10, pady=5, sticky="w")
    Entry(form_window, textvariable=employe_var).grid(row=6, column=1, padx=10, pady=5)

    Label(form_window, text="Avancement :").grid(row=7, column=0, padx=10, pady=5, sticky="w")
    ttk.Combobox(form_window, textvariable=avancement_var, values=["En attente", "Coupé", "En couture", "Terminée"]).grid(row=7, column=1, padx=10, pady=5)

    Label(form_window, text="Statut :").grid(row=8, column=0, padx=10, pady=5, sticky="w")
    ttk.Combobox(form_window, textvariable=statut_var, values=["En attente", "En cours", "Terminée", "Annulée"]).grid(row=8, column=1, padx=10, pady=5)

    # Fonction pour enregistrer la commande
    def save_order():
        connection = sqlite3.connect("app.db")
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO commandes (client_id, modele_vetement, qte, date_debut, date_fin, montant, employe_id, avancement, statut)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            client_var.get(), modele_var.get(), qte_var.get(), date_debut_var.get(),
            date_fin_var.get(), montant_var.get(), employe_var.get(), avancement_var.get(), statut_var.get()
        ))
        connection.commit()
        connection.close()
        print("Commande enregistrée avec succès !")
        form_window.destroy()

    # Bouton Enregistrer
    Button(form_window, text="Enregistrer", command=save_order).grid(row=9, column=0, columnspan=2, pady=10)

# Test de la fonction
open_create_order_form()
