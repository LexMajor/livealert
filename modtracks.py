# -*- coding: utf-8 -*-
import random

class Track():

    def isX(self,position):
        if (self.ticks[position]['hit']=='X'):
            return True
        else:
            return False
    def isY(self,position):
        if (self.ticks[position]['hit']=='Y'):
            return True
        else:
            return False
    def isZ(self,position):
        if (self.ticks[position]['hit']=='Z'):
            return True
        else:
            return False

class T1(Track):
    name = None
    menaces = []
    ticks =[
        {'pos':0,'rng':2,'hit':None},
        {'pos':1,'rng':2,'hit':None},
        {'pos':2,'rng':2,'hit':None},
        {'pos':3,'rng':2,'hit':None},
        {'pos':4,'rng':2,'hit':None},
        {'pos':5,'rng':1,'hit':'X'},
        {'pos':6,'rng':1,'hit':None},
        {'pos':7,'rng':1,'hit':None},
        {'pos':8,'rng':1,'hit':None},
        {'pos':9,'rng':1,'hit':'Z'}
    ]

class T2(Track):
    name = None
    menaces = []
    ticks =[
        {'pos':0,'rng':3,'hit':None},
        {'pos':1,'rng':2,'hit':None},
        {'pos':2,'rng':2,'hit':None},
        {'pos':3,'rng':2,'hit':'X'},
        {'pos':4,'rng':2,'hit':None},
        {'pos':5,'rng':2,'hit':None},
        {'pos':6,'rng':1,'hit':None},
        {'pos':7,'rng':1,'hit':None},
        {'pos':8,'rng':1,'hit':None},
        {'pos':9,'rng':1,'hit':None},
        {'pos':10,'rng':1,'hit':'Z'}
    ]

class T3(Track):
    name = None
    menaces = []
    ticks =[
        {'pos':0,'rng':3,'hit':None},
        {'pos':1,'rng':3,'hit':None},
        {'pos':2,'rng':2,'hit':None},
        {'pos':3,'rng':2,'hit':None},
        {'pos':4,'rng':2,'hit':'X'},
        {'pos':5,'rng':2,'hit':None},
        {'pos':6,'rng':2,'hit':None},
        {'pos':7,'rng':1,'hit':None},
        {'pos':8,'rng':1,'hit':None},
        {'pos':9,'rng':1,'hit':'Y'},
        {'pos':10,'rng':1,'hit':None},
        {'pos':11,'rng':1,'hit':'Z'}
    ]

class T4(Track):
    name = None
    menaces = []
    ticks =[
        {'pos':0,'rng':3,'hit':None},
        {'pos':1,'rng':3,'hit':None},
        {'pos':2,'rng':3,'hit':None},
        {'pos':3,'rng':2,'hit':None},
        {'pos':4,'rng':2,'hit':'X'},
        {'pos':5,'rng':2,'hit':None},
        {'pos':6,'rng':2,'hit':None},
        {'pos':7,'rng':2,'hit':None},
        {'pos':8,'rng':1,'hit':'Y'},
        {'pos':9,'rng':1,'hit':None},
        {'pos':10,'rng':1,'hit':None},
        {'pos':11,'rng':1,'hit':None},
        {'pos':12,'rng':1,'hit':'Z'}
    ]

class T5(Track):
    name = None
    menaces = []
    ticks =[
        {'pos':0,'rng':3,'hit':None},
        {'pos':1,'rng':3,'hit':None},
        {'pos':2,'rng':3,'hit':None},
        {'pos':3,'rng':3,'hit':'X'},
        {'pos':4,'rng':2,'hit':None},
        {'pos':5,'rng':2,'hit':None},
        {'pos':6,'rng':2,'hit':'Y'},
        {'pos':7,'rng':2,'hit':None},
        {'pos':8,'rng':2,'hit':None},
        {'pos':9,'rng':1,'hit':None},
        {'pos':10,'rng':1,'hit':None},
        {'pos':11,'rng':1,'hit':None},
        {'pos':12,'rng':1,'hit':None},
        {'pos':13,'rng':1,'hit':'Z'}
    ]

class T6(Track):
    name = None
    menaces = []
    ticks =[
        {'pos':0,'rng':3,'hit':None},
        {'pos':1,'rng':3,'hit':None},
        {'pos':2,'rng':3,'hit':None},
        {'pos':3,'rng':3,'hit':None},
        {'pos':4,'rng':3,'hit':None},
        {'pos':5,'rng':2,'hit':'X'},
        {'pos':6,'rng':2,'hit':None},
        {'pos':7,'rng':2,'hit':None},
        {'pos':8,'rng':2,'hit':'Y'},
        {'pos':9,'rng':2,'hit':None},
        {'pos':10,'rng':1,'hit':None},
        {'pos':11,'rng':1,'hit':None},
        {'pos':12,'rng':1,'hit':'Y'},
        {'pos':13,'rng':1,'hit':None},
        {'pos':14,'rng':1,'hit':'Z'}
    ]

class T7(Track):
    name = None
    menaces = []
    ticks =[
        {'pos':0,'rng':3,'hit':None},
        {'pos':1,'rng':3,'hit':None},
        {'pos':2,'rng':3,'hit':None},
        {'pos':3,'rng':3,'hit':None},
        {'pos':4,'rng':3,'hit':'X'},
        {'pos':5,'rng':3,'hit':None},
        {'pos':6,'rng':2,'hit':None},
        {'pos':7,'rng':2,'hit':None},
        {'pos':8,'rng':2,'hit':'Y'},
        {'pos':9,'rng':2,'hit':None},
        {'pos':10,'rng':2,'hit':None},
        {'pos':11,'rng':1,'hit':'Y'},
        {'pos':12,'rng':1,'hit':None},
        {'pos':13,'rng':1,'hit':None},
        {'pos':14,'rng':1,'hit':None},
        {'pos':15,'rng':1,'hit':'Z'}
    ]

# METHODES DU MODULE
def getTracks(spaceship):
    spaceship.trackBlue = tracks.pop()
    spaceship.trackBlue.name = "Blue"
    spaceship.trackWhite = tracks.pop()
    spaceship.trackWhite.name = "White"
    spaceship.trackRed = tracks.pop()
    spaceship.trackRed.name = "Red"
    spaceship.trackInterne = tracks.pop()
    spaceship.trackInterne.name = "Interne"
    return spaceship

tracks = []

tracks.append(T1())
tracks.append(T2())
tracks.append(T3())
tracks.append(T4())
tracks.append(T5())
tracks.append(T6())
tracks.append(T7())
random.shuffle(tracks)

print("Import du Module Track complet")
