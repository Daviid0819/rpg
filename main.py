# RPG

import pygame
from sys import exit

class Player:
    def __init__(self,name):
        self.name=name
        self.health=100
        self.lv=1
        self.xp=0

def main():
    pygame.init()
    width=800
    height=600
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("RPG")
    clock = pygame.time.Clock()

    menufont = pygame.font.Font("freesansbold.ttf",30)

    win=0
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
                    else:
                        name += event.unicode

        screen.fill("black")

        if win==0:
            text_ng = menufont.render("New Game",1,"white")
            screen.blit(text_ng,(width/2-text_ng.get_rect().width/2,100))

            text_ng_rect = text_ng.get_rect()
            text_ng_rect.x = width/2-text_ng.get_rect().width/2
            text_ng_rect.y = 100

            text_lg = menufont.render("Load Game",1,"white")
            screen.blit(text_lg,(width/2-text_lg.get_rect().width/2,250))

            text_lg_rect = text_lg.get_rect()
            text_lg_rect.x = width/2-text_lg.get_rect().width/2
            text_lg_rect.y = 250

            text_eg = menufont.render("Exit Game",1,"white")
            screen.blit(text_eg,(width/2-text_eg.get_rect().width/2,400))

            text_eg_rect = text_eg.get_rect()
            text_eg_rect.x = width/2-text_eg.get_rect().width/2
            text_eg_rect.y = 400

            if pygame.mouse.get_pressed()[0] and text_ng_rect.collidepoint(pygame.mouse.get_pos()):
                win=1
            elif pygame.mouse.get_pressed()[0] and text_lg_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                exit()
            elif pygame.mouse.get_pressed()[0] and text_eg_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                exit()
        elif win==1:
            text_ng = menufont.render("Enter name:",1,"white")
            screen.blit(text_ng,(width/2-text_ng.get_rect().width/2,100))

            text_name = menufont.render(name, True, "white")
            screen.blit(text_name,(width/2-text_name.get_rect().width/2,250))

            text_ok = menufont.render("Start Game", True, "white")
            screen.blit(text_ok,(width/2-text_ok.get_rect().width/2,400))

        pygame.display.update()
        pygame.time.delay(10)


main()