import pygame
import os
import random


pygame.init()
# FUNCTIONS


def szoveg_general(szoveg, szin):
    return IRAS_FONT.render(szoveg, False, szin)


def dobas_szoveg_general(szoveg, szin):
    return IRAS_FONT_DOBAS.render(szoveg, False, szin)


def megjelenit_gomb(szoveg, x, y, keret_y, szin):
    screen.blit(szoveg, ((kepernyo[0] / 2 + x), (kepernyo[1] / 2) + y))
    pygame.draw.rect(screen, szin, pygame.Rect((kepernyo[0] / 2 - 115), (kepernyo[1] / 2 + keret_y), 250, 60), 3)


def megjelenit_gomb_jatek(szoveg, x, y, keret_x, szin):
    screen.blit(szoveg, ((kepernyo[0] / 2 + x), (kepernyo[1] / 2) + y))
    pygame.draw.rect(screen, szin, pygame.Rect((kepernyo[0] / 2 - keret_x), 50, 250, 60), 3)


def megjelenit_gomb_dobas(szoveg, x, y, keret_x, szin):
    screen.blit(szoveg, ((kepernyo[0] / 2 + x), (kepernyo[1] / 2) + y))
    pygame.draw.rect(screen, szin, pygame.Rect((kepernyo[0] / 2 - keret_x), 50, 350, 100), 3)


def kezdo_kep():  # első képernyő
    screen.blit(CIM, ((kepernyo[0]/2 - 370), kepernyo[1]/54))  # reszponzív fő cím
    megjelenit_gomb(szoveg_general('Folytatás', valtozo_szoveg_szinek[0]), -60, -80, -85, valtozo_szoveg_szinek[0])  # folytatás gomb
    megjelenit_gomb(szoveg_general('Új játék', valtozo_szoveg_szinek[1]), -50, -10, -15, valtozo_szoveg_szinek[1])  # játék gomb
    megjelenit_gomb(szoveg_general('Beállítások', valtozo_szoveg_szinek[2]), -75, 60, 55, valtozo_szoveg_szinek[2])  # beállítások gomb
    megjelenit_gomb(szoveg_general('Kilépés', valtozo_szoveg_szinek[-1]), -45, 130, 125, valtozo_szoveg_szinek[-1])  # kilépés gomb


def beallitasok_kep_1():  # beállításokat kezelő képernyő
    screen.blit(CIM, ((kepernyo[0]/2 - 370), kepernyo[1]/54))  # fő cím
    megjelenit_gomb(szoveg_general('Felbontás', valtozo_szoveg_szinek[1]), -65, 60, 55, valtozo_szoveg_szinek[1])  # Felbontás gomb
    megjelenit_gomb(szoveg_general('Vissza', valtozo_szoveg_szinek[-1]), -40, 130, 125, valtozo_szoveg_szinek[-1])  # vissza gomb


def beallitasok_kep_2():
    screen.blit(CIM, ((kepernyo[0] / 2 - 370), kepernyo[1] / 54))
    megjelenit_gomb(szoveg_general('Vissza', valtozo_szoveg_szinek[-1]), -40, 200, 195, valtozo_szoveg_szinek[-1])
    megjelenit_gomb(szoveg_general('1920x1050', valtozo_szoveg_szinek[1]), -75, -80, -85, valtozo_szoveg_szinek[1])
    for index in range(1, 4):
        megjelenit_gomb(szoveg_general(FELBONTASOK[index], valtozo_szoveg_szinek[index+1]), -65, (-80+index*70), (-85+index*70), valtozo_szoveg_szinek[index+1])


