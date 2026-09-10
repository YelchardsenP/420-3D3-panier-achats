import tkinter as tk
from datetime import datetime


ARTICLES = [
    {"nom": "Clavier mécanique", "prix": 89.99},
    {"nom": "Souris sans fil",   "prix": 34.99},
    {"nom": "Écran 27 pouces",   "prix": 299.99},
    {"nom": "Webcam HD",         "prix": 49.99},
    {"nom": "Casque audio",      "prix": 79.99},
]

SEUIL_LIVRAISON = 50.0


class App:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("Panier d'achat")
        self.fenetre.resizable(False, False)

        self.panier = []

        # Titre
        tk.Label(
            self.fenetre,
            text="Panier d'achat",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        # Boutons d'ajout
        frame_articles = tk.LabelFrame(
            self.fenetre, text="Articles disponibles", padx=10, pady=10
        )
        frame_articles.pack(fill=tk.X, padx=10, pady=5)

        for article in ARTICLES:
            tk.Button(
                frame_articles,
                text=f"Ajouter {article['nom']} ({article['prix']:.2f} $)",
                command=lambda a=article: self.ajouter(a)
            ).pack(fill=tk.X, pady=2)

        # Contenu du panier
        frame_panier = tk.LabelFrame(
            self.fenetre, text="Mon panier", padx=10, pady=10
        )
        frame_panier.pack(fill=tk.X, padx=10, pady=5)

        self.liste_articles = tk.Listbox(frame_panier, height=6)
        self.liste_articles.pack(fill=tk.X)

        tk.Button(
            frame_panier,
            text="Retirer l'article sélectionné",
            command=self.retirer
        ).pack(pady=5)

        # Total
        self.label_total = tk.Label(
            self.fenetre,
            text="Total : 0.00 $",
            font=("Arial", 14, "bold")
        )
        self.label_total.pack(pady=5)

        # Indicateur livraison
        self.label_livraison = tk.Label(
            self.fenetre,
            text=f"Ajoutez {SEUIL_LIVRAISON:.2f} $ pour la livraison gratuite",
            font=("Arial", 11),
            fg="gray"
        )
        self.label_livraison.pack(pady=5)

        self.fenetre.mainloop()

    def ajouter(self, article):
        self.panier.append(article)
        self.actualiser()

        # Écrire dans le log
        horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("panier.log", 'a') as f:
            f.write(f"{horodatage} | AJOUT : {article['nom']} — {article['prix']:.2f} $\n")

    def retirer(self):
        selection = self.liste_articles.curselection()
        if not selection:
            return
        index = selection[0]
        article = self.panier[index]
        self.panier.pop(index)
        self.actualiser()

        # Écrire dans le log
        horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("panier.log", 'a') as f:
            f.write(f"{horodatage} | RETRAIT : {article['nom']} — {article['prix']:.2f} $\n")

    def actualiser(self):
        # Mettre à jour la liste des articles
        self.liste_articles.delete(0, tk.END)
        for article in self.panier:
            self.liste_articles.insert(tk.END, f"{article['nom']} — {article['prix']:.2f} $")

        # Mettre à jour le total
        total = sum(a['prix'] for a in self.panier)
        self.label_total.config(text=f"Total : {total:.2f} $")

        # Mettre à jour l'indicateur de livraison
        if total >= SEUIL_LIVRAISON:
            self.label_livraison.config(
                text="✓ Livraison gratuite !",
                fg="green"
            )
        else:
            manque = SEUIL_LIVRAISON - total
            self.label_livraison.config(
                text=f"Ajoutez {manque:.2f} $ pour la livraison gratuite",
                fg="gray"
            )


if __name__ == "__main__":
    app = App()
