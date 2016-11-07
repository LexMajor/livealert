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
    # Avancer les roquettes avant ou après? 
    # Avancer toutes les menaces, et les faire executer ce qu'elles ont à exécuter au besoin
    for uneMenaceBlue in spaceship.trackBlue.menaces:
        uneMenaceBlue.activate(spaceship)

    for uneMenaceWhite in spaceship.trackWhite.menaces:
        uneMenaceWhite.activate(spaceship)

    for uneMenaceRed in spaceship.trackRed.menaces:
        uneMenaceRed.activate(spaceship)

    for uneMenaceInterne in spaceship.trackInterne.menaces:
        uneMenaceInterne.activate(spaceship)

    #status report
    print("hpRed: ",spaceship.hpRed,", hpWhite: ",spaceship.hpWhite,", hpBlue: ",spaceship.hpBlue)
    print("shieldsRed: ",spaceship.shieldsRed,", shieldsWhite: ",spaceship.shieldsWhite,", shieldsBlue: ",spaceship.shieldsBlue)
    print("energyRed: ",spaceship.energyRed,", energyWhite: ",spaceship.energyWhite,", energyBlue: ",spaceship.energyBlue)
    # Dire que tous les joueurs ont joue


########### SANDBOX PLAY #################

modjoueurs.Joueur("Yellow")
#print("Joueurs",modjoueurs.joueurs)

spaceship=modspaceship.Spaceship()

modtracks.getTracks(spaceship)
print("Track Blue: T",len(spaceship.trackBlue.ticks)-9,"Track Red: T",len(spaceship.trackRed.ticks)-9,"Track White: T",len(spaceship.trackWhite.ticks)-9,"Track Interne: T",len(spaceship.trackInterne.ticks)-9)

#modmenace.newMenaceInt(spaceship.trackInterne)
modmenace.newMenaceExt(spaceship.trackRed)
#modmenace.newMenaceExt(spaceship.trackWhite)
#modmenace.newMenaceExt(spaceship.trackBlue)
#modmenace.newMenaceExt(spaceship.trackRed)
#modmenace.newMenaceExt(spaceship.trackWhite)

#print(menacesBlue)
#print("hpRed: ",spaceship.hpRed,", hpWhite: ",spaceship.hpWhite,", hpBlue: ",spaceship.hpBlue)
#print("shieldsRed: ",spaceship.shieldsRed,", shieldsWhite: ",spaceship.shieldsWhite,", shieldsBlue: ",spaceship.shieldsBlue)
#print("energyRed: ",spaceship.energyRed,", shieldsWhite: ",spaceship.shieldsWhite,", energyBlue: ",spaceship.energyBlue)
#print("menace: ",uneMenace.track)
#evenement = pygame.event.Event(USEREVENT, joueur='Yellow', action='A', localisation=1)
#pygame.event.post(evenement)
#evenement = pygame.event.Event(USEREVENT, joueur='Yellow', action='A', localisation=2)
#pygame.event.post(evenement)
#evenement = pygame.event.Event(USEREVENT, joueur='Yellow', action='A', localisation=3)
#pygame.event.post(evenement)
#evenement = pygame.event.Event(USEREVENT, joueur='Yellow', action='A', localisation=4)
#pygame.event.post(evenement)
#evenement = pygame.event.Event(USEREVENT, joueur='Yellow', action='A', localisation=5)
#pygame.event.post(evenement)
#evenement = pygame.event.Event(USEREVENT, joueur='Yellow', action='A', localisation=6)
#pygame.event.post(evenement)
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

# set up pygame
pygame.init()
clock = pygame.time.Clock()

# Set Events Blocks
pygame.event.set_blocked ( pygame.MOUSEMOTION )

# Turn ends
pygame.time.set_timer(USEREVENT+1,modcfg.perturn*1000)

print("Duree: ",modcfg.duration,",Tours: ",modcfg.turns,", Par tour: ",modcfg.perturn)

# For setup actions
actionID = 0


print("Debut Tour",modcfg.currentTurn)
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
        #print("Event: ",event.type)
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
            print("Fin Tour",modcfg.currentTurn)
            endTurn()
            modcfg.currentTurn+=1
            if (modcfg.currentTurn>modcfg.turns):
                sys.exit("Partie Terminee")
    clock.tick(20)
    ticks = pygame.time.get_ticks()
    #print("Ticks Init: ",ticks)

    if (ticks>2500 and actionID<=0):
        actionID+=1
        print("A1")
        #modmenace.newMenaceExt(spaceship.trackRed)
        evenement = pygame.event.Event(USEREVENT, joueur='Yellow', action='A', localisation=1)
        pygame.event.post(evenement)
        evenement = pygame.event.Event(USEREVENT, joueur='Yellow', action='A', localisation=4)
        pygame.event.post(evenement)
    elif (ticks>5500 and actionID<=1):
        actionID+=1
        print("A2")
        evenement = pygame.event.Event(USEREVENT, joueur='Yellow', action='A', localisation=2)
        pygame.event.post(evenement)
        evenement = pygame.event.Event(USEREVENT, joueur='Yellow', action='A', localisation=5)
        pygame.event.post(evenement)
        #modmenace.newMenaceExt(spaceship.trackBlue)
    elif (ticks>8500 and actionID<=2):
        actionID+=1
        print("A3")
        evenement = pygame.event.Event(USEREVENT, joueur='Yellow', action='A', localisation=3)
        pygame.event.post(evenement)
        evenement = pygame.event.Event(USEREVENT, joueur='Yellow', action='A', localisation=6)
        pygame.event.post(evenement)
        #modmenace.newMenaceExt(spaceship.trackBlue)
    elif (ticks>11500 and actionID<=3):
        actionID+=1
        print("A4")
        #modmenace.newMenaceExt(spaceship.trackBlue)
    elif (ticks>14500 and actionID<=4):
        actionID+=1
        print("A5")
        #modmenace.newMenaceExt(spaceship.trackBlue)
    elif (ticks>17500 and actionID<=5):
        actionID+=1
        print("A6")
        #modmenace.newMenaceExt(spaceship.trackBlue)
    elif (ticks>20500 and actionID<=6):
        actionID+=1
        print("A7")
        #modmenace.newMenaceExt(spaceship.trackBlue)
    elif (ticks>23500 and actionID<=7):
        actionID+=1
        print("A8")
        #modmenace.newMenaceExt(spaceship.trackBlue)
    elif (ticks>26500 and actionID<=8):
        actionID+=1
        print("A9")
        #modmenace.newMenaceExt(spaceship.trackBlue)
    elif (ticks>29500 and actionID<=9):
        actionID+=1
        print("A10")
        #modmenace.newMenaceExt(spaceship.trackBlue)
    elif (ticks>32500 and actionID<=10):
        actionID+=1
        print("A11")
        #modmenace.newMenaceExt(spaceship.trackBlue)
    elif (ticks>35500 and actionID<=11):
        actionID+=1
        print("A12")
        #modmenace.newMenaceExt(spaceship.trackBlue)









