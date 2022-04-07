import pygame
import os
import random


pygame.init()
# FUNCTIONS


def megjelenit_gomb(szoveg, x, y, keret_y, szin):  # a gomb kinézetét hozza létre
    screen.blit(szoveg, ((kepernyo[0] / 2 + x), (kepernyo[1] / 2) + y))
    pygame.draw.rect(screen, szin, pygame.Rect((kepernyo[0] / 2 - 115), (kepernyo[1] / 2 + keret_y), 250, 60), 3)


def megjelenit_gomb_jatek(szoveg, x, y, keret_x, szin):  # a játék képernyő gomb kinézetét hozza létre
    screen.blit(szoveg, ((kepernyo[0] / 2 + x), (kepernyo[1] / 2) + y))
    pygame.draw.rect(screen, szin, pygame.Rect((kepernyo[0] / 2 - keret_x), 50, 250, 60), 3)


def megjelenit_gomb_dobas(szoveg, x, y, keret_x, szin):  # a dobás gomb kinezetéért felelős
    screen.blit(szoveg, ((kepernyo[0] / 2 + x), (kepernyo[1] / 2) + y))
    pygame.draw.rect(screen, szin, pygame.Rect((kepernyo[0] / 2 - keret_x), 50, 350, 100), 3)


def kezdo_kep():  # első képernyő elrendezése reszponzívan
    screen.blit(comic_szoveget_letrehoz('Kockapóker', ZOLD, 142), ((kepernyo[0]/2 - 370), kepernyo[1]/54))  # fő cím
    megjelenit_gomb(arial_szoveget_letrehoz('Folytatás', valtozo_szoveg_szinek[0], 42), -60, -80, -85, valtozo_szoveg_szinek[0])  # folytatás gomb
    megjelenit_gomb(arial_szoveget_letrehoz('Új játék', valtozo_szoveg_szinek[1], 42), -50, -10, -15, valtozo_szoveg_szinek[1])  # játék gomb
    megjelenit_gomb(arial_szoveget_letrehoz('Beállítások', valtozo_szoveg_szinek[2], 42), -75, 60, 55, valtozo_szoveg_szinek[2])  # beállítások gomb
    megjelenit_gomb(arial_szoveget_letrehoz('Kilépés', valtozo_szoveg_szinek[-1], 42), -45, 130, 125, valtozo_szoveg_szinek[-1])  # kilépés gomb


def beallitasok_kep_1():  # beállításokat kezelő képernyő
    screen.blit(comic_szoveget_letrehoz('Kockapóker', ZOLD, 142), ((kepernyo[0]/2 - 370), kepernyo[1]/54))  # fő cím
    megjelenit_gomb(arial_szoveget_letrehoz('Felbontás', valtozo_szoveg_szinek[1], 42), -65, 60, 55, valtozo_szoveg_szinek[1])  # Felbontás gomb
    megjelenit_gomb(arial_szoveget_letrehoz('Vissza', valtozo_szoveg_szinek[-1], 42), -40, 130, 125, valtozo_szoveg_szinek[-1])  # vissza gomb


def beallitasok_kep_2():  # a felbontásokat kezelő képernyő
    screen.blit(comic_szoveget_letrehoz('Kockapóker', ZOLD, 142), ((kepernyo[0] / 2 - 370), kepernyo[1] / 54))
    megjelenit_gomb(arial_szoveget_letrehoz('Vissza', valtozo_szoveg_szinek[-1], 42), -40, 200, 195, valtozo_szoveg_szinek[-1])
    megjelenit_gomb(arial_szoveget_letrehoz('1920x1050', valtozo_szoveg_szinek[1], 42), -75, -80, -85, valtozo_szoveg_szinek[1])
    for index in range(1, 4):
        megjelenit_gomb(arial_szoveget_letrehoz(FELBONTASOK[index], valtozo_szoveg_szinek[index+1], 42), -65, (-80+index*70), (-85+index*70), valtozo_szoveg_szinek[index+1])


