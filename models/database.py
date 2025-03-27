import sqlite3

def create_connection():
    connection = sqlite3.connect("couture.db")
    return connection

def create_clients_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            contact TEXT NOT NULL,
            epaule TEXT,
            poitrine TEXT,
            pince TEXT,
            long_taille TEXT,
            tour_taille TEXT,
            long_camisole TEXT,
            long_manche TEXT,
            tour_manche TEXT,
            poignet TEXT,
            ceinture TEXT,
            bassin TEXT,
            long_genou TEXT,
            long_jupe TEXT,
            long_robe TEXT,
            frappe TEXT,
            cuisse TEXT,
            long_chemise TEXT,
            long_pantalon TEXT,
            bas TEXT
        )
    """)
    connection.commit()
    connection.close()

# Exécuter la création de la table
create_clients_table()


def create_employes_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            contact TEXT NOT NULL,
            date_naissance TEXT,
            genre TEXT,
            cnib TEXT NOT NULL UNIQUE
        )
    """)
    connection.commit()
    connection.close()

# Exécuter la création de la table
create_employes_table()


def create_table_commandes():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS commandes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            modele_vetement TEXT NOT NULL,
            detail TEXT,
            qte INTEGER NOT NULL,
            date_debut DATE NOT NULL,
            date_fin DATE NOT NULL,
            montant REAL NOT NULL,
            employe_id INTEGER,
            avancement TEXT NOT NULL,
            statut TEXT NOT NULL,
            FOREIGN KEY (client_id) REFERENCES clients(id),
            FOREIGN KEY (employe_id) REFERENCES employes(id)
        )
    """)
    connection.commit()
    connection.close()

# Exécuter la création de la table
create_table_commandes()