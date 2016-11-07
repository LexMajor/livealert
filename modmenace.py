# -*- coding: utf-8 -*-
import modtracks
import modspaceship
import random

class Menace():
    'Les menaces qui peuvent survenir'

    speed = None 
    hitpoints = None  
    position = None
    track = None
    currentDmg = 0

    def activate(self,spaceship):
        start = self.position+1
        end  = self.position+self.speed+1
        self.position+=self.speed
        #print("Activation range: ",start,end)
        for i in range(start,end):
            if (self.track.ticks[i]['hit']=='X'): 
                self.executerX(spaceship)
            elif (self.track.ticks[i]['hit']=='Y'): 
                self.executerY(spaceship)
            elif (self.track.ticks[i]['hit']=='Z'): 
                self.executerZ(spaceship)
                self.destroy()
                break #On ne va pas plus loin sur la track

    def executerX(self):
        print("Exec X Menaces")
    
    def executerY(self):
        print("Exec Y Menaces")

    def executerZ(self):
        print("Exec Z Menaces")

    def assignDmg(self,leDmg):
        self.currentDmg+=leDmg
        
    def assignerTrack(self,trackAssignee):
        self.track = trackAssignee

    def destroy(self):
        self.track.menaces.remove(self)
        print("Menace Detruite")

    def isHitByPulse(self):
        #Dummy
        pass

    def unsetPulseHit(self):
        #Dummy
        pass

####################################################################################
#################     MENACES EXTERNES        ######################################
####################################################################################

class MenaceExterne(Menace):
    'Coquille pour fonctions Externes'

    def isTargetable(self):
        return True

    def resolveDmg(self):
        if (self.currentDmg>self.shields):
            damage = (self.currentDmg-self.shields)
            self.hitpoints-=damage
            print("Damage Menace",damage)

        self.currentDmg=0 # Reset

        if (self.hitpoints<1):
            self.destroy()

    def damage(self,damage):
        if (damage>=self.shields):
            damage = damage-self.shields
            self.hitpoints-=damage
            print("Damage Menace",damage)

        if (self.hitpoints<1):
            self.destroy()

class PulseBall(MenaceExterne):
    'Une balle de pulsations'

    def __init__(self):
        self.speed = 2 
        self.shields = 1 
        self.hitpoints = 5
        self.position = 0
        print("Nouvelle PulseBall!")

    def executerX(self,spaceship):
        spaceship.damage(1,spaceship.trackBlue)
        spaceship.damage(1,spaceship.trackRed)
        spaceship.damage(1,spaceship.trackWhite)
        print("Exec Pulse X: Blue, Red & White!")

    def executerY(self,spaceship):
        spaceship.damage(1,spaceship.trackBlue)
        spaceship.damage(1,spaceship.trackRed)
        spaceship.damage(1,spaceship.trackWhite)
        print("Exec Pulse Y: Blue, Red & White!")

    def executerZ(self,spaceship):
        spaceship.damage(2,spaceship.trackBlue)
        spaceship.damage(2,spaceship.trackRed)
        spaceship.damage(2,spaceship.trackWhite)
        print("Exec Pulse Z: Blue, Red & White!")

class Destroyer(MenaceExterne):
    'Un vaisseau mean'

    def __init__(self):
        self.speed = 2 
        self.shields = 2 
        self.hitpoints = 5
        self.position = 0
        print("Nouveau Destroyer!")

    def executerX(self,spaceship):
        spaceship.damage2x(1,self.track)
        print("Hit Destroyer X")

    def executerY(self,spaceship):
        spaceship.damage2x(2,self.track)
        print("Hit Destroyer Y")

    def executerZ(self,spaceship):
        spaceship.damage2x(2,self.track)
        print("Hit Destroyer Z")

class StealthFighter(MenaceExterne):
    'Un vaisseau subtil'

    def __init__(self):
        self.speed = 3 
        self.shields = 2 
        self.hitpoints = 4
        self.position = 0
        self.visible = False
        print("Nouveau Stealth Fighter!")

    def executerX(self,spaceship):
        self.visible = True
        print("Exec X Stealth Fighter")

    def executerY(self,spaceship):
        spaceship.damage(2,self.track)
        print("Exec Y Stealth Fighter")

    def executerZ(self,spaceship):
        spaceship.damage(2,self.track)
        print("Exec Z Stealth Fighter")

    def isTargetable(self):
        if (self.visible):
            print("Stealth Fighter Visible")
            return True
        else:
            print("Stealth Fighter is Stealthy")
            return False
            

