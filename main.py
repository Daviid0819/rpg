# RPG

import pygame
from sys import exit

from player import *
from item import *

def main():
    pygame.init()
    width=800
    height=600
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("RPG")
    clock = pygame.time.Clock()

    p=Player("David")

    p.slots.append(items[0])
    p.slots.append(items[1])
    p.slots.append(items[2])
    p.slots.append(items[0])
    p.slots.append(items[1])
    p.slots.append(items[2])
    p.slots.append(items[3])
    p.slots.append(items[3])
    p.slots.append(items[3])
    p.slots.append(items[3])
    p.slots.append(items[3])
    p.slots.append(items[3])

    menufont = pygame.font.Font("freesansbold.ttf",30)
    menucolor = {
        "ng": "white",
        "lg": "white",
        "eg": "white"
    }

    classfont = pygame.font.Font("freesansbold.ttf",20)
    itemfont = pygame.font.Font("freesansbold.ttf",16)

    win=3
    gamemenu=0
    name=""
    clicked=0

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
            if clicked==1 and event.type==pygame.MOUSEBUTTONUP and event.button==1:
                clicked=0

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

            pygame.draw.line(screen,"white",(text_ch_rect.x+text_ch_rect.width+60,0),(text_ch_rect.x+text_ch_rect.width+60,height),1)

            # Character gamemenu
            if text_ch_rect.collidepoint(pygame.mouse.get_pos()) or gamemenu==1:
                if pygame.mouse.get_pressed()[0] or gamemenu==1:
                    if gamemenu!=1: 
                        gamemenu=1

                    # Player properties
                    text_nm = classfont.render(p.name,1,"white")
                    text_nm_rect = text_nm.get_rect()
                    text_nm_rect.x = (text_ch_rect.width+text_ch_rect.x+80+width)/2-(text_nm_rect.width/2)
                    text_nm_rect.y = 50
                    screen.blit(text_nm,(text_nm_rect.x,text_nm_rect.y))

                    text_lv = itemfont.render(f"Level: {p.lv}",1,"white")
                    screen.blit(text_lv,(((text_nm_rect.x+text_nm_rect.width/2)-40)-text_lv.get_rect().width,90))
                    
                    screen.blit(itemfont.render(f"XP: {p.xp}/{p.lv*100}",1,"white"),(((text_nm_rect.x+text_nm_rect.width/2)+40),90))

                    text_c = itemfont.render(f"Coin: {p.coin}",1,"white")
                    text_c_rect = text_c.get_rect()
                    text_c_rect.x = (text_ch_rect.width+text_ch_rect.x+80+width)/2-(text_c_rect.width/2)
                    text_c_rect.y = 130
                    screen.blit(text_c,(text_c_rect.x,text_c_rect.y))
                    
                    if text_nm_rect.collidepoint(pygame.mouse.get_pos()):
                        clas=None
                        if p.cl==1:
                            clas="Warrior"
                        elif p.cl==2:
                            clas="Mage"
                        elif p.cl==3:
                            clas="Thief"
                        else:
                            clas="Bundaskenyer"

                        p_cl = itemfont.render(f"Class: {clas}",1,"white")
                        p_cl_rect = p_cl.get_rect()
                        p_cl_rect.x = (text_nm_rect.width/2-p_cl_rect.width/2)+text_nm_rect.x
                        p_cl_rect.y = 80

                        p_str = itemfont.render(f"Strength: {p.str}",1,"white")
                        p_str_rect = p_str.get_rect()
                        p_str_rect.x = (text_nm_rect.width/2-p_str_rect.width/2)+text_nm_rect.x
                        p_str_rect.y = 100

                        p_ag = itemfont.render(f"Agility: {p.ag}",1,"white")
                        p_ag_rect = p_ag.get_rect()
                        p_ag_rect.x = (text_nm_rect.width/2-p_ag_rect.width/2)+text_nm_rect.x
                        p_ag_rect.y = 120

                        p_ig = itemfont.render(f"Intelligence: {p.ig}",1,"white")
                        p_ig_rect = p_ig.get_rect()
                        p_ig_rect.x = (text_nm_rect.width/2-p_ig_rect.width/2)+text_nm_rect.x
                        p_ig_rect.y = 140

                        pygame.draw.rect(screen,"black",pygame.Rect(min(p_cl_rect.x,p_str_rect.x,p_ag_rect.x,p_ig_rect.x),p_cl_rect.y,max(p_cl_rect.width,p_str_rect.width,p_ag_rect.width,p_ig_rect.width),90))

                        screen.blit(p_cl,(p_cl_rect.x,p_cl_rect.y))
                        screen.blit(p_str,(p_str_rect.x,p_str_rect.y))
                        screen.blit(p_ag,(p_ag_rect.x,p_ag_rect.y))
                        screen.blit(p_ig,(p_ig_rect.x,p_ig_rect.y))

                    # Show player equipped items
                    text_wep=classfont.render(f"Weapon:",1,"white")
                    screen.blit(text_wep,(((text_nm_rect.x+text_nm_rect.width/2)-80)-text_wep.get_rect().width,220))

                    screen.blit(classfont.render("Clothe:",1,"white"),(((text_nm_rect.x+text_nm_rect.width/2)+80),220))

                    if p.weapon==None:
                        text_pwep=classfont.render("None",1,"white")
                        screen.blit(text_pwep,(((text_nm_rect.x+text_nm_rect.width/2)-80)-text_pwep.get_rect().width,270))
                    else:
                        text_pwep=classfont.render(p.weapon.name,1,"white")
                        text_pwep_rect=text_pwep.get_rect()
                        text_pwep_rect.x=((text_nm_rect.x+text_nm_rect.width/2)-80)-text_pwep.get_rect().width
                        text_pwep_rect.y=270
                        screen.blit(text_pwep,(text_pwep_rect.x,text_pwep_rect.y))

                        if text_pwep_rect.collidepoint(pygame.mouse.get_pos()):
                            j=0
                            props=[]
                            recty=0
                            atk,atk_rect,de,de_rect,str,str_rect,ig,ig_rect,ag,ag_rect=None,None,None,None,None,None,None,None,None,None
                            if p.weapon.atk!=0:
                                atk = itemfont.render(f"ATK: {p.weapon.atk}",1,"white")
                                atk_rect=atk.get_rect()
                                atk_rect.x=(text_pwep_rect.width/2-atk_rect.width/2)+text_pwep_rect.x
                                atk_rect.y=text_pwep_rect.y+text_pwep_rect.height+((j*20)+10)

                                if j==0:
                                    recty=atk_rect.y
                                j+=1
                                props.append(atk_rect)

                            if p.weapon.de!=0:
                                de = itemfont.render(f"DEF: {p.weapon.de}",1,"white")
                                de_rect=de.get_rect()
                                de_rect.x=(text_pwep_rect.width/2-de_rect.width/2)+text_pwep_rect.x
                                de_rect.y=text_pwep_rect.y+text_pwep_rect.height+((j*20)+10)

                                if j==0:
                                    recty=de_rect.y
                                j+=1
                                props.append(de_rect)

                            if p.weapon.str!=0:
                                str = itemfont.render(f"STR: {p.weapon.str}",1,"white")
                                str_rect=str.get_rect()
                                str_rect.x=(text_pwep_rect.width/2-str_rect.width/2)+text_pwep_rect.x
                                str_rect.y=text_pwep_rect.y+text_pwep_rect.height+((j*20)+10)

                                if j==0:
                                    recty=str_rect.y
                                j+=1
                                props.append(str_rect)
                            
                            if p.weapon.ig!=0:
                                ig = itemfont.render(f"IG: {p.weapon.ig}",1,"white","black")
                                ig_rect=ig.get_rect()
                                ig_rect.x=(text_pwep_rect.width/2-ig_rect.width/2)+text_pwep_rect.x
                                ig_rect.y=text_pwep_rect.y+text_pwep_rect.height+((j*20)+10)

                                if j==0:
                                    recty=ig_rect.y
                                j+=1
                                props.append(ig_rect)

                            if p.weapon.ag!=0:
                                ag = itemfont.render(f"AG: {p.weapon.ag}",1,"white","black")
                                ag_rect=ag.get_rect()
                                ag_rect.x=(text_pwep_rect.width/2-ag_rect.width/2)+text_pwep_rect.x
                                ag_rect.y=text_pwep_rect.y+text_pwep_rect.height+((j*20)+10)

                                if j==0:
                                    recty=ag_rect.y
                                j+=1
                                props.append(ag_rect)

                            big=props[0]
                            for pr in props:
                                if pr.width>big.width:
                                    big=pr

                            pygame.draw.rect(screen,"black",pygame.Rect(big.x,recty,big.width,20*j))
                            if atk!=None:
                                screen.blit(atk,(atk_rect.x,atk_rect.y))
                            if de!=None:
                                screen.blit(de,(de_rect.x,de_rect.y))
                            if str!=None:
                                screen.blit(str,(str_rect.x,str_rect.y))
                            if ig!=None:
                                screen.blit(ig,(ig_rect.x,ig_rect.y))
                            if ag!=None:
                                screen.blit(ag,(ag_rect.x,ag_rect.y))

                            if pygame.mouse.get_pressed()[0] and clicked==0:
                                p.unequipWeapon()
                                clicked=1
                    
                    if p.clothe==None:
                        screen.blit(classfont.render("None",1,"white"),(((text_nm_rect.x+text_nm_rect.width/2)+80),270))
                    else:
                        text_co=classfont.render(p.clothe.name,1,"white")
                        text_co_rect=text_co.get_rect()
                        text_co_rect.x=((text_nm_rect.x+text_nm_rect.width/2)+80)
                        text_co_rect.y=270
                        screen.blit(text_co,(text_co_rect.x,text_co_rect.y))

                        if text_co_rect.collidepoint(pygame.mouse.get_pos()):
                            j=0
                            props=[]
                            recty=0
                            atk,atk_rect,de,de_rect,str,str_rect,ig,ig_rect,ag,ag_rect=None,None,None,None,None,None,None,None,None,None
                            if p.clothe.atk!=0:
                                atk = itemfont.render(f"ATK: {p.clothe.atk}",1,"white")
                                atk_rect=atk.get_rect()
                                atk_rect.x=(text_co_rect.width/2-atk_rect.width/2)+text_co_rect.x
                                atk_rect.y=text_co_rect.y+text_co_rect.height+((j*20)+10)

                                if j==0:
                                    recty=atk_rect.y
                                j+=1
                                props.append(atk_rect)

                            if p.clothe.de!=0:
                                de = itemfont.render(f"DEF: {p.clothe.de}",1,"white")
                                de_rect=de.get_rect()
                                de_rect.x=(text_co_rect.width/2-de_rect.width/2)+text_co_rect.x
                                de_rect.y=text_co_rect.y+text_co_rect.height+((j*20)+10)

                                if j==0:
                                    recty=de_rect.y
                                j+=1
                                props.append(de_rect)

                            if p.clothe.str!=0:
                                str = itemfont.render(f"STR: {p.clothe.str}",1,"white")
                                str_rect=str.get_rect()
                                str_rect.x=(text_co_rect.width/2-str_rect.width/2)+text_co_rect.x
                                str_rect.y=text_co_rect.y+text_co_rect.height+((j*20)+10)

                                if j==0:
                                    recty=str_rect.y
                                j+=1
                                props.append(str_rect)
                            
                            if p.clothe.ig!=0:
                                ig = itemfont.render(f"IG: {p.clothe.ig}",1,"white","black")
                                ig_rect=ig.get_rect()
                                ig_rect.x=(text_co_rect.width/2-ig_rect.width/2)+text_co_rect.x
                                ig_rect.y=text_co_rect.y+text_co_rect.height+((j*20)+10)

                                if j==0:
                                    recty=ig_rect.y
                                j+=1
                                props.append(ig_rect)

                            if p.clothe.ag!=0:
                                ag = itemfont.render(f"AG: {p.clothe.ag}",1,"white","black")
                                ag_rect=ag.get_rect()
                                ag_rect.x=(text_co_rect.width/2-ag_rect.width/2)+text_co_rect.x
                                ag_rect.y=text_co_rect.y+text_co_rect.height+((j*20)+10)

                                if j==0:
                                    recty=ag_rect.y
                                j+=1
                                props.append(ag_rect)

                            big=props[0]
                            for pr in props:
                                if pr.width>big.width:
                                    big=pr

                            pygame.draw.rect(screen,"black",pygame.Rect(big.x,recty,big.width,20*j))
                            if atk!=None:
                                screen.blit(atk,(atk_rect.x,atk_rect.y))
                            if de!=None:
                                screen.blit(de,(de_rect.x,de_rect.y))
                            if str!=None:
                                screen.blit(str,(str_rect.x,str_rect.y))
                            if ig!=None:
                                screen.blit(ig,(ig_rect.x,ig_rect.y))
                            if ag!=None:
                                screen.blit(ag,(ag_rect.x,ag_rect.y))

                            if pygame.mouse.get_pressed()[0] and clicked==0:
                                p.unequipClothe()
                                clicked=1                        
                    
                    # Show player items
                    text_it = classfont.render("Items",1,"white")
                    screen.blit(text_it,((text_ch_rect.width+text_ch_rect.x+80+width)/2-(text_it.get_rect().width/2),400))

                    text_items=[]
                    text_items_rect=[]
                    i=0
                    itemy=0

                    for item in p.slots:
                        text_items.append(classfont.render(item.name,1,"white"))
                        text_items_rect.append(text_items[i].get_rect())

                        if i>0 and i<6:
                            itemy+=text_items[i-1].get_rect().width
                            text_items_rect[i].x=(text_ch_rect.width+text_ch_rect.x+120)+(i*40)+itemy
                            text_items_rect[i].y=450
                        elif i>=6:
                            if i==6:
                                itemy=0
                                text_items_rect[i].x=(text_ch_rect.width+text_ch_rect.x+120)
                                text_items_rect[i].y=550
                            else:
                                itemy+=text_items[i-1].get_rect().width
                                text_items_rect[i].x=(text_ch_rect.width+text_ch_rect.x+120)+((i-6)*40)+itemy
                                text_items_rect[i].y=550
                        else:
                            text_items_rect[i].x=(text_ch_rect.width+text_ch_rect.x+120)
                            text_items_rect[i].y=450

                        screen.blit(text_items[i],(text_items_rect[i].x,text_items_rect[i].y))
                        i+=1
                        
                    # Item properties
                    i=0
                    for item in text_items_rect:
                        if item.collidepoint(pygame.mouse.get_pos()):
                            j=0
                            props=[]
                            recty=0
                            atk,atk_rect,de,de_rect,str,str_rect,ig,ig_rect,ag,ag_rect=None,None,None,None,None,None,None,None,None,None
                            if p.slots[i].atk!=0:
                                atk = itemfont.render(f"ATK: {p.slots[i].atk}",1,"white")
                                atk_rect=atk.get_rect()
                                atk_rect.x=(item.width/2-atk_rect.width/2)+item.x
                                atk_rect.y=item.y+item.height+((j*20)+10)

                                if j==0:
                                    recty=atk_rect.y
                                j+=1
                                props.append(atk_rect)

                            if p.slots[i].de!=0:
                                de = itemfont.render(f"DEF: {p.slots[i].de}",1,"white")
                                de_rect=de.get_rect()
                                de_rect.x=(item.width/2-de_rect.width/2)+item.x
                                de_rect.y=item.y+item.height+((j*20)+10)

                                if j==0:
                                    recty=de_rect.y
                                j+=1
                                props.append(de_rect)

                            if p.slots[i].str!=0:
                                str = itemfont.render(f"STR: {p.slots[i].str}",1,"white")
                                str_rect=str.get_rect()
                                str_rect.x=(item.width/2-str_rect.width/2)+item.x
                                str_rect.y=item.y+item.height+((j*20)+10)

                                if j==0:
                                    recty=str_rect.y
                                j+=1
                                props.append(str_rect)
                            
                            if p.slots[i].ig!=0:
                                ig = itemfont.render(f"IG: {p.slots[i].ig}",1,"white","black")
                                ig_rect=ig.get_rect()
                                ig_rect.x=(item.width/2-ig_rect.width/2)+item.x
                                ig_rect.y=item.y+item.height+((j*20)+10)

                                if j==0:
                                    recty=ig_rect.y
                                j+=1
                                props.append(ig_rect)

                            if p.slots[i].ag!=0:
                                ag = itemfont.render(f"AG: {p.slots[i].ag}",1,"white","black")
                                ag_rect=ag.get_rect()
                                ag_rect.x=(item.width/2-ag_rect.width/2)+item.x
                                ag_rect.y=item.y+item.height+((j*20)+10)

                                if j==0:
                                    recty=ag_rect.y
                                j+=1
                                props.append(ag_rect)

                            big=props[0]
                            for pr in props:
                                if pr.width>big.width:
                                    big=pr

                            pygame.draw.rect(screen,"black",pygame.Rect(big.x,recty,big.width,20*j))
                            if atk!=None:
                                screen.blit(atk,(atk_rect.x,atk_rect.y))
                            if de!=None:
                                screen.blit(de,(de_rect.x,de_rect.y))
                            if str!=None:
                                screen.blit(str,(str_rect.x,str_rect.y))
                            if ig!=None:
                                screen.blit(ig,(ig_rect.x,ig_rect.y))
                            if ag!=None:
                                screen.blit(ag,(ag_rect.x,ag_rect.y))

                            if pygame.mouse.get_pressed()[0] and clicked==0:
                                clicked=1
                                if p.slots[i].itype==1:
                                    p.unequipWeapon()
                                    p.equipWeapon(i)
                                elif p.slots[i].itype==2:
                                    p.unequipClothe()
                                    p.equipClothe(i)
                        i+=1

            # Missions gamemenu
            if text_ms_rect.collidepoint(pygame.mouse.get_pos()) or gamemenu==2:
                if pygame.mouse.get_pressed()[0] or gamemenu==2:
                    if gamemenu!=2: 
                        gamemenu=2
                    # quests

        pygame.display.update()
        pygame.time.delay(10)


main()