# RPG

import pygame
from sys import exit

class Player:
    def __init__(self,name):
        self.name=name
        self.health=100
        self.lv=1
        self.xp=0

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

class Item:
    def __init__(self,name,atk,de,str,ig,ag):
        self.name=name
        self.atk=atk
        self.de=de
        self.str=str
        self.ig=ig
        self.ag=ag

def main():
    pygame.init()
    width=800
    height=600
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("RPG")
    clock = pygame.time.Clock()

    p=Player("dave")

    items = [
        Item("Sword",15,0,5,1,3),
        Item("Wand",7,0,2,8,4),
        Item("Knife",10,0,4,0,7),

        Item("Chainvest",0,10,3,0,-4)
    ]

    p.slots.append(items[0])
    p.slots.append(items[1])
    p.slots.append(items[2])

    menufont = pygame.font.Font("freesansbold.ttf",30)
    menucolor = {
        "ng": "white",
        "lg": "white",
        "eg": "white"
    }

    classfont = pygame.font.Font("freesansbold.ttf",20)

    win=3
    name=""

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if win==1:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    elif len(name)<10:
                        name += event.unicode

        screen.fill("black")

        if win==0: # Main menu
            text_ng = menufont.render("New Game",1,menucolor["ng"])
            text_ng_rect = text_ng.get_rect()
            text_ng_rect.x = width/2-text_ng_rect.width/2
            text_ng_rect.y = 100
            screen.blit(text_ng,(text_ng_rect.x,text_ng_rect.y))

            text_lg = menufont.render("Load Game",1,menucolor["lg"])
            text_lg_rect = text_lg.get_rect()
            text_lg_rect.x = width/2-text_lg_rect.width/2
            text_lg_rect.y = 250
            screen.blit(text_lg,(text_lg_rect.x,text_lg_rect.y))

            text_eg = menufont.render("Exit Game",1,menucolor["eg"])
            text_eg_rect = text_eg.get_rect()
            text_eg_rect.x = width/2-text_eg_rect.width/2
            text_eg_rect.y = 400
            screen.blit(text_eg,(text_eg_rect.x,text_eg_rect.y))

            if text_ng_rect.collidepoint(pygame.mouse.get_pos()):
                menucolor["ng"]="green"
                if pygame.mouse.get_pressed()[0]:
                    win=1
            elif text_lg_rect.collidepoint(pygame.mouse.get_pos()):
                menucolor["lg"]="blue"
                if pygame.mouse.get_pressed()[0]:
                    pygame.quit()
                    exit()
            elif text_eg_rect.collidepoint(pygame.mouse.get_pos()):
                menucolor["eg"]="red"
                if pygame.mouse.get_pressed()[0]:
                    pygame.quit()
                    exit()
            else:
                menucolor["ng"]="white"
                menucolor["lg"]="white"
                menucolor["eg"]="white"
        elif win==1: # Enter name
            text_en = menufont.render("Enter name:",1,"white")
            screen.blit(text_en,(width/2-text_en.get_rect().width/2,100))

            text_name = menufont.render(name, True, "white")
            screen.blit(text_name,(width/2-text_name.get_rect().width/2,250))

            text_ok = menufont.render("Start Game", True, menucolor["ng"])
            text_ok_rect = text_ok.get_rect()
            text_ok_rect.x = width/2-text_ok_rect.width/2
            text_ok_rect.y = 400
            screen.blit(text_ok,(text_ok_rect.x,text_ok_rect.y))

            if text_ok_rect.collidepoint(pygame.mouse.get_pos()):
                menucolor["ng"]="green"
                if pygame.mouse.get_pressed()[0]:
                    p=Player(name)
                    win=2
            else:
                menucolor["ng"]="white"
        elif win==2: # Switch Class
            text_sc = menufont.render("Switch Class",1,"white")
            screen.blit(text_sc,(width/2-text_sc.get_rect().width/2,100))

            text_w = classfont.render("Warrior",1,menucolor["ng"])
            text_w_rect = text_w.get_rect()
            text_w_rect.x = width/4-text_w_rect.width/4
            text_w_rect.y = 250
            screen.blit(text_w,(text_w_rect.x,text_w_rect.y))

            text_m = classfont.render("Mage",1,menucolor["lg"])
            text_m_rect = text_m.get_rect()
            text_m_rect.x = (width/4-text_m_rect.width/4)*2
            text_m_rect.y = 250
            screen.blit(text_m,(text_m_rect.x,text_m_rect.y))

            text_t = classfont.render("Thief",1,menucolor["eg"])
            text_t_rect = text_t.get_rect()
            text_t_rect.x = (width/4-text_t_rect.width/4)*3
            text_t_rect.y = 250
            screen.blit(text_t,(text_t_rect.x,text_t_rect.y))

            if text_w_rect.collidepoint(pygame.mouse.get_pos()):
                menucolor["ng"]="blue"

                text_str = classfont.render("Strength: 10",1,"white")
                screen.blit(text_str,(text_w_rect.x-((text_str.get_rect().width-text_w_rect.width)/2),290))

                text_ig = classfont.render("Intelligence: 4",1,"white")
                screen.blit(text_ig,(text_w_rect.x-((text_ig.get_rect().width-text_w_rect.width)/2),320))

                text_ag = classfont.render("Agility: 5",1,"white")
                screen.blit(text_ag,(text_w_rect.x-((text_ag.get_rect().width-text_w_rect.width)/2),350))

                if pygame.mouse.get_pressed()[0]:
                    p.setClass(1)
                    win=3
            elif text_m_rect.collidepoint(pygame.mouse.get_pos()):
                menucolor["lg"]="purple"

                text_str = classfont.render("Strength: 2",1,"white")
                screen.blit(text_str,(text_m_rect.x-((text_str.get_rect().width-text_m_rect.width)/2),290))

                text_ig = classfont.render("Intelligence: 10",1,"white")
                screen.blit(text_ig,(text_m_rect.x-((text_ig.get_rect().width-text_m_rect.width)/2),320))

                text_ag = classfont.render("Agility: 7",1,"white")
                screen.blit(text_ag,(text_m_rect.x-((text_ag.get_rect().width-text_m_rect.width)/2),350))

                if pygame.mouse.get_pressed()[0]:
                    p.setClass(2)
                    win=3
            elif text_t_rect.collidepoint(pygame.mouse.get_pos()):
                menucolor["eg"]="red"

                text_str = classfont.render("Strength: 6",1,"white")
                screen.blit(text_str,(text_t_rect.x-((text_str.get_rect().width-text_t_rect.width)/2),290))

                text_ig = classfont.render("Intelligence: 6",1,"white")
                screen.blit(text_ig,(text_t_rect.x-((text_ig.get_rect().width-text_t_rect.width)/2),320))

                text_ag = classfont.render("Agility: 10",1,"white")
                screen.blit(text_ag,(text_t_rect.x-((text_ag.get_rect().width-text_t_rect.width)/2),350))

                if pygame.mouse.get_pressed()[0]:
                    p.setClass(3)
                    win=3
            else:
                menucolor["ng"]="white"
                menucolor["lg"]="white"
                menucolor["eg"]="white"
        elif win==3: # Game menu
            text_ch = classfont.render("Character",1,"white")
            text_ch_rect = text_ch.get_rect()
            text_ch_rect.x = 40
            text_ch_rect.y = 50
            screen.blit(text_ch,(text_ch_rect.x,text_ch_rect.y))

            text_ms = classfont.render("Missions",1,"white")
            text_ms_rect = text_ms.get_rect()
            text_ms_rect.x = 40
            text_ms_rect.y = 100
            screen.blit(text_ms,(text_ms_rect.x,text_ms_rect.y))

            text_sh = classfont.render("Shop",1,"white")
            text_sh_rect = text_sh.get_rect()
            text_sh_rect.x = 40
            text_sh_rect.y = 150
            screen.blit(text_sh,(text_sh_rect.x,text_sh_rect.y))

            text_ex = classfont.render("Exit",1,"white")
            text_ex_rect = text_ex.get_rect()
            text_ex_rect.x = 40
            text_ex_rect.y = 200
            screen.blit(text_ex,(text_ex_rect.x,text_ex_rect.y))

            if text_ch_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    text_items=[]
                    i=0
                    for item in p.slots:
                        text_items.append(classfont.render(item.name,1,"white"))
                        if i>0:
                            screen.blit(text_items[i],(400,100+(i*50)))
                        else:
                            screen.blit(text_items[i],(400,100))
                        i+=1
            

        pygame.display.update()
        pygame.time.delay(10)


main()