def jatek_nav_bar():  # a fő játék fent megjelenő navigációs menüje reszponzívan
    screen.blit(comic_szoveget_letrehoz('Kockapóker', ZOLD, 78), (60, kepernyo[1] / 50))
    screen.blit(comic_szoveget_letrehoz("Kockák Számai:", ZOLD, 54), (60, kepernyo[1] / 8 + 25))
    if kepernyo[0] > 1600:
        screen.blit(kor_jelzo, (kepernyo[0]/2-310, 0))
    else:
        screen.blit(kis_kor_jelzo, (kepernyo[0]/2-160, 0))
    megjelenit_gomb_jatek(arial_szoveget_letrehoz('Kilépés', valtozo_szoveg_szinek[-1], 42), kepernyo[0]/2 - 230, -kepernyo[1]/2 + 55, -kepernyo[0]/2 + 300, valtozo_szoveg_szinek[-1])
    megjelenit_gomb_jatek(arial_szoveget_letrehoz('Mentés', valtozo_szoveg_szinek[1], 42), kepernyo[0]/2 - 530, -kepernyo[1]/2 + 55, -kepernyo[0]/2 + 600, valtozo_szoveg_szinek[1])


def jatek_kep_1(dobas, ticks, dob):  # kockák dobásának képernyője reszponzívan
    jatek_nav_bar()
    pygame.draw.rect(screen, valtozo_szoveg_szinek[2], pygame.Rect((kepernyo[0] / 2 - 180), kepernyo[1]/2 + 140, 360, 110), 4)
    screen.blit(comic_szoveget_letrehoz('DOBÁS', valtozo_szoveg_szinek[2], 64), ((kepernyo[0] / 2 - 115), (kepernyo[1] / 2) + 150))

    if dobas:
        dobasa = kocka_kepek_megjelenit(dobas, ticks, dob)
        return dobasa
    else:
        kocka_kepek_megjelenit(dobas, ticks, dob)


def kep_valtas_jateknal(tick):  # váltás a dobás és pontozás között
    if tick > 200:
        return 2, True, FEHER
    else:
        return 1, False, GYENGE_FEHER


def tablazat_rajzol(eddigi_allas, pont_mutat):  # a megjelenése a pontozó táblának a lehetséges pontokkal
    lehetseges_pontok = pontok_szamitasa(dobasok)
    osszes_pontok = [0, 0]
    FELIRATOK = ["Szemét", "2 egyforma", "3 egyforma", "2 pár", "4 egyforma", "2 + 3 egyforma", "Kis sor", "Nagy sor", "5 egyforma"]
    for index in range(2):
        for szam in eddigi_allas[index]:
            if szam != "-":
                osszes_pontok[index] += szam
    PONT_FELIRAT = [f"Játékos pontjai: {osszes_pontok[0]}p", f"Gép pontjai: {osszes_pontok[1]}p"]

    for sor_index in range(9):
        pygame.draw.rect(screen, [230, 230, 230], pygame.Rect(kepernyo[0] / 4, kepernyo[1]/2.8 + sor_index * kepernyo[1]/16, kepernyo[0]/7.68, kepernyo[1]/16 + 1), 3)
        screen.blit(comic_szoveget_letrehoz(FELIRATOK[sor_index], [0, 230, 0], int(kepernyo[0] / 60)), (kepernyo[0] / 2 - kepernyo[0] / 4 + 5, kepernyo[1] / 2.8 + sor_index * kepernyo[1] / 16 + 10))

    for oszlop_index in range(2):
        pygame.draw.rect(screen, [230, 230, 230], pygame.Rect(kepernyo[0] / 7.68 + kepernyo[0] / 4 + (oszlop_index * (kepernyo[0] / 7.68 + kepernyo[0] / 28)), kepernyo[1] / 2.8 - kepernyo[1] / 16, kepernyo[0] / 6, kepernyo[1] / 16 + 1), 3)
        screen.blit(comic_szoveget_letrehoz(PONT_FELIRAT[oszlop_index], [0, 230, 0], int(kepernyo[0] / 62)), (kepernyo[0] / 7.68 + kepernyo[0] / 4 + oszlop_index * (kepernyo[0] / 7.68 + kepernyo[0] / 28) + 10, kepernyo[1] / 2.8 - kepernyo[1] / 16 + 10))

        for sor_index in range(9):
            pygame.draw.rect(screen, [230, 230, 230], pygame.Rect(kepernyo[0] / 7.68 + kepernyo[0] / 4 + (oszlop_index * (kepernyo[0]/7.68 + kepernyo[0]/28)), kepernyo[1]/2.8 + sor_index * kepernyo[1] / 16, kepernyo[0] / 6, kepernyo[1] / 16 + 1), 3)
            if oszlop_index == 0:
                if ki_jatszik == "jatekos" and eddigi_allas[0][sor_index] == "-" and pont_mutat:
                    screen.blit(comic_szoveget_letrehoz(f"{lehetseges_pontok[sor_index]}p", [100, 100, 100], int(kepernyo[0] / 60)), (kepernyo[0] / 2.19 + (oszlop_index * kepernyo[0] / 6), kepernyo[1] / 2.75 + sor_index * kepernyo[1] / 16))
                if eddigi_allas[0][sor_index] != "-":
                    screen.blit(comic_szoveget_letrehoz(f"{eddigi_allas[0][sor_index]}p", [250, 250, 250], int(kepernyo[0] / 60)), (kepernyo[0] / 2.19 + (oszlop_index * kepernyo[0] / 6), kepernyo[1] / 2.75 + sor_index * kepernyo[1] / 16))

            if oszlop_index == 1:
                if ki_jatszik == "gep" and eddigi_allas[1][sor_index] == "-" and pont_mutat:
                    screen.blit(comic_szoveget_letrehoz(f"{lehetseges_pontok[sor_index]}p", [100, 100, 100], int(kepernyo[0] / 60)), (kepernyo[0] / 2.19 + (oszlop_index * kepernyo[0] / 6), kepernyo[1] / 2.75 + sor_index * kepernyo[1] / 16))
                if eddigi_allas[1][sor_index] != "-":
                    screen.blit(comic_szoveget_letrehoz(f"{eddigi_allas[1][sor_index]}p", [250, 250, 250], int(kepernyo[0] / 60)), (kepernyo[0] / 2.19 + (oszlop_index * kepernyo[0] / 6), kepernyo[1] / 2.75 + sor_index * kepernyo[1] / 16))
    return lehetseges_pontok


