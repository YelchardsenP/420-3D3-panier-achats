from models.subject import Sujet

class Panier(Sujet):
    
    #representation de liste d'articles
    def __init__(self):
        super().__init__() #instansiation liste observateurs
        self._articles = []
    
    #ajouter un article
    # TODO: A MODIF POUR INCLURE INDE
    def ajouter(self, article) -> None:
        self._articles.append(article)
    
    #retirer un article
    # TODO: A MODIF POUR INCLURE INDEX
    def retirer(self, article) -> None:
        self._articles.remove(article)
    
    #retour dun dict avec articles
    def get_donnees(self) -> dict:
        return {"articles" : self._articles}
