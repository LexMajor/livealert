# -*- coding: utf-8 -*-
import socket, sys, os, os.path
import pygame
from pygame.locals import *
import modmenace,modtracks,modspaceship,modinterface,modjoueurs,modactions
import modcfg

def startTurn():
    # Menaces entrent
    pass

def endTurn():

    # Resoudre les actions des joueurs, dans l'ordre

    # Resoudre le dommage des actions des joueurs
    for uneMenaceBlue in spaceship.trackBlue.menaces:
        uneMenaceBlue.resolveDmg()
    for uneMenaceWhite in spaceship.trackWhite.menaces:
        uneMenaceWhite.resolveDmg()
    for uneMenaceRed in spaceship.trackRed.menaces:
        uneMenaceRed.resolveDmg()
    for uneMenaceInterne in spaceship.trackInterne.menaces:
        uneMenaceInterne.resolveDmg()
    #Reset all "has fired" values
    hrFired,hwFired,hbFired,lrFired,pcFired,lbFired = [False,False,False,False,False,False]

    #print("Track: ",spaceship.trackInterne.menaces)
    # Avancer les roquettes avant ou apr�s? 
    # Avancer toutes les menaces, et les faire executer ce qu'elles ont � ex�cuter au besoin
    for uneMenaceBlue in spaceship.trackBlue.menaces:
        uneMenaceBlue.activate(spaceship)
        uneMenaceBlue.unsetPulseHit()

    for uneMenaceWhite in spaceship.trackWhite.menaces:
        uneMenaceWhite.activate(spaceship)
        uneMenaceWhite.unsetPulseHit()

    for uneMenaceRed in spaceship.trackRed.menaces:
        uneMenaceRed.activate(spaceship)
        uneMenaceRed.unsetPulseHit()

    for uneMenaceInterne in spaceship.trackInterne.menaces:
        uneMenaceInterne.activate(spaceship)

    #status report
    print("hpRed: ",spaceship.hpRed,", hpWhite: ",spaceship.hpWhite,", hpBlue: ",spaceship.hpBlue)
    print("shieldsRed: ",spaceship.shieldsRed,", shieldsWhite: ",spaceship.shieldsWhite,", shieldsBlue: ",spaceship.shieldsBlue)
    print("energyRed: ",spaceship.energyRed,", energyWhite: ",spaceship.energyWhite,", energyBlue: ",spaceship.energyBlue)
    # Dire que tous les joueurs ont joue

# set up pygame
pygame.init()
clock = pygame.time.Clock()

# Set Events Blocks
pygame.event.set_blocked ( pygame.MOUSEMOTION )

# Turn ends
pygame.time.set_timer(USEREVENT+1,modcfg.perturn*1000)

print("Duree: ",modcfg.duration,",Tours: ",modcfg.turns,", Par tour: ",modcfg.perturn)

########### SANDBOX PLAY #################

modjoueurs.Joueur("Yellow")
#print("Joueurs",modjoueurs.joueurs)

spaceship=modspaceship.Spaceship()

modtracks.getTracks(spaceship)
print("Track Blue: T",len(spaceship.trackBlue.ticks)-9,"Track Red: T",len(spaceship.trackRed.ticks)-9,"Track White: T",len(spaceship.trackWhite.ticks)-9,"Track Interne: T",len(spaceship.trackInterne.ticks)-9)

#modmenace.newMenaceInt(spaceship.trackInterne)
modmenace.newMenaceExt(spaceship.trackRed)
modmenace.newMenaceExt(spaceship.trackWhite)
modmenace.newMenaceExt(spaceship.trackBlue)
modmenace.newMenaceExt(spaceship.trackBlue)
#modmenace.newMenaceExt(spaceship.trackRed)
#modmenace.newMenaceExt(spaceship.trackWhite)

#print(menacesBlue)
#print("hpRed: ",spaceship.hpRed,", hpWhite: ",spaceship.hpWhite,", hpBlue: ",spaceship.hpBlue)
#print("shieldsRed: ",spaceship.shieldsRed,", shieldsWhite: ",spaceship.shieldsWhite,", shieldsBlue: ",spaceship.shieldsBlue)
#print("energyRed: ",spaceship.energyRed,", shieldsWhite: ",spaceship.shieldsWhite,", energyBlue: ",spaceship.energyBlue)
#print("menace: ",uneMenace.track)
evenement = pygame.event.Event(USEREVENT, joueur='Yellow', action='A', localisation=1)
pygame.event.post(evenement)
evenement = pygame.event.Event(USEREVENT, joueur='Yellow', action='A', localisation=2)
pygame.event.post(evenement)
evenement = pygame.event.Event(USEREVENT, joueur='Yellow', action='A', localisation=3)
pygame.event.post(evenement)
evenement = pygame.event.Event(USEREVENT, joueur='Yellow', action='A', localisation=4)
pygame.event.post(evenement)
evenement = pygame.event.Event(USEREVENT, joueur='Yellow', action='A', localisation=5)
pygame.event.post(evenement)
evenement = pygame.event.Event(USEREVENT, joueur='Yellow', action='A', localisation=6)
pygame.event.post(evenement)
#evenement = pygame.event.Event(USEREVENT, joueur=1, action='B', localisation=3)
#pygame.event.post(evenement)
#evenement = pygame.event.Event(USEREVENT, joueur=2, action='C', localisation=2)
#pygame.event.post(evenement)
#evenement = pygame.event.Event(USEREVENT, joueur=2, action='C', localisation=1)
#pygame.event.post(evenement)
#evenement = pygame.event.Event(USEREVENT, joueur=2, action='C', localisation=1)
#pygame.time.set_timer(USEREVENT+1,3000)

#POC pour afficher interface
#modinterface.splashPage(modinterface.RED)
# Open Socket 
#if os.path.exists( "/tmp/socket_interface" ):
#  os.remove( "/tmp/socket_interface" )
 
#print("Opening socket...")
#server = socket.socket( socket.AF_UNIX, socket.SOCK_DGRAM )
#server.bind("/tmp/socket_interface")
#server.setblocking(False)

# run the game loop
while 1:

    if (spaceship.isDestroyed()):
        sys.exit("Vaisseau destru. Vous avez perdu.")
#    try:
#        datagram = server.recv( 1024 ) 
#        print("Commande recue: ")
#    except socket.error:
#        # Nothing to see there
#        pass

    for event in pygame.event.get():
        print("Event: ",event.type)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            print("Quitter?")
            if event.key == ord ( "q" ): 
                print("Quitter!")
                pygame.event.post ( pygame.QUIT )
        elif event.type == USEREVENT:
            print("Action: ",event.joueur,event.action,event.localisation)
            modactions.activer(event.joueur,event.action, event.localisation, spaceship)
        elif event.type == USEREVENT+1:
            endTurn()
            modcfg.currentTurn+=1
            print("Fin Tour",modcfg.currentTurn)
            if (modcfg.currentTurn>modcfg.turns):
                sys.exit("Partie Terminee")
    clock.tick(20)
