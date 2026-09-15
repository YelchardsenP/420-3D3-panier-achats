import tkinter as tk
from models.panier import Panier
from observers.affichage_articles import AffichageArticle
from observers.affichage_total import AffichageTotal
from observers.indicateur_livraison import IndicateurLivraison 
from observers.logger_panier import LoggerPanier

class Dashboard(tk.Tk):

    def __init__(self):
        super().__init()
        self.title("Panier d'achats")
        self.resizable(False,False)

        self._creer_observateurs()
        self._abonner_observateurs()
        self._creer_boutons()
    
    def _creer_observateurs(self) -> None:
        pass

    def _abonner_observateurs(self) -> None:
        pass

    def _creer_boutons(self) -> None:
        pass

    

        
    