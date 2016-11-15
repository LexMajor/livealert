# -*- coding: utf-8 -*-
#import socket, sys, os, os.path
#import modmenace,modtracks,modspaceship,modinterface,modjoueurs
import modjoueurs,modmenace
#import modcfg

### VARIABLES RELATIVES AUX ACTIONS DU TOUR COURANT ###

def activer(leJoueur,lAction,laLocalisation, leSC):
    objJoueur = modjoueurs.getJoueur(leJoueur)
    #print("Action fct:  ",objJoueur,lAction,laLocalisation)

    if (lAction=='A'):
        if (laLocalisation==1):
            if (not leSC.hrFired and leSC.energyRed>0):
                leSC.energyRed-=1
                print("Fire Heavy Cannon Red")
                curPos = -1 
                curTarget = None

                # Find Best target
                for menaceRed in leSC.trackRed.menaces:
                    #print("Eval Menace",menaceRed)
                    if (menaceRed.track is leSC.trackRed):
                        #print("Menace Red Detected")
                        if (menaceRed.position > curPos and menaceRed.isTargetable()):
                            print("Menace Red Targeted")
                            curTarget = menaceRed
                            curPos = menaceRed.position

                if (curTarget): 
                    curTarget.assignDmg(leSC.dmgHeavyRed)
                    leSC.hrFired = True
                print("Menace Red Damage Assigned")
            else:
                print("No Energy for Red Cannon or already fired")
                
        elif (laLocalisation==2):
            if (not leSC.hwFired and leSC.energyWhite>0):
                leSC.energyWhite-=1
                print("Fire Heavy Cannon White")
                curPos = -1 
                curTarget = None

                # Find Best target
                for menaceWhite in leSC.trackWhite.menaces:
                    #print("Eval Menace",menaceWhite)
                    if (menaceWhite.track is leSC.trackWhite):
                        #print("Menace White Detected")
                        if (menaceWhite.position > curPos and menaceWhite.isTargetable()):
                            print("Menace White Targeted")
                            curTarget = menaceWhite
                            curPos = menaceWhite.position

                if (curTarget): 
                    curTarget.assignDmg(leSC.dmgHeavyWhite)
                    leSC.hwFired = True
                    print("Menace White Damage Assigned")
            else:
                print("No Energy for White Cannon or already fired")

        elif (laLocalisation==3):
            if (not leSC.hbFired and leSC.energyBlue>0):
                leSC.energyBlue-=1
                print("Fire Heavy Cannon Blue")
                curPos = -1 
                curTarget = None

                # Find Best target
                for menaceBlue in leSC.trackBlue.menaces:
                    #print("Eval Menace",menaceBlue)
                    if (menaceBlue.track is leSC.trackBlue):
                        #print("Menace Blue Detected")
                        if (menaceBlue.position > curPos and menaceBlue.isTargetable()):
                            print("Menace Blue Targeted")
                            curTarget = menaceBlue
                            curPos = menaceBlue.position

                if (curTarget): 
                    curTarget.assignDmg(leSC.dmgHeavyBlue)
                    leSC.hbFired = True
                    print("Menace Blue Damage Assigned")
            else:
                print("No Energy for Blue Cannon or already fired")

        elif (laLocalisation==4):
            # Light Red, no energy, fire once 
            if (not leSC.lrFired):
                print("Fire Light Red Cannon")
                curPos = -1 
                curTarget = None

                # Find Best target
                for menaceRed in leSC.trackRed.menaces:
                    #print("Eval Menace",menaceRed)
                    if (menaceRed.track is leSC.trackRed):
                        #print("Menace Red Detected")
                        if (menaceRed.position > curPos and menaceRed.isTargetable()):
                            print("Menace Red Targeted")
                            curTarget = menaceRed
                            curPos = menaceRed.position

                if (curTarget): 
                    curTarget.assignDmg(leSC.dmgLightRed)
                    leSC.lrFired = True
                    print("Menace Red Damage Assigned")
            else:
                print("Light Red already fired")

        elif (laLocalisation==5):
            # Pulse, Energy, check Range
            if (not leSC.pcFired and leSC.energyWhite>0):
                leSC.energyWhite-=1
                print("Fire Pulse Cannon")

                # Find Red targets
                for menaceRed in leSC.trackRed.menaces:
                    #print("Eval Menace",menaceRed)
                    if (menaceRed.track is leSC.trackRed):
                        #print("Menace Red Detected")
                        if (leSC.trackRed.ticks[menaceRed.position]['rng']<=leSC.rngPulseCannon and menaceRed.isTargetable()):
                            print("Menace Red Targeted")
                            menaceRed.assignDmg(leSC.dmgPulseCannon)
                            menaceRed.isHitByPulse()
                            leSC.pcFired = True
                            print("Menace Red Damage Assigned")

                # Find White targets
                for menaceWhite in leSC.trackWhite.menaces:
                    #print("Eval Menace",menaceWhite)
                    if (menaceWhite.track is leSC.trackWhite):
                        #print("Menace White Detected")
                        if (leSC.trackWhite.ticks[menaceWhite.position]['rng']<=leSC.rngPulseCannon and menaceWhite.isTargetable()):
                            print("Menace White Targeted")
                            menaceWhite.assignDmg(leSC.dmgPulseCannon)
                            menaceWhite.isHitByPulse()
                            leSC.pcFired = True
                            print("Menace White Damage Assigned")

                # Find Blue targets
                for menaceBlue in leSC.trackBlue.menaces:
                    #print("Eval Menace",menaceBlue)
                    if (menaceBlue.track is leSC.trackBlue):
                        #print("Menace Blue Detected")
                        if (leSC.trackBlue.ticks[menaceBlue.position]['rng']<=leSC.rngPulseCannon and menaceBlue.isTargetable()):
                            print("Menace Blue Targeted")
                            menaceBlue.assignDmg(leSC.dmgPulseCannon)
                            menaceBlue.isHitByPulse()
                            leSC.pcFired = True
                            print("Menace Blue Damage Assigned")
            else:
                print("No Energy for Pulse Cannon or already fired")
            pass

        elif (laLocalisation==6):
            # Light Blue, no energy, fire once 
            if (not leSC.lbFired):
                print("Fire Light Blue Cannon")
                curPos = -1 
                curTarget = None

                # Find Best target
                for menaceBlue in leSC.trackBlue.menaces:
                    #print("Eval Menace",menaceBlue)
                    if (menaceBlue.track is leSC.trackBlue):
                        #print("Menace Blue Detected")
                        if (menaceBlue.position > curPos and menaceBlue.isTargetable()):
                            print("Menace Blue Targeted")
                            curTarget = menaceBlue
                            curPos = menaceBlue.position

                if (curTarget): 
                    curTarget.assignDmg(leSC.dmgLightBlue)
                    leSC.lbFired = True
                    print("Menace Blue Damage Assigned")
            else:
                print("Light Blue already fired")

    elif (lAction=='B'):

        for menaceInterne in leSC.trackInterne.menaces:
            if (menaceInterne.actionDmg == 'B'):
                if(laLocalisation==menaceInterne.localisation):
                    # A la meme place
                    menaceInterne.actionI()
                    # On ne veut faire qu'une seule menace
                    break


        if (laLocalisation==1):
            print("Recharge Shields Red")
            while (leSC.energyRed>0 and leSC.shieldsRed<leSC.shieldsCapRed):
                leSC.energyRed-=1
                leSC.shieldsRed+=1
        elif (laLocalisation==2):
            print("Recharge Shields White")
            while (leSC.energyWhite>0 and leSC.shieldsWhite<leSC.shieldsCapWhite):
                leSC.energyWhite-=1
                leSC.shieldsWhite+=1
        elif (laLocalisation==3):
            print("Recharge Shields Blue")
            while (leSC.energyBlue>0 and leSC.shieldsBlue<leSC.shieldsCapBlue):
                leSC.energyBlue-=1
                leSC.shieldsBlue+=1
        elif (laLocalisation==4):
            print("Recharge Reactor Red")
            while (leSC.energyWhite>0 and leSC.energyRed<leSC.energyCapRed):
                leSC.energyWhite-=1
                leSC.energyRed+1
        elif (laLocalisation==5):
            print("Recharge White Central Reactor")
            if (leSC.energyReservoirs>0):
                leSC.energyReservoirs-=1
                leSC.energyWhite=leSC.energyCapWhite #5
        elif (laLocalisation==6):
            print("Recharge Reactor Blue")
            while (leSC.energyWhite>0 and leSC.energyBlue<leSC.energyCapBlue):
                leSC.energyWhite-=1
                leSC.energyBlue+=1

    elif (lAction=='C'):
        for menaceInterne in leSC.trackInterne.menaces:
            if (menaceInterne.actionDmg == 'C'):
                if(laLocalisation==menaceInterne.localisation):
                    # A la meme place
                    menaceInterne.actionI()
                    # On ne veut faire qu'une seule menace
                    break

        if (laLocalisation==1):
            # Partir dans l'espace
            pass
        elif (laLocalisation==2):
            # Brasser la souris
            pass
        elif (laLocalisation==3):
            # Battlebots Bleus
            pass
        elif (laLocalisation==4):
            # Battlebots Rouges
            pass
        elif (laLocalisation==5):
            # Regarder dehors
            print("C'est Beau...")
        elif (laLocalisation==6):
            # Rockets
            pass

    elif (lAction=='R'): # Robots a partir d'un module telecommande?
        for menaceInterne in leSC.trackInterne.menaces:
            if (menaceInterne.actionDmg == 'R'):
                if(laLocalisation==menaceInterne.localisation):
                    # A la meme place
                    menaceInterne.actionI()
                    # On ne veut faire qu'une seule menace
                    break

        if (laLocalisation==7):
            # Dans l'espace avec les robots!
            pass

print "import modaction complété"
