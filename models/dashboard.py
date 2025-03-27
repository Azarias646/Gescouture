import tkinter as tk
#from ttkbootstrap.constants import *
import sqlite3

def create_card(parent, icon, title, value, bootstyle):
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

    cursor.execute("SELECT COUNT(*) FROM commandes WHERE statut='Non payé'")
    commandes_unsold = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM commandes WHERE avancement='Terminée'")
    commandes_terminees = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(montant) FROM commandes")
    total_revenu = cursor.fetchone()[0] or 0

    cursor.execute("SELECT COUNT(*) FROM clients")
    total_clients = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(DISTINCT employe_id) FROM commandes")
    total_employes = cursor.fetchone()[0]

    connection.close()

    # Titre
    title_label = tk.Label(content_frame, text="Accueil", font=("Arial", 16), bg="#CECECE")
    title_label.pack(pady=10)

    # Conteneur principal des cartes
    cards_frame = tk.Frame(content_frame, bg="#CECECE", pady=20)
    cards_frame.pack(fill="both", expand=True)

    # Création des cartes pour chaque statistique avec icônes et valeurs dynamiques
    create_card(cards_frame, "📦", "Total Commandes", str(total_commandes), "success")
    create_card(cards_frame, "⏳", "Commandes Impayées", str(commandes_unsold), "info")
    create_card(cards_frame, "✅", "Commandes Terminées", str(commandes_terminees), "warning")
    create_card(cards_frame, "💰", "Revenu Total", f"{total_revenu:.2f} Fcfa", "primary")
    create_card(cards_frame, "👥", "Nombre de Clients", str(total_clients), "secondary")
    create_card(cards_frame, "🧑‍💻", "Employés Impliqués", str(total_employes), "light")
