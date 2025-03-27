import tkinter as tk
from tkinter import ttk

# Fonction pour changer le contenu affiché
def show_content(content_frame, content_text):
    # Effacer l'ancien contenu
    for widget in content_frame.winfo_children():
        widget.destroy()
    # Ajouter le nouveau contenu
    content_label = tk.Label(content_frame, text=content_text, bg="white", font=("Arial", 16))
    content_label.pack(pady=20)

# Créer la fenêtre principale
root = tk.Tk()
root.title("Dashboard")
root.geometry("800x500")  # Largeur x Hauteur

# Cadre pour la navigation à gauche
nav_frame = tk.Frame(root, bg="#2c3e50", width=200)
nav_frame.pack(side="left", fill="y")

# Titre pour le menu de navigation
nav_title = tk.Label(nav_frame, text="Navigation", bg="#2c3e50", fg="white", font=("Arial", 14))
nav_title.pack(pady=20)

# Cadre principal pour le contenu
content_frame = tk.Frame(root, bg="white")
content_frame.pack(side="right", expand=True, fill="both")

# Affichage initial
show_content(content_frame, "Bienvenue sur le dashboard !")

# Boutons de navigation avec actions
btn_dashboard = tk.Button(
    nav_frame, text="Accueil", bg="#34495e", fg="white", font=("Arial", 12), relief="flat",
    command=lambda: show_content(content_frame, "Vous êtes sur la page Accueil.")
)
btn_dashboard.pack(fill="x", pady=10, padx=10)

btn_commande = tk.Button(
    nav_frame, text="Commades", bg="#34495e", fg="white", font=("Arial", 12), relief="flat",
    command=lambda: show_content(content_frame, "Voici vos commandes.")
)
btn_commande.pack(fill="x", pady=10, padx=10)

btn_client = tk.Button(
    nav_frame, text="Paramètres", bg="#34495e", fg="white", font=("Arial", 12), relief="flat",
    command=lambda: show_content(content_frame, "Bienvenue dans les clients.")
)
btn_client.pack(fill="x", pady=10, padx=10)

btn_employe = tk.Button(
    nav_frame, text="Paramètres", bg="#34495e", fg="white", font=("Arial", 12), relief="flat",
    command=lambda: show_content(content_frame, "Bienvenue dans les employes.")
)
btn_employe.pack(fill="x", pady=10, padx=10)

# Lancer la boucle principale
root.mainloop()