def jatek_kep_1(dobas, ticks, dob):
    screen.blit(KIS_CIM, (60, kepernyo[1] / 50))
    megjelenit_gomb_jatek(szoveg_general('Kilépés', valtozo_szoveg_szinek[-1]), kepernyo[0]/2 - 230, -kepernyo[1]/2 + 55, -kepernyo[0]/2 + 300, valtozo_szoveg_szinek[-1])
    megjelenit_gomb_jatek(szoveg_general('Mentés', valtozo_szoveg_szinek[1]), kepernyo[0]/2 - 530, -kepernyo[1]/2 + 55, -kepernyo[0]/2 + 600, valtozo_szoveg_szinek[1])
    pygame.draw.rect(screen, valtozo_szoveg_szinek[2], pygame.Rect((kepernyo[0] / 2 - 180), kepernyo[1]/2 + 140, 360, 110), 4)
    screen.blit(dobas_szoveg_general('DOBÁS', valtozo_szoveg_szinek[2]), ((kepernyo[0] / 2 - 115), (kepernyo[1] / 2) + 150))
    print(f"{dob} +2")
    if dobas:
        dobasa = kocka_kepek_megjelenit(dobas, ticks, dob)
        return dobasa
    else:
        kocka_kepek_megjelenit(dobas, ticks, dob)


def kocka_kepek_megjelenit(dobas, ticks, dobasok):
    if dobas:
        jelenlegi_dobasok = dobasok
        print(dobasok)
        if ticks < 30:
            jelenlegi_dobasok[0] = str(random.randint(1, 6))
        if ticks < 60:
            jelenlegi_dobasok[1] = str(random.randint(1, 6))
        if ticks < 90:
            jelenlegi_dobasok[2] = str(random.randint(1, 6))
        if ticks < 120:
            jelenlegi_dobasok[3] = str(random.randint(1, 6))
        if ticks < 150:
            jelenlegi_dobasok[4] = str(random.randint(1, 6))
        kep_1 = pygame.image.load(f'Images/kocka-{jelenlegi_dobasok[0]}.png')
        kep_2 = pygame.image.load(f'Images/kocka-{jelenlegi_dobasok[1]}.png')
        kep_3 = pygame.image.load(f'Images/kocka-{jelenlegi_dobasok[2]}.png')
        kep_4 = pygame.image.load(f'Images/kocka-{jelenlegi_dobasok[3]}.png')
        kep_5 = pygame.image.load(f'Images/kocka-{jelenlegi_dobasok[4]}.png')
        try:
            screen.blit(kep_1, (kepernyo[0] / 2 - 375, kepernyo[1] / 2 - 30))
            screen.blit(kep_2, (kepernyo[0] / 2 - 225, kepernyo[1] / 2 - 75))
            screen.blit(kep_3, (kepernyo[0] / 2 - 75, kepernyo[1] / 2 - 100))
            screen.blit(kep_4, (kepernyo[0] / 2 + 75, kepernyo[1] / 2 - 75))
            screen.blit(kep_5, (kepernyo[0] / 2 + 225, kepernyo[1] / 2 - 30))
        except:
            print("nem sikerült betölteni a képet.")
        dobasa = jelenlegi_dobasok
        return dobasa
    else:
        screen.blit(kep_0, (kepernyo[0] / 2 - 375, kepernyo[1] / 2 - 30))
        screen.blit(kep_0, (kepernyo[0] / 2 - 225, kepernyo[1] / 2 - 75))
        screen.blit(kep_0, (kepernyo[0] / 2 - 75, kepernyo[1] / 2 - 100))
        screen.blit(kep_0, (kepernyo[0] / 2 + 75, kepernyo[1] / 2 - 75))
        screen.blit(kep_0, (kepernyo[0] / 2 + 225, kepernyo[1] / 2 - 30))
        print(f"{dobasok}+1")


def pozicio(ertek_x, ertek_y):
    poziciok = [kepernyo[0] / 2 + ertek_x, kepernyo[0] / 2 + (ertek_x + 250), kepernyo[1] / 2 + ertek_y, kepernyo[1] / 2 + ertek_y + 60]
    return poziciok


def dobas_pozicio(ertek_x, ertek_y):
    poziciok = [kepernyo[0] / 2 + ertek_x, kepernyo[0] / 2 + (ertek_x + 364), kepernyo[1] / 2 + ertek_y, kepernyo[1] / 2 + ertek_y + 115]
    return poziciok


def gomb_pozicio(x, y, eger_pozicio):
    if pozicio(x, y)[0] <= eger_pozicio[0] <= pozicio(x, y)[1] and pozicio(x, y)[2] <= eger_pozicio[1] <= pozicio(x, y)[3]:
        return True
    else:
        return False


