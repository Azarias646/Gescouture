import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.dashboard import show_dashboard
from views.content import show_clients, show_commandes, show_employes
import tkinter as tk


def create_nav_frame(root):
    nav_frame = tk.Frame(root, bg="#2c3e50", width=200)
    nav_frame.pack(side="left", fill="y")

    # Titre pour le menu de navigation
    nav_title = tk.Label(nav_frame, text="Couturges", bg="#2c3e50", fg="white", font=("Arial", 14))
    nav_title.pack(pady=20)

    # Boutons de navigation avec actions
    btn_dashboard = tk.Button(
        nav_frame, text="Accueil", bg="#34495e", fg="white", font=("Arial", 12), relief="flat",
        command=lambda: show_dashboard(root.content_frame)
    )
    btn_dashboard.pack(fill="x", pady=10, padx=10)

    btn_commandes = tk.Button(
        nav_frame, text="Commandes", bg="#34495e", fg="white", font=("Arial", 12), relief="flat",
        command=lambda: show_commandes(root.content_frame)
    )
    btn_commandes.pack(fill="x", pady=10, padx=10)

    btn_clients = tk.Button(
    nav_frame, text="Clients", bg="#34495e", fg="white", font=("Arial", 12), relief="flat",
    command=lambda: show_clients(root.content_frame)
    )
    btn_clients.pack(fill="x", pady=10, padx=10)


    btn_employes = tk.Button(
        nav_frame, text="Employés", bg="#34495e", fg="white", font=("Arial", 12), relief="flat",
        command=lambda: show_employes(root.content_frame)
    )
    btn_employes.pack(fill="x", pady=10, padx=10)

    return nav_frame