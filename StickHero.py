
import pygame
from pygame.locals import *
from random import *
from math import *

# REMPLIT LA FENETRE DE LA COULEUR RGB.

def fillwindow():
    _window.fill((255,204,51))


# GERE L'AFFICHAGE ET LE RAFRAICHISSEMENT DE LA FENETRE DANS DIFFERENTS CAS.

def affichage(c, x, y):
    global l_plateforme2, espace_p1_p2, score, xcerise, aff_cerise, cube_rouge
    if ( c == "retour" ):
        fillwindow()
        pygame.draw.rect(_window,Color(0,0,0,0),((l_init + espace_p1_p2,h_plateforme),(l_plateforme2,h_plateforme)))
        ninja(x, y)
        dessine_score(score)
        pygame.display.flip()

    if ( c == "debut" ):
        fillwindow()
        l_plateforme2 = 0
        espace_p1_p2 = 0
        plateformejeu()
        if(espace_p1_p2 > 50):
            xcerise = randint(50,espace_p1_p2-50)
        if(aff_cerise == True):
            cerise()
        ninja(0,0)
        dessine_score(score)
        pygame.display.flip()

    if ( c == "baton qui tombe" ):
        fillwindow()
        ninja(0,0)
        dessine_score(score)
        pygame.draw.line(_window,Color(0,0,0,0),(x_baton, h_plateforme), (x, y), 5)
        plateformejeu()
        if(aff_cerise == True):
            cerise()
        pygame.display.flip()

    if ( c == "deplace ninja"):
        fillwindow()
        ninja(x, y)
        plateformejeu()
        if(aff_cerise == True):
            cerise()
        dessine_score(score)
        pygame.draw.line(_window,Color(0,0,0,0),((x_baton), h_plateforme), ((x_baton) + taille_baton , h_plateforme), 5)
        pygame.display.flip()

    if ( c == "deplace ninja reverse"):
        fillwindow()
        ninja_reverse(x, y)
        plateformejeu()
        if(aff_cerise == True):
            cerise()
        dessine_score(score)
        pygame.draw.line(_window,Color(0,0,0,0),((x_baton), h_plateforme), ((x_baton) + taille_baton , h_plateforme), 5)
        pygame.display.flip()

    if ( c == "enlever cerise") :
        cerise(-500,-500)

    if ( c == "cerise"):
        message = "+5"
        myfont = pygame.font.SysFont("message", 50)
        wscore = myfont.render(message, 1, (255,0,0))
        _window.blit(wscore, (xcerise+l_init, h_plateforme-100))
        pygame.display.flip()

    if ( c == "+2"):
        message = "+2"
        myfont = pygame.font.SysFont("message", 50)
        wscore = myfont.render(message, 1, (255,0,0))
        _window.blit(wscore, (cube_rouge, h_plateforme-100))
        pygame.display.flip()
        

#DESSINE LA CERISE
def cerise(x=0,y=0):
    pygame.draw.circle(_window,Color(255,0,0,0), (l_init + xcerise - 7,h_plateforme + 38),13)
    pygame.draw.circle(_window,Color(255,0,0,0), (l_init + xcerise + 20,h_plateforme + 35), 13)
    pygame.draw.line(_window,Color(100,255,100,0),(l_init+xcerise - 5, h_plateforme + 25),(l_init+xcerise+7,h_plateforme+5),5)
    pygame.draw.line(_window,Color(100,255,100,0),(l_init+xcerise +7, h_plateforme + 5),(l_init+xcerise+17,h_plateforme+23),5)
    pygame.draw.rect(_window,Color(0,0,0,0),( (l_init + xcerise + 3,h_plateforme+3),(7, 7)))


# DESSINE LE NINJA
def ninja(x=0, y=0):
    if x==0 and y==0:
        x = l_init + 52
        y = h - 550

    stickpied1 = pygame.draw.rect(_window,Color(0,0,0,0),((x-100,y+240),(6, 10)))
    stickpied2 = pygame.draw.rect(_window,Color(0,0,0,0),((x-85,y+240),(6, 10)))
    stickcorps = pygame.draw.rect(_window,Color(0,0,0,0),((x-105,y+200),(30, 43)))
    stickoeil = pygame.draw.rect(_window,Color(255,255,255,0),((x-83,y+210),(5,5)))
    stickbandeau = pygame.draw.rect(_window,Color(255,0,0,0),((x-108,y+202),(35, 7)))
    sticknoeud = pygame.draw.rect(_window,Color(255,0,0,0),((x-115,y+205),(5, 5)))
    sticknoeud2 = pygame.draw.rect(_window,Color(255,0,0,0),((x-114,y+211),(4, 4)))


