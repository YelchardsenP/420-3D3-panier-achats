from models.subject import Sujet

class Panier(Sujet):
    
    #representation de liste d'articles
    def __init__(self):
        super().__init__() #instansiation liste observateurs
        self._liste_articles = []
    
    #ajouter un article
    def ajouter(self, article) -> None:
        pass
    
    #retirer un article
    def retirer(self, index) -> None:
        pass
    
    #recevoir les donnees
    def get_donnees(self) -> dict:
        pass 