def dobas_gomb_pozicio(x, y, eger_pozicio):
    if dobas_pozicio(x, y)[0] <= eger_pozicio[0] <= dobas_pozicio(x, y)[1] and dobas_pozicio(x, y)[2] <= eger_pozicio[1] <= dobas_pozicio(x, y)[3]:
        return True
    else:
        return False


def szin_valtas(fuggveny, szin_1, szin_2):
    if fuggveny:
        return szin_1
    else:
        return szin_2


def mappa_ellenor():
    teljes_helye = os.getcwd() + "\\mentesek"
    if not os.path.isdir(teljes_helye):
        os.mkdir(teljes_helye)


def mentes_ellenor():
    mentes_hely = os.getcwd() + "\\mentesek\\"
    mentesek = os.listdir(mentes_hely)
    if len(mentesek) == 0:
        return False
    else:
        return True


# VÁLTOZÓK ÉS KONSTANSOK

# kordináták és képernyő beállítások
kepernyo = [1920, 1050]
screen = pygame.display.set_mode((kepernyo[0], kepernyo[1]))
jelenlegi_kepernyo = 1
beallitas_kepernyo = 0
jatek_kepernyo = 1

# színek
FEHER = [255, 255, 255]
FEKETE = [0, 0, 0]
PIROS = [255, 0, 0]
ZOLD = [0, 255, 0]

mappa_ellenor()
if mentes_ellenor():  # mentés ellenőrzése, hogy van-e
    FOLYTATAS_GOMB = [[255, 255, 255], [0, 255, 0]]
else:
    FOLYTATAS_GOMB = [[140, 140, 140], [140, 140, 140]]

valtozo_szoveg_szinek = [FOLYTATAS_GOMB[0], FEHER, FEHER, FEHER, FEHER, FEHER, FEHER]

# szövegek, szövegek stílusai
CIM_FONT = pygame.font.SysFont('Comic Sans MS', 142)
KIS_CIM_FONT = pygame.font.SysFont('Comic Sans MS', 78)
IRAS_FONT = pygame.font.SysFont('Arial', 42)
IRAS_FONT_DOBAS = pygame.font.SysFont('Comic Sans MS', 64)
CIM = CIM_FONT.render('Kockapóker', False, ZOLD)
KIS_CIM = KIS_CIM_FONT.render('Kockapóker', False, ZOLD)
FELBONTASOK = ['1920x1050', '1600x900', '1360x768', '1280x720']

# egyéb értékek, adatok
clock = pygame.time.Clock()
done = False
pont_tablazat = [["-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-"]]
ki_jatszik = "jatekos"
kep_0 = pygame.image.load('Images/kocka-0.png')
kep_index = 0
dobas_van_e = False
ticks = 0

# A PROGRAM

