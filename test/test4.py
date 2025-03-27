import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap.constants import *
import sqlite3
from views.content import show_clients, show_commandes, show_employes

def create_horizontal_card(parent, icon, title, value, bootstyle):
    """
    Fonction pour créer une carte horizontale avec une icône, un titre et une valeur.
    """
    card = tk.Frame(parent, bg="#ffffff", bd=1, relief="solid", padx=15, pady=10)
    card.pack(fill="x", padx=10, pady=5)

    # Icône
    icon_label = tk.Label(card, text=icon, font=("Arial", 20), bg="#ffffff", fg="black")
    icon_label.pack(side="left", anchor="center", padx=10)

    # Titre
    title_label = tk.Label(card, text=title, font=("Arial", 14, "bold"), bg="#ffffff", fg="black")
    title_label.pack(side="left", anchor="w")

    # Valeur
    value_label = tk.Label(card, text=value, font=("Arial", 16, "bold"), bg="#ffffff", fg="black")
    value_label.pack(side="right", anchor="e")

    return card

def show_dashboard(content_frame):
    """
    Affiche le tableau de bord avec des cartes dynamiques provenant de la base de données.
    """
    # Efface le contenu précédent
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Connexion à la base de données
    connection = sqlite3.connect("couture.db")
    cursor = connection.cursor()

    # Récupération des statistiques dynamiques
    cursor.execute("SELECT COUNT(*) FROM commandes")
    total_commandes = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM commandes WHERE statut='En attente'")
    commandes_attente = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM commandes WHERE statut='Terminée'")
    commandes_terminees = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(montant) FROM commandes")
    total_revenu = cursor.fetchone()[0] or 0

    cursor.execute("SELECT COUNT(DISTINCT client_id) FROM commandes")
    total_clients = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(DISTINCT employe_id) FROM commandes")
    total_employes = cursor.fetchone()[0]

    connection.close()

    # Conteneur principal des cartes
    cards_frame = tk.Frame(content_frame, bg="#f0f0f0", pady=20)
    cards_frame.pack(fill="both", expand=True)

    # Création des cartes pour chaque statistique avec icônes et valeurs dynamiques
    create_horizontal_card(cards_frame, "📦", "Total Commandes", str(total_commandes), "success")
    create_horizontal_card(cards_frame, "⏳", "Commandes En Attente", str(commandes_attente), "info")
    create_horizontal_card(cards_frame, "✅", "Commandes Terminées", str(commandes_terminees), "warning")
    create_horizontal_card(cards_frame, "💰", "Revenu Total", f"{total_revenu:.2f} €", "primary")
    create_horizontal_card(cards_frame, "👥", "Nombre de Clients", str(total_clients), "secondary")
    create_horizontal_card(cards_frame, "🧑‍💻", "Employés Impliqués", str(total_employes), "light")

def open_main_window():
    """
    Fenêtre principale avec barre de navigation et affichage du tableau de bord.
    """
    # Fenêtre principale stylisée avec ttkbootstrap
    style = Style(theme="solar")
    root = style.master
    root.title("Application - Tableau de Bord")
    root.geometry("1100x600")

    # Cadre principal
    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True)

    # Barre de navigation à gauche
    nav_frame = tk.Frame(main_frame, bg="#2c3e50", width=200, padx=10, pady=10)
    nav_frame.pack(side="left", fill="y")

    # Contenu principal à droite
    content_frame = tk.Frame(main_frame, bg="#f0f0f0")
    content_frame.pack(side="right", fill="both", expand=True)

    # Navigation
    tk.Label(nav_frame, text="Gescouture", font=("Arial", 14, "bold"), fg="white", bg="#34495e").pack(pady=10)
    tk.Button(nav_frame, text="Dashboard", command=lambda: show_dashboard(content_frame), width=20).pack(pady=5)
    tk.Button(nav_frame, text="Clients", command=lambda: show_clients(content_frame), width=20).pack(pady=5)
    tk.Button(nav_frame, text="Commandes", command=lambda: show_commandes(content_frame), width=20).pack(pady=5)
    tk.Button(nav_frame, text="Employés", command=lambda: show_employes(content_frame), width=20).pack(pady=5)

    # Afficher le Dashboard au lancement
    show_dashboard(content_frame)

    root.mainloop()

# Lancer l'application
open_main_window()