# DESSINE LE NINJA RETOURNE
def ninja_reverse(x=0, y=0):
    if x==0 and y==0:
        x = l_init + 52
        y = h - 750

    stickpied1 = pygame.draw.rect(_window,Color(0,0,0,0),((x-100,y+250),(6, 10)))
    stickpied2 = pygame.draw.rect(_window,Color(0,0,0,0),((x-85,y+250),(6, 10)))
    stickcorps = pygame.draw.rect(_window,Color(0,0,0,0),((x-105,y+260),(30, 43)))
    stickoeil = pygame.draw.rect(_window,Color(255,255,255,0),((x-83,y+283),(5,5)))
    stickbandeau = pygame.draw.rect(_window,Color(255,0,0,0),((x-108,y+291),(35, 7)))
    sticknoeud = pygame.draw.rect(_window,Color(255,0,0,0),((x-115,y+294),(5, 5)))
    sticknoeud2 = pygame.draw.rect(_window,Color(255,0,0,0),((x-114,y+289),(4, 4)))


# CREE UNE NOUVELLE PLATEFORME DE TAILLE ALEATOIRE SI CELLE-CI N'EXISTE PAS ENCORE ET L'AFFICHE.
# DESSINE AUSSI LE CARRE ROUGE AU MILIEU DE LA NOUVELLE PLATEFORME.

