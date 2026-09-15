import tkinter as tk
from observers.observer import Observateur

class IndicateurLivraison(Observateur):

    def __init__(self, parent):
        
        self._label = tk.Label(
            parent, 
            text=f"Livraison... gratuite?", 
            font=("Arial", 14, "bold"),
            fg="gray"
        )
        self._label(pady=5)
    
    def actualiser(self, sujet) -> None:

        donnees = sujet.get_donnees()
        
        
        self._label.config(text="Modification")
    
    
        
       
    
    