def jatek_kep_2(pont_tablazat, pont_mutat):  # a pontozó tábla pontjainak megjelenítése reszponzívan
    jatek_nav_bar()
    dobas_szoveg = ""
    for szam in dobasok:
        dobas_szoveg += str(szam) + " "
    screen.blit(comic_szoveget_letrehoz(dobas_szoveg, FEHER, 48), (470, kepernyo[1] / 8 + 30))
    return tablazat_rajzol(pont_tablazat, pont_mutat)


def jatek_kep_3(pont_tabla):  # játék vége képernyő
    ossz_pontok = [sum(pont_tabla[0]), sum(pont_tabla[1])]

    if ossz_pontok[0] > ossz_pontok[1]:
        screen.blit(comic_szoveget_letrehoz("Nyertél!", ZOLD, 104), (kepernyo[0] / 2 - 200, kepernyo[1] / 2 - 100))
        screen.blit(comic_szoveget_letrehoz(f"Játékos pontjai: {ossz_pontok[0]}p", FEHER, 36), (kepernyo[0] / 2 - 150, kepernyo[1] / 2 + 50))
        screen.blit(comic_szoveget_letrehoz(f"A gép pontjai: {ossz_pontok[1]}p", FEHER, 36), (kepernyo[0] / 2 - 125, kepernyo[1] / 2 + 100))
    elif ossz_pontok[1] > ossz_pontok[0]:
        screen.blit(comic_szoveget_letrehoz("Vesztettél!",PIROS, 104), (kepernyo[0] / 2 - 250, kepernyo[1] / 2 - 100))
        screen.blit(comic_szoveget_letrehoz(f"Játékos pontjai: {ossz_pontok[0]}p", FEHER, 36), (kepernyo[0] / 2 - 150, kepernyo[1] / 2 + 50))
        screen.blit(comic_szoveget_letrehoz(f"A gép pontjai: {ossz_pontok[1]}p", FEHER, 36), (kepernyo[0] / 2 - 125, kepernyo[1] / 2 + 100))
    else:
        screen.blit(comic_szoveget_letrehoz("Döntetlen!", FEHER, 104), (kepernyo[0] / 2 - 250, kepernyo[1] / 2 - 100))
        screen.blit(comic_szoveget_letrehoz(f"Játékos pontjai: {ossz_pontok[0]}p", FEHER, 36), (kepernyo[0] / 2 - 150, kepernyo[1] / 2 + 50))
        screen.blit(comic_szoveget_letrehoz(f"A gép pontjai: {ossz_pontok[1]}p", FEHER, 36), (kepernyo[0] / 2 - 125, kepernyo[1] / 2 + 100))