while not done:
    for event in pygame.event.get():  # esemény figyelő
        if event.type == pygame.QUIT:
            done = True

        eger_poz = pygame.mouse.get_pos()

        if jelenlegi_kepernyo == 1:   # menü gombjai és interakciói
            valtozo_szoveg_szinek[0] = szin_valtas(gomb_pozicio(-115, -85, eger_poz), FOLYTATAS_GOMB[1], FOLYTATAS_GOMB[0])  # folytatás gomb hover
            valtozo_szoveg_szinek[1] = szin_valtas(gomb_pozicio(-115, -15, eger_poz), ZOLD, FEHER)  # játék gomb hover
            valtozo_szoveg_szinek[2] = szin_valtas(gomb_pozicio(-115, 55, eger_poz), ZOLD, FEHER)  # beállítás gomb hover
            valtozo_szoveg_szinek[-1] = szin_valtas(gomb_pozicio(-115, 125, eger_poz), PIROS, FEHER)  # kilépés gomb hover

            if event.type == pygame.MOUSEBUTTONDOWN:
                if gomb_pozicio(-115, -15, eger_poz):  # játék gomb funkció
                    jelenlegi_kepernyo = 3

                if gomb_pozicio(-115, 55, eger_poz):  # Beállítások gomb funkció
                    jelenlegi_kepernyo = 2

                if gomb_pozicio(-115, 125, eger_poz):  # kilépés gomb funkció
                    done = True

        if jelenlegi_kepernyo == 2:  # beállítások gombjai és interakciói
            if beallitas_kepernyo == 1:
                valtozo_szoveg_szinek[1] = szin_valtas(gomb_pozicio(-115, 55, eger_poz), ZOLD, FEHER)
                valtozo_szoveg_szinek[-1] = szin_valtas(gomb_pozicio(-115, 125, eger_poz), PIROS, FEHER)

            if beallitas_kepernyo == 2:
                valtozo_szoveg_szinek[-1] = szin_valtas(gomb_pozicio(-115, 195, eger_poz), PIROS, FEHER)
                for index in range(4):
                    valtozo_szoveg_szinek[index+1] = szin_valtas(gomb_pozicio(-115, (-85+index*70), eger_poz), ZOLD, FEHER)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if beallitas_kepernyo == 1:
                    if gomb_pozicio(-115, 55, eger_poz):  # Felbontás gomb funkció
                        beallitas_kepernyo = 2
                        break

                    if gomb_pozicio(-115, 125, eger_poz):
                        jelenlegi_kepernyo = 1
                        beallitas_kepernyo = 0
                        break

                if beallitas_kepernyo == 2:

                    for index in range(4):  # kis bug 1600 rol  a legkisebbre való váltáskor
                        if gomb_pozicio(-115, (-85+index*70), eger_poz):
                            felbontas = FELBONTASOK[index].split("x")
                            kepernyo = int(felbontas[0]), int(felbontas[1])
                            screen = pygame.display.set_mode((kepernyo[0], kepernyo[1]))

                    if gomb_pozicio(-115, 195, eger_poz):
                        jelenlegi_kepernyo = 2
                        beallitas_kepernyo = 0

        if jelenlegi_kepernyo == 3:  # játék képernyő

            valtozo_szoveg_szinek[-1] = szin_valtas(gomb_pozicio(kepernyo[0]/2 - 300, -kepernyo[1]/2 + 50, eger_poz), PIROS, FEHER)
            valtozo_szoveg_szinek[1] = szin_valtas(gomb_pozicio(kepernyo[0]/2 - 600, -kepernyo[1]/2 + 50, eger_poz), ZOLD, FEHER)

            if jatek_kepernyo == 1:
                valtozo_szoveg_szinek[2] = szin_valtas(dobas_gomb_pozicio(- 182, 140, eger_poz), ZOLD, FEHER)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if gomb_pozicio(kepernyo[0]/2 - 300, -kepernyo[1]/2 + 50, eger_poz):
                    done = True
                if gomb_pozicio(kepernyo[0]/2 - 600, -kepernyo[1]/2 + 50, eger_poz):
                    done = True
                if dobas_gomb_pozicio(-180, 140, eger_poz):
                    dobas_van_e = True

    if jelenlegi_kepernyo == 1:  # VÁLASZTÓ KÉP
        screen.fill((0, 0, 0))
        kezdo_kep()
        dobasok = ['1','1','1','1','1']

    if jelenlegi_kepernyo == 2:  # BEÁLLÍTÁSOK KÉP
        screen.fill((0, 0, 0))
        if beallitas_kepernyo != 2:
            beallitas_kepernyo = 1
            if beallitas_kepernyo == 1:
                beallitasok_kep_1()

        if beallitas_kepernyo == 2:
            beallitasok_kep_2()

    if jelenlegi_kepernyo == 3:  # JÁTÉK PROGRAMJA
        screen.fill((0, 0, 0))
        print(f"{dobasok} +1")
        if dobas_van_e:
            dobasok = jatek_kep_1(dobas_van_e, ticks, dobasok)
        else:
            jatek_kep_1(dobas_van_e, ticks, dobasok)
        if dobas_van_e:
            if ticks % 8 == 0:
                kep_index = str(random.randint(1, 6))
            ticks += 1

    clock.tick(60)  # fps lock
    pygame.display.flip()