def plateformejeu():
    global cube_rouge, l_plateforme2, espace_p1_p2

    if l_plateforme2 == 0 and espace_p1_p2 == 0:
            l_plateforme2 = randrange(110,150)                                          #largeur de la deuxieme plateforme
            espace_p1_p2 = randrange(l_init, l_window - l_init - 150)                   # distance entre la plateforme 1 et 2

    cube_rouge = ( (l_init + espace_p1_p2) + l_plateforme2 // 2 - (l_cube_rouge // 2) ) #icone rouge sur deuxieme plateforme

    pygame.draw.rect(_window,Color(0,0,0,0),((0,h_plateforme),(l_init, 300)))                   #plateforme1
    pygame.draw.rect(_window,Color(0,0,0,0),( (l_init + espace_p1_p2,h_plateforme),(l_plateforme2,h_plateforme) ) ) # plateforme2
    pygame.draw.rect(_window,Color(255,0,0,0),( (cube_rouge,h_plateforme),(l_cube_rouge, 10)))  # objectif rouge


# GERE L'AFFICHAGE DU DEPLACEMENT LORSQUE LE NINJA EST ARRIVE SUR LA NOUVELLE PLATEFORME.

def plateformequisedeplace():
    global taille_baton, espace_p1_p2
    
    x = 225 + espace_p1_p2 + l_plateforme2 - 30
    y = h - 550

    while x > l_init + 52 :
        espace_p1_p2 = espace_p1_p2 - 5
        x = x-5
        affichage("retour", x, y)

    affichage("debut", x, y)
    taille_baton = 0
    


# GERE L'AFFICHAGE DU SCORE PASSE EN PARAMETRE.

def dessine_score(score):
    message = str(score)
    message = "SCORE : " + message 
    myfont = pygame.font.SysFont("message", 50)
    wscore = myfont.render(message, 1, (0,0,0))
    _window.blit(wscore, (l_window/2-80, 100))
    message_best_score = str(best_score)
    message_best_score = "Best score : "+message_best_score
    myfont = pygame.font.SysFont("message_best_score", 25)
    w_bestscore = myfont.render(message_best_score, 1, (0,0,0))
    _window.blit(w_bestscore, (l_window/2-50, 150))


# GERE L'AFFICHAGE DU BATON DE TAILLE PASSEE EN PARAMETRE.

def dessine_baton(taille_baton):
    pygame.draw.line(_window,Color(0,0,0,0),(x_baton, h_plateforme),(x_baton,h_plateforme-taille_baton),5)
    pygame.display.flip()

# >> A COMPLETER : FONCTION BATON QUI TOMBE :
# GERE L'ANIMATION DU BATON QUI TOMBE.

def batonquitombe():
    global taille_baton, l_plateforme2, espace_p1_p2, score
    
    for angle in range (-90, 1,1):

            angle_rad = radians(angle)
            
            x2_baton = x_baton + ( cos(angle_rad) * taille_baton )
            y2_baton = y_baton + ( sin(angle_rad) * taille_baton )

            affichage("baton qui tombe",x2_baton, y2_baton)



# GERE L'ANIMATION DU DEPLACEMENT DU NINJA QUAND LE PONT EST TOMBE.
# GERE AUSSI L'ANIMATION DE LA CHUTE DU NINJA OU NON SI LE PONT EST TROP COURT.

def deplaceninja(scr):
    global reverse
    global taille_baton, l_plateforme2, espace_p1_p2, xcerise, score,aff_cerise
    pygame.key.set_repeat(50,50)
    cerise = True
    for i in range (0,taille_baton + 52,10):
        x=(l_init + 52) + i
        for event in pygame.event.get():
            if pygame.key.get_pressed()[32]:
                if(reverse == True):
                    reverse = False
                else :
                    reverse = True
        y=h-550
        if(reverse == True):
            y = h - 548
            affichage("deplace ninja reverse", x, y)
        else:
            affichage("deplace ninja", x, y)

        if (x-70)//10 >= (l_init + xcerise)//10 and (x-100)//10 <= (l_init + xcerise)//10 and reverse == True:
            aff_cerise = False
            
        if x >= l_init + espace_p1_p2 + 70 and reverse == True:
            for p in range (0,330,1):
                y= (h-548) + p
                affichage("deplace ninja reverse", x, y)
            score = 0
            affichage("debut", x, y)
            reverse = False
            taille_baton = 0
            pygame.key.set_repeat(1,1)
            return True
        if(aff_cerise == False):
            affichage("cerise",x,y)

        if (x_baton + taille_baton) >= cube_rouge and (x_baton + taille_baton) <= (cube_rouge + l_cube_rouge):
                affichage("+2",x,y)
        
        pygame.time.delay(15)
    
    if taille_baton <= espace_p1_p2 or taille_baton >= (espace_p1_p2 + l_plateforme2):
        for p in range (0,330,3):
            y= (h-550) + p
            if(reverse == True):
                affichage("deplace ninja reverse", x, y)
            else :
                affichage("deplace ninja", x, y)

        affichage("debut", x, y)
        taille_baton = 0
        
    if(aff_cerise == False):
        score = score + 5
    aff_cerise = True
    pygame.key.set_repeat(1,1)


# Main()


# On definit les differentes variables.

l_window = 600
h = 850
h_plateforme = h - 300
l_init = 148
x = 0
y = 0
best_score = 0
reverse = False
aff_cerise = True
taille_baton = 0
x_baton = l_init - 3
y_baton = h_plateforme
score = 0
l_cube_rouge = 10
l_plateforme2 = 0
espace_p1_p2 = 0
xcerise = 0
xninja = l_init - 30

# On initialise la fenetre

pygame.init()
pygame.font.init()
_window=pygame.display.set_mode((l_window,h))


#affichage des elements du jeu

affichage("debut", x, y)


interaction = False
continuer = 1
pygame.key.set_repeat(1,1)


while continuer == 1:
    perdu = False
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            continuer = 0
            pygame.quit()
            break
        
        if pygame.key.get_pressed()[32]:
            interaction = True
            taille_baton += 1
            dessine_baton(taille_baton)

        elif interaction:
            interaction = False
            batonquitombe()
            
            if taille_baton <= espace_p1_p2 or taille_baton >= (espace_p1_p2 + l_plateforme2):
                reverse = False
                if(score > best_score):
                    best_score = score
                score = 0
                perdu = deplaceninja(score)
                reverse = False

            elif (x_baton + taille_baton) >= cube_rouge and (x_baton + taille_baton) <= (cube_rouge + l_cube_rouge):
                score += 2
                perdu = deplaceninja(score)
                reverse = False
                if(perdu!=True):
                    plateformequisedeplace()
                else :
                    score = 0
                
            elif (taille_baton <= espace_p1_p2+l_plateforme2) and (taille_baton>=espace_p1_p2):
                score +=1
                perdu = deplaceninja(score)
                reverse = False
                if(perdu!=True):
                    plateformequisedeplace()
                else :
                    score = 0
                