def kocka_kepek_megjelenit(dobas, ticks, dobasok):  # random váltakozó kocka képek és random számok
    if dobas:
        jelenlegi_dobasok = dobasok
        if ticks < 30:
            jelenlegi_dobasok[0] = random.randint(1, 6)
        else:
            screen.blit(arial_szoveget_letrehoz(f'{jelenlegi_dobasok[0]}', PIROS, 42), (kepernyo[0] / 2 - 310, kepernyo[1]/2 - 100))
        if ticks < 60:
            jelenlegi_dobasok[1] = random.randint(1, 6)
        else:
            screen.blit(arial_szoveget_letrehoz(f'{jelenlegi_dobasok[1]}', PIROS, 42), (kepernyo[0] / 2 - 160, kepernyo[1] / 2 - 145))
        if ticks < 90:
            jelenlegi_dobasok[2] = random.randint(1, 6)
        else:
            screen.blit(arial_szoveget_letrehoz(f'{jelenlegi_dobasok[2]}', PIROS, 42), (kepernyo[0] / 2 - 10, kepernyo[1] / 2 - 170))
        if ticks < 120:
            jelenlegi_dobasok[3] = random.randint(1, 6)
        else:
            screen.blit(arial_szoveget_letrehoz(f'{jelenlegi_dobasok[3]}', PIROS, 42), (kepernyo[0] / 2 + 140, kepernyo[1] / 2 - 145))
        if ticks < 150:
            jelenlegi_dobasok[4] = random.randint(1, 6)
        else:
            screen.blit(arial_szoveget_letrehoz(f'{jelenlegi_dobasok[4]}', PIROS, 42), (kepernyo[0] / 2 + 290, kepernyo[1] / 2 - 100))

        kep_1 = pygame.image.load(f'Images/kocka-{str(jelenlegi_dobasok[0])}.png')
        kep_2 = pygame.image.load(f'Images/kocka-{str(jelenlegi_dobasok[1])}.png')
        kep_3 = pygame.image.load(f'Images/kocka-{str(jelenlegi_dobasok[2])}.png')
        kep_4 = pygame.image.load(f'Images/kocka-{str(jelenlegi_dobasok[3])}.png')
        kep_5 = pygame.image.load(f'Images/kocka-{str(jelenlegi_dobasok[4])}.png')
        try:
            screen.blit(kep_1, (kepernyo[0] / 2 - 375, kepernyo[1] / 2 - 30))
            screen.blit(kep_2, (kepernyo[0] / 2 - 225, kepernyo[1] / 2 - 75))
            screen.blit(kep_3, (kepernyo[0] / 2 - 75, kepernyo[1] / 2 - 100))
            screen.blit(kep_4, (kepernyo[0] / 2 + 75, kepernyo[1] / 2 - 75))
            screen.blit(kep_5, (kepernyo[0] / 2 + 225, kepernyo[1] / 2 - 30))
        except:
            print("Hiányoznak a kocka képek")
        dobasa = jelenlegi_dobasok
        return dobasa
    else:
        screen.blit(kep_0, (kepernyo[0] / 2 - 375, kepernyo[1] / 2 - 30))
        screen.blit(kep_0, (kepernyo[0] / 2 - 225, kepernyo[1] / 2 - 75))
        screen.blit(kep_0, (kepernyo[0] / 2 - 75, kepernyo[1] / 2 - 100))
        screen.blit(kep_0, (kepernyo[0] / 2 + 75, kepernyo[1] / 2 - 75))
        screen.blit(kep_0, (kepernyo[0] / 2 + 225, kepernyo[1] / 2 - 30))


def pozicio(ertek_x, ertek_y):  # 4 elemű listát ad vissza amivel körbe lehet határolni egy gombot
    poziciok = [kepernyo[0] / 2 + ertek_x, kepernyo[0] / 2 + (ertek_x + 250), kepernyo[1] / 2 + ertek_y, kepernyo[1] / 2 + ertek_y + 60]
    return poziciok


def dobas_pozicio(ertek_x, ertek_y):  # a dobás gomb kordináta listája
    poziciok = [kepernyo[0] / 2 + ertek_x, kepernyo[0] / 2 + (ertek_x + 364), kepernyo[1] / 2 + ertek_y, kepernyo[1] / 2 + ertek_y + 115]
    return poziciok


