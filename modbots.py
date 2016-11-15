# -*- coding: utf-8 -*-
import modjoueurs

class Bots():
    'Des Bots'
    
    def __init__(self,laCouleur,laLocalisation):
        self.active = False
        self.couleur = laCouleur
        self.joueur = None

        print("Nouveaux Bots couleur: ",self.couleur)

    def activerBots(self,leJoueur):
        self.joueur=leJoueur
        self.active=True

botsBleus = Bots('Bleus')
botsRouges = Bots('Rouges')
