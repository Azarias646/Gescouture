import tkinter as tk
from tkinter import ttk

def test_search_functionality():
    # Fenêtre principale
    root = tk.Tk()
    root.title("Test Barre de Recherche")
    root.geometry("600x400")

    # Liste des données fictives
    data = [
        (1, "Jean Dupont", "jean.dupont@email.com", "123456789"),
        (2, "Marie Curie", "marie.curie@email.com", "987654321"),
        (3, "Albert Einstein", "albert.einstein@email.com", "555555555"),
    ]

    # Variable pour la recherche
    search_var = tk.StringVar()

    def filter_results():
        query = search_var.get().lower()
        for item in tree.get_children():
            values = tree.item(item, "values")
            if any(query in str(value).lower() for value in values):
                tree.item(item, tags=())
            else:
                tree.item(item, tags=("hidden",))
        tree.tag_configure("hidden", foreground="", background="")  # Cache les lignes masquées

    # Barre de recherche
    search_entry = tk.Entry(root, textvariable=search_var, width=30)
    search_entry.pack(pady=5)
    search_entry.bind("<KeyRelease>", lambda event: filter_results())

    # Tableau
    columns = ("ID", "Nom", "Email", "Téléphone")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nom", text="Nom")
    tree.heading("Email", text="Email")
    tree.heading("Téléphone", text="Téléphone")
    tree.pack(expand=True, fill="both", padx=10, pady=10)

    # Ajouter les données au tableau
    for row in data:
        tree.insert("", "end", values=row)

    root.mainloop()

# Tester la fonctionnalité
test_search_functionality()
