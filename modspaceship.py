# -*- coding: utf-8 -*-
class Spaceship():
    'Le spaceship lui-même'
    #structure
    # Decks de 1 a 6
    #Hit Points
    hpBlue = 6
    hpWhite = 6
    hpRed = 6
    dmgHeavyBlue = 4
    dmgHeavyWhite = 5
    dmgHeavyRed = 4
    dmgLightBlue = 2
    rngPulseWhite = 2
    dmgLightRed = 2
    shieldsCapBlue = 2
    shieldsCapWhite = 3
    shieldsCapRed = 2
    energyCapBlue = 3
    energyCapWhite = 5
    energyCapRed = 3
    #Current
    energyReservoirs = 3
    shieldsBlue = 1
    shieldsWhite = 1
    shieldsRed = 1
    energyBlue = 2
    energyWhite = 3
    energyRed = 2

    trackBlue = None
    trackRed = None
    trackWhite = None
    trackInterne = None

    def damage(self,damage,track):
        if (track is self.trackBlue):
            if (damage>=self.shieldsBlue):
                damage = damage-self.shieldsBlue
                self.shieldsBlue=0
                self.hpBlue-=damage
            else: 
                self.shieldsBlue-=damage
            print("Damage Blue",damage)
        elif (track is self.trackRed):
            if (damage>=self.shieldsRed):
                damage = damage-self.shieldsRed
                self.shieldsRed=0
                self.hpRed-=damage
            else: 
                self.shieldsRed-=damage
            print("Damage Red",damage)
        elif (track is self.trackWhite):
            print "Damage White"
            if (damage>=self.shieldsWhite):
                damage = damage-self.shieldsWhite
                self.shieldsWhite=0
                self.hpWhite-=damage
            else: 
                self.shieldsWhite-=damage
            print("Damage White",damage)
        else:
            print "Pas trouve track"

    def damage2x(self,damage,track):
        if (track is self.trackBlue):
            if (damage>=self.shieldsBlue):
                damage = damage-self.shieldsBlue
                self.shieldsBlue=0
                damage = damage*2#2x past shields
                self.hpBlue-=damage
            else: 
                self.shieldsBlue-=damage
            print("Damage Blue (x2)",damage)
        elif (track is self.trackRed):
            if (damage>=self.shieldsRed):
                damage = damage-self.shieldsRed
                self.shieldsRed=0
                damage = damage*2#2x past shields
                self.hpRed-=damage
            else: 
                self.shieldsRed-=damage
            print("Damage Red (x2)",damage)
        elif (track is self.trackWhite):
            if (damage>=self.shieldsWhite):
                damage = damage-self.shieldsWhite
                self.shieldsWhite=0
                damage = damage*2#2x past shields
                self.hpWhite-=damage
            else: 
                self.shieldsWhite-=damage
            print("Damage White (x2)",damage)
        else:
            print "Pas trouve track"

    def damageNoShields(self,damage,track):
        if (track is self.trackBlue):
            self.hpBlue-=damage
            print("Damage Blue",damage)
        elif (track is self.trackRed):
            self.hpRed-=damage
            print("Damage Red",damage)
        elif (track is self.trackWhite):
            self.hpWhite-=damage
            print("Damage White",damage)
        else:
            print "Pas trouve track"

    def drainShields(self,track):
        if (track is self.trackBlue):
            self.shieldsBlue=0
            print "Shields Drainés Blue"
        elif (track is self.trackRed):
            self.shieldsRed=0
            print "Shields Drainés Red"
        elif (track is self.trackWhite):
            self.shieldsWhite=0
            print "Shields Drainés White"

    def isDestroyed(self):
        if (self.hpBlue <1 or self.hpWhite<1 or self.hpRed<1):
            return True
        else:
            return False

print "import modspaceship"