def pont_ertek_pozicio(index):  # a pontozó tábla gombjainak kordináta listája
    poziciok = [kepernyo[0] / 2.63, kepernyo[0] / 2.63 + kepernyo[0] / 6, kepernyo[1] / 2.75 + index * kepernyo[1] / 16, kepernyo[1] / 2.75 + (index+1) * kepernyo[1] / 16]
    return poziciok


def gomb_pozicio(x, y, eger_pozicio):  # megvizsgálja, hogy az egér a kordináta lista értékein belül van-e
    if pozicio(x, y)[0] <= eger_pozicio[0] <= pozicio(x, y)[1] and pozicio(x, y)[2] <= eger_pozicio[1] <= pozicio(x, y)[3]:
        return True
    else:
        return False


def dobas_gomb_pozicio(x, y, eger_pozicio):  # egér helyzetét figyelembe vevő függvény
    if dobas_pozicio(x, y)[0] <= eger_pozicio[0] <= dobas_pozicio(x, y)[1] and dobas_pozicio(x, y)[2] <= eger_pozicio[1] <= dobas_pozicio(x, y)[3]:
        return True
    else:
        return False


def pont_ertek_gomb_pozicio(eger_pozicio, index):  # egér helyzetét figyelembe vevő függvény
    if pont_ertek_pozicio(index)[0] <= eger_pozicio[0] <= pont_ertek_pozicio(index)[1] and pont_ertek_pozicio(index)[2] <= eger_pozicio[1] <= pont_ertek_pozicio(index)[3]:
        return True
    else:
        return False


def szin_valtas(fuggveny, szin_1, szin_2):  # hover effekt színváltása
    if fuggveny:
        return szin_1
    else:
        return szin_2


def mappa_ellenor():  # ellenőrzi létezik-e a mentés mappa, ha nem akkor létrehozza
    teljes_helye = os.getcwd() + "\\mentesek"
    if not os.path.isdir(teljes_helye):
        os.mkdir(teljes_helye)


def mentes_ellenor():  # ellenőrzi van-e mentett játék
    mentes_hely = os.getcwd() + "\\mentesek\\"
    mentesek = os.listdir(mentes_hely)
    if len(mentesek) == 0:
        return False
    else:
        return True


def mentes_betoltese():  # betölti a mentett játékot
    mentes_hely = os.getcwd() + "\\mentesek\\mentes.txt"
    mentes = open(mentes_hely, "rt", encoding="UTF-8")
    adatok = mentes.readlines()
    pontok = [adatok[0].split(" "), adatok[1].split(" ")]
    for oszlop_index in range(2):
        pontok[oszlop_index].pop(-1)
        for sor_index in range(9):
            if pontok[oszlop_index][sor_index] != "-":
                pontok[oszlop_index][sor_index] = int(pontok[oszlop_index][sor_index])
    dobas = adatok[2].split(" ")
    dobas.pop(-1)
    for index in range(5):
        dobas[index] = int(dobas[index])
    ki_jon = adatok[3]
    mentes.close()
    return pontok, dobas, ki_jon


def jatek_lementese(adatok):  # lementi a játék állását
    mentes_hely = os.getcwd() + "\\mentesek\\mentes.txt"
    mentes = open(mentes_hely, "wt", encoding="UTF-8")
    for index in range(4):
        if index == 0 or index == 1 or index == 2:
            pontok = ""
            for adat in adatok[index]:
                pontok += f"{adat} "
            pontok += "\n"
            mentes.write(pontok)
        else:
            mentes.write(adatok[index])
    mentes.close()


def torol_mentes():  # új játék esetén törli a mentést
    mentes_hely = os.getcwd() + "\\mentesek\\mentes.txt"
    if os.path.exists(mentes_hely):
        os.remove(mentes_hely)


def comic_betu_font(pt):  # Comic betűtípus és fontnagyság szöveghez
    return pygame.font.SysFont('Comic Sans MS', pt)


def arial_betu_font(pt):  # Arial betűtípus és fontnagyság szöveghez
    return pygame.font.SysFont('Arial', pt)


def comic_szoveget_letrehoz(szoveg, szin, pt):  # comic szöveg generálás
    return comic_betu_font(pt).render(szoveg, False, szin)


def arial_szoveget_letrehoz(szoveg, szin, pt):  # arial szöveg generálás
    return arial_betu_font(pt).render(szoveg, False, szin)


