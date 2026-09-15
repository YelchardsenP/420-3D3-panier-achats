from models.panier import Panier
from views.dashboard import Dashboard

panier = Panier()
app = Dashboard(panier)
app.mainloop()