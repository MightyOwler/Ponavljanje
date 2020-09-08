import math
import time
import random
start_time = time.time()

zgodovinski_dogodki = {
    "Napad na Bastilijo":"1789",
    "Odkritje Amerike" : "1492",
    "Rojstni dan" : "13.9",
}

seznam_dogodkov = [i for i in range(len(zgodovinski_dogodki.keys()))]
random.shuffle(seznam_dogodkov)

pravilni_odgovori = 0
vsi_odgovori = 0

for i in seznam_dogodkov:
    print(list(zgodovinski_dogodki.keys())[i])
    odgovor = str(input("Leto: "))
    if odgovor == list(zgodovinski_dogodki.values())[i]:
        print("Pravilno!")
        pravilni_odgovori += 1
    else:
        print("Narobe, pravilni odgovor je:", list(zgodovinski_dogodki.values())[i])
        seznam_dogodkov.append(i)

    vsi_odgovori += 1

print("\nPravilno si odgovoril-a na", pravilni_odgovori, "od", vsi_odgovori, "vprašanj, kar je", 100*pravilni_odgovori/vsi_odgovori, "%")
if (pravilni_odgovori == vsi_odgovori):
    print("Viljenka bi bila ponosna nate!")
if (pravilni_odgovori/vsi_odgovori < 0.5):
    print("Tako pa ne gre deček/deklica!")
print("\n")
print("Skupaj si porabil-a", round(time.time() - start_time, 0), "sekund")