def pontok_szamitasa(szamok):  # kiszámítja a kilenc mezőből, hogy melyik mennyi pontot ér
    return [szemet(szamok), ket_egyforma(szamok), harom_egyforma(szamok), ket_par(szamok), negy_egyforma(szamok), ket_es_harom_egyforma(szamok), kis_sor(szamok), nagy_sor(szamok), ot_egyforma(szamok)]


def szemet(dobott_szamok):  # szemét pont számítása
    return sum(dobott_szamok)


def ket_egyforma(dobott_szamok):  # két egyforma pont számítása
    legnagyobb_talalat = 0
    for szam in dobott_szamok:
        talalat = dobott_szamok.count(szam)
        if talalat > 1:
            if szam + szam > legnagyobb_talalat:
                legnagyobb_talalat = szam + szam
    return legnagyobb_talalat


def harom_egyforma(dobott_szamok):  # három egyforma pont számítása
    legnagyobb_talalat = 0
    for szam in dobott_szamok:
        talalat = dobott_szamok.count(szam)
        if talalat > 2:
            legnagyobb_talalat = szam*3
            break
    return legnagyobb_talalat


def ket_par(dobott_szamok):  # két pár pont számítása
    talalatok = 0
    eredmeny = 0
    volt_szam = []
    for szam in dobott_szamok:
        talalat = dobott_szamok.count(szam)
        if talalat > 1 and szam not in volt_szam:
            talalatok += 1
            volt_szam.append(szam)
            if talalatok == 2:
                eredmeny += volt_szam[0]*2 + volt_szam[1]*2
    return eredmeny


def negy_egyforma(dobott_szamok):  # négy egyforma pont számítása
    eredmeny = 0
    for szam in dobott_szamok:
        talalat = dobott_szamok.count(szam)
        if talalat > 3:
            eredmeny = szam*4
            break
    return eredmeny


def ket_es_harom_egyforma(dobott_szamok):  # két és három egyforma pont számítása
    volt_szam = [0, 0]
    talalatok = [False, False]
    for szam in dobott_szamok:
        talalat = dobott_szamok.count(szam)
        if talalat == 2:
            volt_szam[0] = szam
            talalatok[0] = True
        if talalat == 3:
            volt_szam[1] = szam
            talalatok[1] = True
    if talalatok[0] and talalatok[1]:
        return volt_szam[0]*2 + volt_szam[1]*3
    else:
        return 0


def kis_sor(dobott_szamok):  # kis sor pont számítása
    if all(x in dobott_szamok for x in [1, 2, 3, 4, 5]):
        return 15
    else:
        return 0


def nagy_sor(dobott_szamok):  # nagy sor pont számítása
    if all(x in dobott_szamok for x in [2, 3, 4, 5, 6]):
        return 20
    else:
        return 0


def ot_egyforma(dobott_szamok):  # öt egyforma pont számítása
    talalat = dobott_szamok.count(dobott_szamok[0])
    if talalat == 5:
        return 50
    else:
        return 0


# VÁLTOZÓK ÉS KONSTANSOK

# kordináták és képernyő beállítások
pygame.display.set_caption('Kockapóker')  # ablak cím
kepernyo = [1920, 1050]  # képernyő felbontása
screen = pygame.display.set_mode((kepernyo[0], kepernyo[1]))
jelenlegi_kepernyo = 1  # a program 3 fő képernyőjét szabályozza
beallitas_kepernyo = 0  # a beállítások képernyő al lapjait szabályozza
jatek_kepernyo = 1  # a játék képernyő al lapjait szabályozza

# színek
FEHER = [255, 255, 255]
GYENGE_FEHER = [140, 140, 140]
FEKETE = [0, 0, 0]
PIROS = [255, 0, 0]
ZOLD = [0, 255, 0]

mappa_ellenor()
if mentes_ellenor():  # mentés ellenőrzése, hogy van-e
    FOLYTATAS_GOMB = [[255, 255, 255], [0, 255, 0]]
else:
    FOLYTATAS_GOMB = [GYENGE_FEHER, GYENGE_FEHER]

valtozo_szoveg_szinek = [FOLYTATAS_GOMB[0], FEHER, FEHER, FEHER, FEHER, FEHER, FEHER]  # hover effekthez használt színek


# értékek, adatok
FELBONTASOK = ['1920x1050', '1600x900', '1360x768', '1280x720']  # lehetséges felbontások

