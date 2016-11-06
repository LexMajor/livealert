# -*- coding: utf-8 -*-

joueurs = []

def getJoueur(laCouleur):
    for unJoueur in joueurs:
        if unJoueur.couleur == laCouleur:
            return unJoueur
    print("on se rend ici?")

class Joueur():
    'Un Joueur'


    def __init__(self,laCouleur):
        self.couleur = laCouleur
        self.localisation = 2 #start bridge
        self.hasBots = False
        self.isKnockedOut = False
        self.aJoue = False

        joueurs.append(self)
        print("Nouveau Joueur couleur: ",self.couleur)

    def knocker(self):
        self.isKnockedOut = True

    def isKO(self):
        return self.isKnockedOut

    def aJoue(self):
        return self.aJoue
