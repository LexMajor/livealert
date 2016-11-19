# -*- coding: utf-8 -*-
#import modjoueurs

class Bots():
    'Des Bots'
    
    def __init__(self,laCouleur):
        self.active = False
        self.couleur = laCouleur
        self.joueur = None

        print("Nouveaux Bots couleur: ",self.couleur)

    def assignerBots(self,leJoueur):
        self.joueur=leJoueur
        leJoueur.bots=self
        self.active=True

botsBleus = Bots('Bleus')
botsRouges = Bots('Rouges')