clock = pygame.time.Clock()
done = False  # program ciklus befejezője
pont_tablazat = [["-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-"]]  # a játékosok pontjai
ki_jatszik = "jatekos"  # melyik fél játszik
kep_0 = pygame.image.load('Images/kocka-0.png')  # a dobókockák kérdőjeles képe

kep_index = 0  # a random képekhez segéd változó
dobas_van_e = False  # ellenőrzi, hogy van-e dobás
ticks = 0  # időt jelző változó

# -------------------------------------------------- A PROGRAM ---------------------------------------------------

while not done:
    for event in pygame.event.get():  # Felhasználói eseményhez kötött program rész
        if event.type == pygame.QUIT:
            done = True

        eger_poz = pygame.mouse.get_pos()

        if jelenlegi_kepernyo == 1:   # menü gombjai és interakciói
            valtozo_szoveg_szinek[0] = szin_valtas(gomb_pozicio(-115, -85, eger_poz), FOLYTATAS_GOMB[1], FOLYTATAS_GOMB[0])  # folytatás gomb hover
            valtozo_szoveg_szinek[1] = szin_valtas(gomb_pozicio(-115, -15, eger_poz), ZOLD, FEHER)  # játék gomb hover
            valtozo_szoveg_szinek[2] = szin_valtas(gomb_pozicio(-115, 55, eger_poz), ZOLD, FEHER)  # beállítás gomb hover
            valtozo_szoveg_szinek[-1] = szin_valtas(gomb_pozicio(-115, 125, eger_poz), PIROS, FEHER)  # kilépés gomb hover

            if event.type == pygame.MOUSEBUTTONDOWN:
                if gomb_pozicio(-115, -85, eger_poz) and FOLYTATAS_GOMB[0] != GYENGE_FEHER:  # folytatás gomb funkció
                    adatok = mentes_betoltese()
                    pont_tablazat = adatok[0]
                    print(pont_tablazat)
                    dobasok = adatok[1]
                    print(dobasok)
                    ki_jatszik = adatok[2]
                    jelenlegi_kepernyo = 3
                    jatek_kepernyo = 2
                    rakott_e_pontot = False
                    pont_mutat = True
                    betoltve = False
                    ticks = 200

                if gomb_pozicio(-115, -15, eger_poz):  # játék gomb funkció
                    jelenlegi_kepernyo = 3
                    torol_mentes()

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

                    for index in range(4):
                        if gomb_pozicio(-115, (-85+index*70), eger_poz):
                            felbontas = FELBONTASOK[index].split("x")
                            kepernyo = int(felbontas[0]), int(felbontas[1])
                            screen = pygame.display.set_mode((kepernyo[0], kepernyo[1]))

                    if gomb_pozicio(-115, 195, eger_poz):
                        jelenlegi_kepernyo = 2
                        beallitas_kepernyo = 0

        if jelenlegi_kepernyo == 3:  # játék képernyő gombjai és interakciói

            valtozo_szoveg_szinek[-1] = szin_valtas(gomb_pozicio(kepernyo[0]/2 - 300, -kepernyo[1]/2 + 50, eger_poz), PIROS, FEHER)

            if jatek_kepernyo == 1:
                valtozo_szoveg_szinek[1] = szin_valtas(gomb_pozicio(kepernyo[0]/2 - 600, -kepernyo[1]/2 + 50, eger_poz), GYENGE_FEHER, GYENGE_FEHER)
                if ki_jatszik == "jatekos":
                    valtozo_szoveg_szinek[2] = szin_valtas(dobas_gomb_pozicio(- 182, 140, eger_poz), ZOLD, FEHER)
                else:
                    valtozo_szoveg_szinek[2] = szin_valtas(dobas_gomb_pozicio(- 182, 140, eger_poz), GYENGE_FEHER, GYENGE_FEHER)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if gomb_pozicio(kepernyo[0]/2 - 300, -kepernyo[1]/2 + 50, eger_poz):
                    done = True
                if dobas_gomb_pozicio(-180, 140, eger_poz) or ki_jatszik == "gep":
                    dobas_van_e = True

            if jatek_kepernyo == 2:
                if rakott_e_pontot:
                    valtozo_szoveg_szinek[1] = szin_valtas(gomb_pozicio(kepernyo[0] / 2 - 600, -kepernyo[1] / 2 + 50, eger_poz), GYENGE_FEHER, GYENGE_FEHER)
                else:
                    valtozo_szoveg_szinek[1] = szin_valtas(gomb_pozicio(kepernyo[0] / 2 - 600, -kepernyo[1] / 2 + 50, eger_poz), ZOLD, FEHER)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if gomb_pozicio(kepernyo[0] / 2 - 600, -kepernyo[1] / 2 + 50, eger_poz) and not rakott_e_pontot:
                        mentendo_adatok = [pont_tablazat[0], pont_tablazat[1], dobasok, ki_jatszik]
                        jatek_lementese(mentendo_adatok)

                    for sor_index in range(9):
                        if pont_ertek_gomb_pozicio(eger_poz, sor_index) and pont_tablazat[0][sor_index] == "-" and not rakott_e_pontot and ki_jatszik == "jatekos" and betoltve:
                            pont_tablazat[0][sor_index] = lehetseges_pontok[sor_index]
                            ticks = 0
                            rakott_e_pontot = True
                            valtozo_szoveg_szinek[1] = GYENGE_FEHER