class EnergyCloud(MenaceExterne):
    'Une menace dans le Cloud '

    def __init__(self):
        self.speed = 2 
        self.shields = 3 
        self.hitpoints = 5
        self.position = 0
        self.pulseCannonTurn = False 
        print("Nouveau Energy Cloud!")

    def executerX(self,spaceship):
        # Drains All Shields
        spaceship.drainShields(spaceship.trackBlue)
        spaceship.drainShields(spaceship.trackRed)
        spaceship.drainShields(spaceship.trackWhite)

        print("Exec X Energy Cloud")

    def executerY(self,spaceship):
        # Attack 1 sur les 2 autres zones
        if (self.track is spaceship.trackBlue):
            spaceship.damage(1,spaceship.trackRed)
            spaceship.damage(1,spaceship.trackWhite)
        elif (self.track is spaceship.trackRed):
            spaceship.damage(1,spaceship.trackBlue)
            spaceship.damage(1,spaceship.trackWhite)
        elif (self.track is spaceship.trackWhite):
            spaceship.damage(1,spaceship.trackBlue)
            spaceship.damage(1,spaceship.trackRed)
        print("Exec Y Energy Cloud")

    def executerZ(self,spaceship):
        # Attack 2 sur les 2 autres zones
        if (self.track is spaceship.trackBlue):
            spaceship.damage(2,spaceship.trackRed)
            spaceship.damage(2,spaceship.trackWhite)
        elif (self.track is spaceship.trackRed):
            spaceship.damage(2,spaceship.trackBlue)
            spaceship.damage(2,spaceship.trackWhite)
        elif (self.track is spaceship.trackWhite):
            spaceship.damage(2,spaceship.trackBlue)
            spaceship.damage(2,spaceship.trackRed)
        print("Exec Z Energy Cloud")

    def isHitByPulse(self):
        self.pulseCannonTurn = True 

    def resolveDmg(self):
        if (self.pulseCannonTurn):
            self.shields=0
        if (self.currentDmg>self.shields):
            damage = (self.currentDmg-self.shields)
            self.hitpoints-=damage
            print("Damage Menace",damage)

        self.currentDmg=0 # Reset
        self.shields=3
        self.pulseCannonTurn = False 

        if (self.hitpoints<1):
            self.destroy()

class Fighter(MenaceExterne):
    'Un Fighter ben normal'

    def __init__(self):
        self.speed = 3 
        self.shields = 2 
        self.hitpoints = 4
        self.position = 0
        print("Nouveau Fighter!")

    def executerX(self,spaceship):
        spaceship.damage(1,self.track)
        print("Exec X Fighter")

    def executerY(self,spaceship):
        spaceship.damage(2,self.track)
        print("Exec Y Fighter")

    def executerZ(self,spaceship):
        spaceship.damage(3,self.track)
        print("Exec Z Fighter")

####################################################################################
#################     MENACES INTERNES        ######################################
####################################################################################

class MenaceInterne(Menace):
    'Coquille pour fonctions de dommage'

    actionDmg=None


    # Never any shields
    def resolveDmg(self):
        damage = self.currentDmg
        self.hitpoints-=damage
        print("Damage Menace Interne ",damage)

        self.currentDmg = 0

        if (self.hitpoints<1):
            self.destroy()

class SkirmishersR(MenaceInterne):
    'Des abordeurs dans le Rouge'
    
    def __init__(self):
        self.speed = 3 
        self.hitpoints = 1
        self.position = 0
        self.localisation = 1 #RF
        self.fight =True
        self.fightback =True
        self.actionDmg='B'
        print("Nouveau SkirmshersR!")

    def executerX(self,spaceship):
        self.localisation+=1 # Move Right to WF
        print("Exec X SkirmishersR")

    def executerY(self,spaceship):
        self.localisation+=3 # Get Down to WA
        print("Exec Y SkirmishersR")

    def executerZ(self,spaceship):
        spaceship.damageNoShields(3,spaceship.trackWhite)
        print("Exec Z SkirmishersR")

class SkirmishersB(MenaceInterne):
    'Des abordeurs dans le Rouge'
    
    def __init__(self):
        self.speed = 3 
        self.hitpoints = 1
        self.position = 0
        self.localisation = 1 #RF
        self.fight =True
        self.fightback =True
        self.actionDmg='B'
        print("Nouveau SkirmshersB!")

    def executerX(self,spaceship):
        self.localisation-=1 # Move Left to WF
        print("Exec X SkirmishersB")

    def executerY(self,spaceship):
        self.localisation+=3 # Get Down to WA
        print("Exec Y SkirmishersB")

    def executerZ(self,spaceship):
        spaceship.damageNoShields(3,spaceship.trackWhite)
        print("Exec Z SkirmishersB")


def newMenaceExt(laTrack):
    nouvelleMenace = menacesExt.pop()
    laTrack.menaces.append(nouvelleMenace)
    nouvelleMenace.assignerTrack(laTrack)
    print("Menace: ",nouvelleMenace," Assignée à ",laTrack)

def newMenaceInt(laTrack):
    nouvelleMenace = menacesInt.pop()
    laTrack.menaces.append(nouvelleMenace)
    nouvelleMenace.assignerTrack(laTrack)
    print("Menace: ",nouvelleMenace," Interne")

menacesExt=[] 
menacesInt=[] 

#menacesExt.append(PulseBall())
#menacesExt.append(Destroyer())
#menacesExt.append(StealthFighter())
#menacesExt.append(EnergyCloud())
menacesExt.append(Fighter())
menacesExt.append(Fighter())
menacesExt.append(Fighter())
menacesExt.append(Fighter())

menacesInt.append(SkirmishersR())
menacesInt.append(SkirmishersB())

random.shuffle(menacesExt)
random.shuffle(menacesInt)

print("Import Mod Menaces")
