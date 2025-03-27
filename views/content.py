import tkinter as tk
from tkinter import Entry, StringVar, ttk, Scrollbar, HORIZONTAL, VERTICAL
from controllers.client_controller import add_client, delete_client, edit_client
from controllers.commande_controller import add_commande, delete_commande, edit_commande
from controllers.employe_controller import add_employe, delete_employe, edit_employe
from models.database import create_connection


def create_content_frame(root):
    content_frame = tk.Frame(root, bg="#CECECE")
    content_frame.pack(side="right", expand=True, fill="both")
    root.content_frame = content_frame
    return content_frame


def show_content(content_frame, content_text):
    # Efface tout contenu existant
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    # Ajoute le nouveau contenu
    content_label = tk.Label(content_frame, text=content_text, bg="#CECECE", font=("Arial", 18))
    content_label.pack(pady=20)


def show_clients(content_frame):
    # Efface l'ancien contenu
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    # Titre
    title_label = tk.Label(content_frame, text="Gestion des Clients", font=("Arial", 16), bg="#CECECE")
    title_label.pack(pady=10)
    
    # Boutons crud
    buttons_frame = tk.Frame(content_frame, bg="#CECECE")
    buttons_frame.pack(pady=10)

    add_button = tk.Button(buttons_frame, text="Ajouter client", font=("Arial", 13), bg="green", command=lambda: add_client(tree))
    add_button.pack(side="left", padx=5)

    edit_button = tk.Button(buttons_frame, text="Modifier client", font=("Arial", 13), bg="gray", command=lambda: edit_client(tree))
    edit_button.pack(side="left", padx=5)

    delete_button = tk.Button(buttons_frame, text="Supprimer client", font=("Arial", 13), bg="red", command=lambda: delete_client(tree))
    delete_button.pack(side="left", padx=5)

    # Création de la barre de recherche
    search_var = StringVar()

    def search_clients():
        # Récupère la requête de l'utilisateur
        query = search_var.get().lower()
       # print(f"Recherche dans la base de données : {query}")  # Log pour débogage

        # Efface toutes les lignes actuelles du tableau
        for item in tree.get_children():
            tree.delete(item)

        # Exécute la requête SQL pour filtrer
        connection = create_connection()
        cursor = connection.cursor()
        
        # Requête SQL pour chercher dans plusieurs colonnes
        cursor.execute("""
            SELECT * FROM clients
            WHERE LOWER(nom) LIKE ? OR LOWER(prenom) LIKE ? OR LOWER(contact) LIKE ?
        """, (f"%{query}%", f"%{query}%", f"%{query}%"))
        
        rows = cursor.fetchall()
        connection.close()

        # Ajoute les résultats filtrés au tableau
        for row in rows:
            tree.insert("", "end", values=row)
        
        #print(f"Résultats affichés : {len(rows)} clients")

    search_entry = Entry(content_frame, textvariable=search_var, width=40, font=("Arial", 15), bg="snow")
    search_entry.pack(pady=5)
    search_entry.bind("<KeyRelease>", lambda event: search_clients())
    
    # Création du cadre principal pour inclure le tableau et les barres de défilement
    table_frame = ttk.Frame(content_frame)
    table_frame.pack(expand=True, fill="both", padx=10, pady=10)

    # Barres de défilement
    x_scroll = Scrollbar(table_frame, orient=HORIZONTAL)  # Défilement horizontal
    y_scroll = Scrollbar(table_frame, orient=VERTICAL)    # Défilement vertical
    
    # Tableau des clients
    columns = ("ID", "Nom", "Prénom", "Contact", "Epaule", "Poitrine", "Pince", "Long_taille", "Tour_taille", "Long_camisole", "Long_manche", "Tour_manche", "Poignet", "Ceinture", "Bassin", "Long_genou", "Long_jupe", "Long_robe", "Frappe", "Cuisse", "Long_chemise", "Long_pantalon", "Bas")
    tree = ttk.Treeview(table_frame, columns=columns, show="headings", xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

    # Définition des colonnes avec centrage du texte
    tree.heading("ID", text="ID", anchor="center")
    tree.column("ID", width=30, anchor="center") 

    tree.heading("Nom", text="Nom", anchor="center")
    tree.column("Nom", width=150, anchor="center") 

    tree.heading("Prénom", text="Prénom", anchor="center")
    tree.column("Prénom", width=200, anchor="center") 

    tree.heading("Contact", text="Contact", anchor="center")
    tree.column("Contact", width=100, anchor="center") 

    tree.heading("Epaule", text="Epaule", anchor="center")
    tree.column("Epaule", width=90, anchor="center") 

    tree.heading("Poitrine", text="Poitrine", anchor="center")
    tree.column("Poitrine", width=90, anchor="center") 

    tree.heading("Pince", text="Pince", anchor="center")
    tree.column("Pince", width=90, anchor="center") 

    tree.heading("Long_taille", text="Long_taille", anchor="center")
    tree.column("Long_taille", width=90, anchor="center") 

    tree.heading("Tour_taille", text="Tour_taille", anchor="center")
    tree.column("Tour_taille", width=90, anchor="center") 

    tree.heading("Long_camisole", text="Long_camisole", anchor="center")
    tree.column("Long_camisole", width=90, anchor="center") 

    tree.heading("Long_manche", text="Long_manche", anchor="center")
    tree.column("Long_manche", width=90, anchor="center") 

    tree.heading("Tour_manche", text="Tour_manche", anchor="center")
    tree.column("Tour_manche", width=90, anchor="center") 

    tree.heading("Poignet", text="Poignet", anchor="center")
    tree.column("Poignet", width=90, anchor="center") 

    tree.heading("Ceinture", text="Ceinture", anchor="center")
    tree.column("Ceinture", width=90, anchor="center") 

    tree.heading("Bassin", text="Bassin", anchor="center")
    tree.column("Bassin", width=90, anchor="center") 

    tree.heading("Long_genou", text="Long_genou", anchor="center")
    tree.column("Long_genou", width=90, anchor="center") 

    tree.heading("Long_jupe", text="Long_jupe", anchor="center")
    tree.column("Long_jupe", width=90, anchor="center") 

    tree.heading("Long_robe", text="Long_robe", anchor="center")
    tree.column("Long_robe", width=90, anchor="center") 

    tree.heading("Frappe", text="Frappe", anchor="center")
    tree.column("Frappe", width=90, anchor="center") 

    tree.heading("Cuisse", text="Cuisse", anchor="center")
    tree.column("Cuisse", width=90, anchor="center") 

    tree.heading("Long_chemise", text="Long_chemise", anchor="center")
    tree.column("Long_chemise", width=90, anchor="center") 

    tree.heading("Long_pantalon", text="Long_pantalon", anchor="center")
    tree.column("Long_pantalon", width=90, anchor="center") 

    tree.heading("Bas", text="Bas", anchor="center")
    tree.column("Bas", width=90, anchor="center") 

    # Placement des barres de défilement
    x_scroll.pack(side="bottom", fill="x")  # Défilement horizontal en bas
    y_scroll.pack(side="right", fill="y")   # Défilement vertical à droite
    tree.pack(expand=True, fill="both")     # Tableau dans tout l'espace disponible

    # Lier les barres de défilement au tableau
    x_scroll.config(command=tree.xview)
    y_scroll.config(command=tree.yview)

    # Charger les clients depuis la base de données
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM clients")
    rows = cursor.fetchall()
    connection.close()

    for row in rows:
        tree.insert("", "end", values=row)


#EMPLOYES

def show_employes(content_frame):
    # Efface l'ancien contenu
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    # Titre
    title_label = tk.Label(content_frame, text="Gestion des Employés", font=("Arial", 16), bg="#CECECE")
    title_label.pack(pady=10)

    # Boutons crud
    buttons_frame = tk.Frame(content_frame, bg="#CECECE")
    buttons_frame.pack(pady=10)

    add_button = tk.Button(buttons_frame, text="Ajouter employé", font=("Arial", 13), bg="green", command=lambda: add_employe(tree))
    add_button.pack(side="left", padx=5)

    edit_button = tk.Button(buttons_frame, text="Modifier employé", font=("Arial", 13), bg="gray", command=lambda: edit_employe(tree))
    edit_button.pack(side="left", padx=5)

    delete_button = tk.Button(buttons_frame, text="Supprimer employé", font=("Arial", 13), bg="red", command=lambda: delete_employe(tree))
    delete_button.pack(side="left", padx=5)

    # Création de la barre de recherche
    search_var = StringVar()

    def search_employes():
        # Récupère la requête de l'utilisateur
        query = search_var.get().lower()
       # print(f"Recherche dans la base de données : {query}")  # Log pour débogage

        # Efface toutes les lignes actuelles du tableau
        for item in tree.get_children():
            tree.delete(item)

        # Exécute la requête SQL pour filtrer
        connection = create_connection()
        cursor = connection.cursor()
        
        # Requête SQL pour chercher dans plusieurs colonnes
        cursor.execute("""
            SELECT * FROM employes
            WHERE LOWER(nom) LIKE ? OR LOWER(prenom) LIKE ? OR LOWER(contact) LIKE ? OR LOWER(genre) LIKE ? OR LOWER(cnib) LIKE ? OR LOWER(date_naissance) LIKE ?
        """, (f"%{query}%", f"%{query}%", f"%{query}%", f"%{query}%", f"%{query}%", f"%{query}%"))
        
        rows = cursor.fetchall()
        connection.close()

        # Ajoute les résultats filtrés au tableau
        for row in rows:
            tree.insert("", "end", values=row)
        
        #print(f"Résultats affichés : {len(rows)} employes")

    search_entry = Entry(content_frame, textvariable=search_var, width=40, font=("Arial", 15), bg="snow")
    search_entry.pack(pady=5)
    search_entry.bind("<KeyRelease>", lambda event: search_employes())

    # Création du cadre principal pour inclure le tableau et les barres de défilement
    table_frame = ttk.Frame(content_frame)
    table_frame.pack(expand=True, fill="both", padx=10, pady=10)

    # Barres de défilement
    x_scroll = Scrollbar(table_frame, orient=HORIZONTAL)  # Défilement horizontal
    y_scroll = Scrollbar(table_frame, orient=VERTICAL)    # Défilement vertical

    # Tableau des employés
    columns = ("ID", "Nom", "Prénom", "Contact", "Date de naissance", "Genre", "CNIB")
    tree = ttk.Treeview(table_frame, columns=columns, show="headings")

    # Définition des colonnes avec centrage du texte
    tree.heading("ID", text="ID", anchor="center")
    tree.column("ID", width=90, anchor="center") 

    tree.heading("Nom", text="Nom", anchor="center")
    tree.column("Nom", width=150, anchor="center") 

    tree.heading("Prénom", text="Prénom", anchor="center")
    tree.column("Prénom", width=200, anchor="center") 

    tree.heading("Contact", text="Contact", anchor="center")
    tree.column("Contact", width=100, anchor="center") 

    tree.heading("Date de naissance", text="Date de naissance", anchor="center")
    tree.column("Date de naissance", width=150, anchor="center") 

    tree.heading("Genre", text="Genre", anchor="center")
    tree.column("Genre", width=60, anchor="center") 

    tree.heading("CNIB", text="CNIB", anchor="center")
    tree.column("CNIB", width=100, anchor="center") 

    # Placement des barres de défilement
    x_scroll.pack(side="bottom", fill="x")  # Défilement horizontal en bas
    y_scroll.pack(side="right", fill="y")   # Défilement vertical à droite
    tree.pack(expand=True, fill="both")     # Tableau dans tout l'espace disponible

    # Lier les barres de défilement au tableau
    x_scroll.config(command=tree.xview)
    y_scroll.config(command=tree.yview)

    # Charger les employés depuis la base de données
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employes")
    rows = cursor.fetchall()
    connection.close()

    for row in rows:
        tree.insert("", "end", values=row)


#COMMANDES

def show_commandes(content_frame):
    # Efface l'ancien contenu
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    # Titre
    title_label = tk.Label(content_frame, text="Gestion des Commandes", font=("Arial", 16), bg="#CECECE")
    title_label.pack(pady=10)

    # Boutons crud
    buttons_frame = tk.Frame(content_frame, bg="#CECECE")
    buttons_frame.pack(pady=10)

    add_button = tk.Button(buttons_frame, text="Ajouter commande", font=("Arial", 13), bg="green", command=lambda: add_commande(tree))
    add_button.pack(side="left", padx=5)

    edit_button = tk.Button(buttons_frame, text="Modifier commande", font=("Arial", 13), bg="gray", command=lambda: edit_commande(tree))
    edit_button.pack(side="left", padx=5)

    delete_button = tk.Button(buttons_frame, text="Supprimer commande", font=("Arial", 13), bg="red", command=lambda: delete_commande(tree))
    delete_button.pack(side="left", padx=5)

    # Création de la barre de recherche
    search_var = StringVar()

    def search_commandes():
        # Récupère la requête de l'utilisateur
        query = search_var.get().lower()
       # print(f"Recherche dans la base de données : {query}")  # Log pour débogage

        # Efface toutes les lignes actuelles du tableau
        for item in tree.get_children():
            tree.delete(item)

        # Exécute la requête SQL pour filtrer
        connection = create_connection()
        cursor = connection.cursor()
        
        # Requête SQL pour chercher dans plusieurs colonnes
        cursor.execute("""
            SELECT * FROM commandes
            WHERE LOWER(client_id) LIKE ? OR LOWER(modele_vetement) LIKE ? OR LOWER(detail) LIKE ? OR LOWER(qte) LIKE ? OR LOWER(date_debut) LIKE ? OR LOWER(date_fin) LIKE ? OR LOWER(montant) LIKE ? OR LOWER(employe_id) LIKE ? OR LOWER(avancement) LIKE ? OR LOWER(statut) LIKE ?
        """, (f"%{query}%", f"%{query}%", f"%{query}%", f"%{query}%", f"%{query}%", f"%{query}%", f"%{query}%", f"%{query}%", f"%{query}%", f"%{query}%"))
        
        rows = cursor.fetchall()
        connection.close()

        # Ajoute les résultats filtrés au tableau
        for row in rows:
            tree.insert("", "end", values=row)
        
        #print(f"Résultats affichés : {len(rows)} commandes")

    search_entry = Entry(content_frame, textvariable=search_var, width=40, font=("Arial", 15), bg="snow")
    search_entry.pack(pady=5)
    search_entry.bind("<KeyRelease>", lambda event: search_commandes())

    # Création du cadre principal pour inclure le tableau et les barres de défilement
    table_frame = ttk.Frame(content_frame)
    table_frame.pack(expand=True, fill="both", padx=10, pady=10)

    # Barres de défilement
    x_scroll = Scrollbar(table_frame, orient=HORIZONTAL)  # Défilement horizontal
    y_scroll = Scrollbar(table_frame, orient=VERTICAL)    # Défilement vertical

    # Tableau des commandes
    columns = ("ID", "Client", "Modèle", "Détail", "Quantité", "Début", "Fin", "Montant", "Employé", "Avancement", "Statut")
    tree = ttk.Treeview(table_frame, columns=columns, show="headings")

    # Définition des colonnes avec centrage du texte
    tree.heading("ID", text="ID", anchor="center")
    tree.column("ID", width=30, anchor="center") 

    tree.heading("Client", text="Client", anchor="center")
    tree.column("Client", width=100, anchor="center") 

    tree.heading("Modèle", text="Modèle", anchor="center")
    tree.column("Modèle", width=100, anchor="center") 

    tree.heading("Détail", text="Détail", anchor="center")
    tree.column("Détail", width=100, anchor="center") 

    tree.heading("Quantité", text="Quantité", anchor="center")
    tree.column("Quantité", width=30, anchor="center") 

    tree.heading("Début", text="Début", anchor="center")
    tree.column("Début", width=100, anchor="center") 

    tree.heading("Fin", text="Fin", anchor="center")
    tree.column("Fin", width=100, anchor="center") 

    tree.heading("Montant", text="Montant", anchor="center")
    tree.column("Montant", width=100, anchor="center")

    tree.heading("Employé", text="Employé", anchor="center")
    tree.column("Employé", width=100, anchor="center")

    tree.heading("Avancement", text="Avancement", anchor="center")
    tree.column("Avancement", width=80, anchor="center")

    tree.heading("Statut", text="Statut", anchor="center")
    tree.column("Statut", width=80, anchor="center")

    # Placement des barres de défilement
    x_scroll.pack(side="bottom", fill="x")  # Défilement horizontal en bas
    y_scroll.pack(side="right", fill="y")   # Défilement vertical à droite
    tree.pack(expand=True, fill="both")     # Tableau dans tout l'espace disponible

    # Lier les barres de défilement au tableau
    x_scroll.config(command=tree.xview)
    y_scroll.config(command=tree.yview)

    # Charger les commandes depuis la base de données
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM commandes")
    rows = cursor.fetchall()
    connection.close()

    for row in rows:
        tree.insert("", "end", values=row)