# -------------------------------Nem felhasználói eseményhez kötött program rész---------------------------------------
    if jelenlegi_kepernyo == 1:  # VÁLASZTÓ KÉP megjelenése
        screen.fill((0, 0, 0))
        kezdo_kep()
        dobasok = ['1','1','1','1','1']

    if jelenlegi_kepernyo == 2:  # BEÁLLÍTÁSOK KÉP megjelenése
        screen.fill((0, 0, 0))
        if beallitas_kepernyo != 2:  # felbontások
            beallitas_kepernyo = 1
            if beallitas_kepernyo == 1:  # beállítási opciók
                beallitasok_kep_1()

        if beallitas_kepernyo == 2:
            beallitasok_kep_2()

    if jelenlegi_kepernyo == 3:  # JÁTÉK PROGRAMJA, megjelenése
        screen.fill((0, 0, 0))
        kor_jelzo = pygame.image.load(f'Images/{ki_jatszik}.png')
        kis_kor_jelzo = pygame.transform.scale(kor_jelzo, (345, 230))

        if jatek_kepernyo == 1:  # kocka dobás
            if ki_jatszik == "gep":
                dobas_van_e = True

            if dobas_van_e:  # kockák dobása
                dobasok = jatek_kep_1(dobas_van_e, ticks, dobasok)
                if ticks % 8 == 0:
                    kep_index = str(random.randint(1, 6))
                ticks += 1
                jatek_kepernyo, pont_mutat, valtozo_szoveg_szinek[1] = kep_valtas_jateknal(ticks)
                rakott_e_pontot = False
            else:
                jatek_kep_1(dobas_van_e, ticks, dobasok)
                ticks = 0

            if ticks % 8 == 0:
                kep_index = str(random.randint(1, 6))

        if jatek_kepernyo == 2:  # pontozó tábla
            if "-" not in pont_tablazat[1]:
                jelenlegi_kepernyo = 4
            lehetseges_pontok = jatek_kep_2(pont_tablazat, pont_mutat)
            if ticks > 135 and ki_jatszik == "gep":
                ticks = 0
            ticks += 1

            if ki_jatszik == "gep" and ticks == 100:  # amikor gép köre jön
                pontot_ero_hely = 0
                legnagyobb_pont = [0, 0]
                for index in range(9):
                    if pont_tablazat[1][index] == "-" and lehetseges_pontok[index] != 0:
                        pontot_ero_hely += 1
                        if lehetseges_pontok[index] > legnagyobb_pont[0]:
                            legnagyobb_pont = lehetseges_pontok[index], index

                if pontot_ero_hely == 0:
                    for index in range(9):
                        if pont_tablazat[1][index] == "-" and not rakott_e_pontot:
                            pont_tablazat[1][index] = lehetseges_pontok[index]
                            rakott_e_pontot = True
                            valtozo_szoveg_szinek[1] = GYENGE_FEHER
                else:
                    pont_tablazat[1][legnagyobb_pont[1]] = lehetseges_pontok[legnagyobb_pont[1]]

            if ticks == 135:
                dobas_van_e = False
                if ki_jatszik == "jatekos":  # játszó fél váltás
                    ki_jatszik = "gep"
                else:
                    ki_jatszik = "jatekos"

                ticks = 0
                jatek_kepernyo = 1

    if jelenlegi_kepernyo == 4:  # befejezés képernyő
        screen.fill(FEKETE)
        jatek_kep_3(pont_tablazat)
    betoltve = True
    clock.tick(60)  # fps lock
    pygame.display.flip()



