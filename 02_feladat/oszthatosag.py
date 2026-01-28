def oszthato(szam):
    if szam % 7 == 0 and szam % 3 != 0:
        return True
    else:
        return False

darab = 0
osszeg = 0
for i in range(100, 1000):
    if oszthato(i):
        darab += 1
        osszeg += i

hettel_oszthato_de_harommal_nem = osszeg / darab
print(hettel_oszthato_de_harommal_nem)