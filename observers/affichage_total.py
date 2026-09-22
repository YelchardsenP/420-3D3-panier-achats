import tkinter as tk
from observers.observer import Observateur

class AffichageTotal(Observateur):
    
    def __init__(self, parent):
        
        self._label = tk.Label(
            parent, 
            text=f"Total : 0,00$", 
            font=("Arial", 14, "bold"),
            fg="gray"
        )
        self._label.pack(pady=5)
    
    def actualiser(self, sujet) -> None:

        liste_articles = sujet.get_donnees()["articles"]

        # Mettre à jour le total
        total = sum(a['prix'] for a in self.panier)
        self._label.config(text=f"Total : {total:2f}$")