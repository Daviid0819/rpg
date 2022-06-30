class Item:
    def __init__(self,name,atk,de,str,ig,ag,price,itype):
        self.name=name
        self.atk=atk
        self.de=de
        self.str=str
        self.ig=ig
        self.ag=ag
        self.price=price
        self.sell=price*0.75
        self.itype=itype

items = [
    Item("Sword",15,0,5,1,3,20,1),
    Item("Wand",7,0,2,8,4,20,1),
    Item("Knife",10,0,4,0,7,20,1),

    Item("Chainvest",0,10,3,0,-4,20,2)
]