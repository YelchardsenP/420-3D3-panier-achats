import wx
from datetime import datetime


ARTICLES = [
    {"nom": "Clavier mécanique", "prix": 89.99},
    {"nom": "Souris sans fil",   "prix": 34.99},
    {"nom": "Écran 27 pouces",   "prix": 299.99},
    {"nom": "Webcam HD",         "prix": 49.99},
    {"nom": "Casque audio",      "prix": 79.99},
]

SEUIL_LIVRAISON = 50.0


class App(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Panier d'achat")
        self.panier = []

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Titre
        titre = wx.StaticText(panel, label="Panier d'achat")
        font = titre.GetFont()
        font.SetPointSize(16)
        font.MakeBold()
        titre.SetFont(font)
        sizer.Add(titre, 0, wx.ALL | wx.CENTER, 10)

        # Articles disponibles
        box_articles = wx.StaticBox(panel, label="Articles disponibles")
        sizer_articles = wx.StaticBoxSizer(box_articles, wx.VERTICAL)
        for article in ARTICLES:
            btn = wx.Button(
                panel,
                label=f"Ajouter {article['nom']} ({article['prix']:.2f} $)"
            )
            btn.Bind(wx.EVT_BUTTON, lambda e, a=article: self.ajouter(a))
            sizer_articles.Add(btn, 0, wx.ALL | wx.EXPAND, 2)
        sizer.Add(sizer_articles, 0, wx.ALL | wx.EXPAND, 10)

        # Panier
        box_panier = wx.StaticBox(panel, label="Mon panier")
        sizer_panier = wx.StaticBoxSizer(box_panier, wx.VERTICAL)
        self.liste_articles = wx.ListBox(panel, size=(300, 120))
        sizer_panier.Add(self.liste_articles, 0, wx.ALL | wx.EXPAND, 5)
        btn_retirer = wx.Button(panel, label="Retirer l'article sélectionné")
        btn_retirer.Bind(wx.EVT_BUTTON, self.retirer)
        sizer_panier.Add(btn_retirer, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(sizer_panier, 0, wx.ALL | wx.EXPAND, 10)

        # Total
        self.label_total = wx.StaticText(panel, label="Total : 0.00 $")
        font_total = self.label_total.GetFont()
        font_total.SetPointSize(14)
        font_total.MakeBold()
        self.label_total.SetFont(font_total)
        sizer.Add(self.label_total, 0, wx.ALL | wx.CENTER, 5)

        # Indicateur livraison
        self.label_livraison = wx.StaticText(
            panel,
            label=f"Ajoutez {SEUIL_LIVRAISON:.2f} $ pour la livraison gratuite"
        )
        sizer.Add(self.label_livraison, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(sizer)
        self.Fit()

    def ajouter(self, article):
        self.panier.append(article)
        self.actualiser()

        horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("panier.log", 'a') as f:
            f.write(
                f"{horodatage} | AJOUT : {article['nom']} — "
                f"{article['prix']:.2f} $\n"
            )

    def retirer(self, event):
        selection = self.liste_articles.GetSelection()
        if selection == wx.NOT_FOUND:
            return
        article = self.panier[selection]
        self.panier.pop(selection)
        self.actualiser()

        horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("panier.log", 'a') as f:
            f.write(
                f"{horodatage} | RETRAIT : {article['nom']} — "
                f"{article['prix']:.2f} $\n"
            )

    def actualiser(self):
        # Mettre à jour la liste
        self.liste_articles.Clear()
        for article in self.panier:
            self.liste_articles.Append(
                f"{article['nom']} — {article['prix']:.2f} $"
            )

        # Mettre à jour le total
        total = sum(a['prix'] for a in self.panier)
        self.label_total.SetLabel(f"Total : {total:.2f} $")

        # Mettre à jour l'indicateur de livraison
        if total >= SEUIL_LIVRAISON:
            self.label_livraison.SetLabel("✓ Livraison gratuite !")
            self.label_livraison.SetForegroundColour(wx.GREEN)
        else:
            manque = SEUIL_LIVRAISON - total
            self.label_livraison.SetLabel(
                f"Ajoutez {manque:.2f} $ pour la livraison gratuite"
            )
            self.label_livraison.SetForegroundColour(wx.LIGHT_GREY)

        self.label_livraison.Refresh()


if __name__ == "__main__":
    app = wx.App()
    fenetre = App()
    fenetre.Show()
    app.MainLoop()
