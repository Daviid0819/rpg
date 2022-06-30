from item import *

class Player:
    def __init__(self,name):
        self.name=name
        self.health=100 # Do I need this!?
        self.lv=1
        self.xp=0
        self.coin=100

        self.slots=[]
        self.weapon=None
        self.clothe=None

        self.cl=0
        self.str=0
        self.ig=0
        self.ag=0
    
    def setClass(self,num):
        self.cl=num
        if num==1: # Warrior
            self.str=10
            self.ig=4
            self.ag=5
        elif num==2: # Mage
            self.str=2
            self.ig=10
            self.ag=7
        elif num==3: # Thief
            self.str=6
            self.ig=6
            self.ag=10
    
    def equipWeapon(self,item):
        self.weapon=self.slots[item]

        if self.clothe!=None:
            self.str=self.weapon.str+self.clothe.str
            self.ig=self.weapon.ig+self.clothe.ig
            self.ag=self.weapon.ag+self.clothe.ag
        else:
            self.str=self.weapon.str
            self.ig=self.weapon.ig
            self.ag=self.weapon.ag

        if self.str<0:
            self.str=0

        if self.ig<0:
            self.ig=0

        if self.ag<0:
            self.ag=0

        self.slots.pop(item)

    def equipClothe(self,item):
        self.clothe=self.slots[item]

        if self.weapon!=None:
            self.str=self.clothe.str+self.weapon.str
            self.ig=self.clothe.ig+self.weapon.ig
            self.ag=self.clothe.ag+self.weapon.ag
        else:
            self.str=self.clothe.str
            self.ig=self.clothe.ig
            self.ag=self.clothe.ag

        if self.str<0:
            self.str=0

        if self.ig<0:
            self.ig=0

        if self.ag<0:
            self.ag=0

        self.slots.pop(item)

    def unequipWeapon(self):
        if self.weapon!=None:
            self.slots.append(self.weapon)

            self.str-=self.weapon.str
            if self.str<0:
                self.str=0

            self.ig-=self.weapon.ig
            if self.ig<0:
                self.ig=0

            self.ag-=self.weapon.ag
            if self.ag<0:
                self.ag=0

            self.weapon=None
    
    def unequipClothe(self):
        if self.clothe!=None:
            self.slots.append(self.clothe)

            self.str-=self.clothe.str
            if self.str<0:
                self.str=0

            self.ig-=self.clothe.ig
            if self.ig<0:
                self.ig=0

            self.ag-=self.clothe.ag
            if self.ag<0:
                self.ag=0

            self.clothe=None
