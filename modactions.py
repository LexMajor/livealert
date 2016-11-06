# -*- coding: utf-8 -*-
#import socket, sys, os, os.path
#import modmenace,modtracks,modspaceship,modinterface,modjoueurs
import modjoueurs
#import modcfg

### VARIABLES RELATIVES AUX ACTIONS DU TOUR COURANT ###

damageOnRed=0
damageOnWhite=0
damageOnBlue=0

def activer(leJoueur,lAction,laLocalisation, leSC):
    objJoueur = modjoueurs.getJoueur(leJoueur)
    print("Action fct:  ",objJoueur,lAction,laLocalisation)

    if (lAction=='A'):
        if (laLocalisation==1):
            pass
        elif (laLocalisation==2):
            pass
        elif (laLocalisation==3):
            pass
        elif (laLocalisation==4):
            pass
        elif (laLocalisation==5):
            pass
        elif (laLocalisation==6):
            pass
    elif (lAction=='B'):
        if (laLocalisation==1):
            while (leSC.energyRed>0 and leSC.shieldsRed<leSC.shieldsCapRed):
                leSC.energyRed-=1
                leSC.shieldsRed+=1
        elif (laLocalisation==2):
            while (leSC.energyWhite>0 and leSC.shieldsWhite<leSC.shieldsCapWhite):
                leSC.energyWhite-=1
                leSC.shieldsWhite+=1
        elif (laLocalisation==3):
            while (leSC.energyBlue>0 and leSC.shieldsBlue<leSC.shieldsCapBlue):
                leSC.energyBlue-=1
                leSC.shieldsBlue+=1
        elif (laLocalisation==4):
            while (leSC.energyWhite>0 and leSC.energyRed<leSC.energyCapRed):
                leSC.energyWhite-=1
                leSC.energyRed+=1
        elif (laLocalisation==5):
            if (leSC.energyReservoirs>0):
                leSC.energyReservoirs-=1
                leSC.energyWhite=leSC.energyCapWhite #5
        elif (laLocalisation==6):
            while (leSC.energyWhite>0 and leSC.energyBlue<leSC.energyCapBlue):
                leSC.energyWhite-=1
                leSC.energyBlue+=1
    elif (lAction=='C'):
        if (laLocalisation==1):
            pass
        elif (laLocalisation==2):
            pass
        elif (laLocalisation==3):
            pass
        elif (laLocalisation==4):
            pass
        elif (laLocalisation==5):
            pass
        elif (laLocalisation==6):
            pass
    elif (lAction=='R'): # Robots a partir d'un module telecommande?
        if (laLocalisation==1):
            pass
        elif (laLocalisation==2):
            pass
        elif (laLocalisation==3):
            pass
        elif (laLocalisation==4):
            pass
        elif (laLocalisation==5):
            pass
        elif (laLocalisation==6):
            pass


print "import modaction complété"
