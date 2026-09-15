from observers.observer import Observateur

class LoggerPanier(Observateur):

    def __init__(self, chemin_fichier: str = "panier.log"):
        pass
    
    def actualiser(self, sujet) -> None:
        pass