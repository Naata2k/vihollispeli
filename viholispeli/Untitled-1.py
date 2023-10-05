import pygame
import random

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Piirtäminen")


def piirraKuva(kuvatiedosto, x, y):
    naytto.blit(kuvatiedosto, (x, y))

def piirtaminen(naytto, hahmot, viholliset):
    naytto.fill((255, 255, 255))

    #Mc:n piirto
    for hahmo in hahmot:
        if hahmo[3] == True:
            kuva = pygame.image.load(hahmo[0]).convert_alpha()
            naytto.blit(kuva, (hahmo[1], hahmo[2]))

    #Vihujen piirto
    for vihollinen in viholliset:
        if vihollinen[3] == True:
            kuva1 = pygame.image.load(vihollinen[0]).convert_alpha()
            naytto.blit(kuva1, (vihollinen[1], vihollinen[2]))
            

    pygame.display.flip()

def kontrolli(hahmot, tapahtuma, viholliset):

    MC = hahmot[0]

    for vihollinen in viholliset:
        if vihollinen[1] <= MC[1] + 50 <= vihollinen[1] + 100:
            if vihollinen[2] <= MC[2] + 75 <= vihollinen[2] + 150:
                hahmot[0][3] = False

    if viholliset[0][1] > 540:
        viholliset[0][1] = 0
        viholliset[0][2] = random.randint(0, 250)
    else:
        viholliset[0][1] += random.randint(0, 10) / 10
    
    if vihollinen[1] > 640:
        vihollinen[1] = 0
        vihollinen[2] = random.randint(0, 250)
    else:
        vihollinen[1] += random.randint(0, 10) / 10
    

    if tapahtuma.type == pygame.KEYDOWN:

        if tapahtuma.key == pygame.K_SPACE:
            hahmot[0][3] = True
            viholliset[0][3] = True
            viholliset[1][3] = True

        #hahmon liikuttaminen
        elif tapahtuma.key == pygame.K_RIGHT: 
            if MC[1] == 540:
                MC[1] += 0
            else:
                MC[1] += 20
        elif tapahtuma.key == pygame.K_LEFT: 
            if MC[1] == 0:
                MC[1] += 0
            else:
                MC[1] -= 20
        elif tapahtuma.key == pygame.K_UP:
            if MC[2] == 0:
                MC[2] += 0
            else:
                MC[2] -= 20
        elif tapahtuma.key == pygame.K_DOWN:
            if MC[2] == 250:
                MC[2] += 0
            else:
                MC[2] += 20

def main():
    MC = ["MC.png", 100, 100, False]
    vihunen = ["vihunen.png", random.randint(0, 540), random.randint(0, 300), False]
    vihree = ["vihree.png", random.randint(0, 540), random.randint(0, 300), False]
    hahmot = [MC]
    viholliset = [vihunen, vihree]
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break
        kontrolli(hahmot, tapahtuma, viholliset)
        piirtaminen(naytto, hahmot, viholliset)


main()