import random
# 1
def zad1():
    a = random.sample(range(0, 31), 10)
    print(a)
    for i in range(0, len(a)):
        a[i] = a[i]*2
    print(a)
    a = str(a)
    plik1 = open("z1.txt", "a+")
    plik1.writelines(a)
    plik1.close()
zad1()
# 2
def zad2():
    plik2 = open("z1.txt", "r")
    print(plik2.read())
    plik2.close()
zad2()
# 3
def zad3():
    with open("z3.txt", "w") as plik3:
        for i in range(10):
            plik3.write("zxc\n")
    plik3 = open("z3.txt", "r")
    print(plik3.read())
    plik3.close()
zad3()
# 4
def zad4():
    class NaZakupy:
        def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
            self.nazwa_produktu = nazwa_produktu
            self.ilosc = ilosc
            self.jednostka_miary = jednostka_miary
            self. cena_jed = cena_jed
        def wyswietl_produkt(self):
            print(self.nazwa_produktu)
            print(self.ilosc)
            print(self.jednostka_miary)
            print(self. cena_jed)
        def ile_produktu(self):
            print(self.ilosc)
            print(self.jednostka_miary)
        def ile_kosztuje(self):
            print(self.cena_jed * self.jednostka_miary)
    obiekt = NaZakupy("woda",2,"litry",0.5)
