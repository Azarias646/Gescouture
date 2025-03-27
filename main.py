import tkinter as tk
from models.dashboard import show_dashboard
from views.nav import create_nav_frame
from views.content import create_content_frame
from models.database import create_clients_table, create_employes_table, create_table_commandes


def main():
    # Créer la fenêtre principale
    root = tk.Tk()
    root.title("Coutureges")

    # Dimensions de la fenêtre
    window_width = 1200
    window_height = 600

   # Dimensions de l'écran utilisable
    screen_width = root.winfo_screenwidth()
    #screen_height = root.winfo_screenheight()

    # Calcul des coordonnées pour centrer la fenêtre
    x = (screen_width // 2) - (window_width // 2)
    y = 0  #(screen_height // 2) - (window_height // 2)

    # Positionner la fenêtre
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Appeler la fonction pour s'assurer que la table est créée
    create_clients_table()
    create_employes_table()
    create_table_commandes()

    # Cadre principal pour la navigation
    nav_frame = create_nav_frame(root)

    # Cadre principal pour le contenu
    content_frame = create_content_frame(root)

    # Afficher le Dashboard au lancement
    show_dashboard(content_frame)

    # Lancer l'application
    root.mainloop()

if __name__ == "__main__":
    main()
