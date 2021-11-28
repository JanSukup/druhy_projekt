import random

def nahodne_cislo():
    ncislo = str(random.randrange(1000,9999))
    list_nahodne_cislo = rozdeleni(ncislo)
#    print(list_nahodne_cislo)
    return(list_nahodne_cislo)

def rozdeleni(cislo:str):
    vysledek=[]
    for znak in cislo:
        vysledek.append(znak)
    return(vysledek)

def ziskani_cisla():
    test = True
    while test:
        cislo=input("Zadej čtyřmístné číslo (exit pro ukončení): ")
        if cislo == "exit":
            quit()
        elif len(cislo)==4 and cislo.isnumeric():
            test = False
        else:
            print("Zadané číslo nesplňuje podmínku.")
    return (cislo)

def vyhodnoceni(pokus_uzivatele:list, reseni:list):
    bb = {"bulls": 0, "cows": 0}
    pomocne_reseni=reseni.copy()
    for i,cislo in enumerate(pokus_uzivatele):
        if cislo == reseni[i]:
            bb["bulls"] += 1
            pomocne_reseni[i]="X"
    for i, cislo in enumerate(pokus_uzivatele):
        if cislo in pomocne_reseni:
            bb["cows"] += 1
            pomocne_reseni[pomocne_reseni.index(cislo)]="X"
#        print(cislo)
#        print(pomocne_reseni)
#    bb["cows"]=bb["cows"]-bb["bulls"]
    return(bb)

def sklonovani(vstupni_cislo:int):
    if vstupni_cislo == 1:
        sklonovani = "pokus"
    elif vstupni_cislo > 1 and vstupni_cislo < 5:
        sklonovani = "pokusy"
    elif vstupni_cislo >= 5:
        sklonovani = "pokusů"
    return sklonovani

def spojeni_listu(vstup: list):
#    vystup=""
#    for prvek in vstup:
#        vystup+=str(prvek)
#    vystup = int(''.join(list(map(lambda x: str(x), vstup))))
    vystup=''.join(map(str, vstup))
    return vystup

def format_casu(cas: float):
    cas=round(cas)
    sekundy = cas % 60
    minuty = cas // 60
    hodiny = minuty // 60
    minuty = minuty % 60
    if hodiny != 0:
        vysledny_cas = str(hodiny) + "h " + str(minuty) + "min " + str(sekundy) + "s"
    elif hodiny == 0 and minuty != 0:
        vysledny_cas = str(minuty) + "min " + str(sekundy) + "s"
    elif hodiny == 0 and minuty == 0:
        vysledny_cas = str(sekundy) + "s"
    return(vysledny_cas)