from funkce_ import *
import time

oddelovac = 80*"-"

print(f'''{oddelovac}
Vítejte
{oddelovac}
Vygeneroval jsem pro Vás náhodné číslo.
Pojďme hrát bulls&cows. Tak hádej, běží Ti čas!
{oddelovac}''')

#ziskani nahodneho cisla, ktere bude hadano
reseni = nahodne_cislo()
#pocitadlo pokusu
pocitadlo = 0
hadani = []
start_time = time.time()
while reseni != hadani:
    #ziskani tipu od hrace
    hadani=rozdeleni(ziskani_cisla())
    #vyhodnoceni pokusu
    vysledek = vyhodnoceni(hadani, reseni)
    if hadani != reseni:
        print("Vyhodnocení pokusu: " + str(vysledek.get("bulls")) + " bulls a "+ str(vysledek.get("cows")) + " cows.")
    print(oddelovac)
    pocitadlo+=1

#zaverecny_tisk
stop_time=time.time()
time_elapsed = stop_time - start_time
print(f"Výborně! Hledané číslo bylo {spojeni_listu(reseni)}. Uhádl jsi na {pocitadlo} {sklonovani(pocitadlo)}. Trvalo ti to {format_casu(time_elapsed)}.")
print(oddelovac)



