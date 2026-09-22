import tkinter as tk
from models.panier import Panier
from observers.affichage_articles import AffichageArticles
from observers.affichage_total import AffichageTotal
from observers.indicateur_livraison import IndicateurLivraison 
from observers.logger_panier import LoggerPanier

class Dashboard(tk.Tk):

    def __init__(self, panier : Panier):
        super().__init__()
        self.title("Panier d'achats")
        self.resizable(False,False)

        self._panier = panier

        self._creer_observateurs()
        self._abonner_observateurs()
        self._creer_boutons()
    
    def _creer_observateurs(self) -> None:
        
        self._articles = AffichageArticles(self)
        self._total = AffichageTotal(self)
        self._livraison = IndicateurLivraison(self)
        self._logger = LoggerPanier(self)

    def _abonner_observateurs(self) -> None:
        
        self._panier.abonner(self._articles)
        self._panier.abonner(self._total)
        self._panier.abonner(self._livraison)
        self._panier.abonner(self._logger)

    def _creer_boutons(self) -> None:
        frame = tk.Frame(self)
        frame.pack(pady=10)

        self._label = tk.Label(self, text="yo ma boii")
        self._label.pack(pady=5)

    

        
    