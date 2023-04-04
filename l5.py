import random
import math

# 1
def zad1():
    a = int(input('Podaj a: '))
    b = int(input('Podaj b: '))
    try:
        x = math.pow(a, 2) + a * b + math.pow(b, 2)
        plik1 = open('zadanie1.txt','w+')
        plik1.write(str(x))
    except ValueError:
        print('Wartość nie jest liczbą')
zad1()
# 2
def zad2():
    lista1 = random.sample(range(0, 100), 10)
    lista2 = random.sample(range(0, 100), 10)
    lista3 = []
    for i in range(0, len(lista1)):
        x = lista1[i] + lista2[i]
        lista3.append(x)
    print(lista3)
zad2()
# 3
def zad3():
    plik = open('tekst.txt', 'r+', encoding="utf-8")
    plik.seek(100)
    zmienna = plik.read(35)
    z = 0
    x = ""
    for i in zmienna:
        if i.isupper():
            x += i
            z += 1
    if z == 0:
        print("W fragmencie nie ma dużych liter")
    print(x)
    print(z)
zad3()
# 4
def zad4():
    listaa = random.sample(range(0, 100), 10)
    print(listaa)
    a = random.randint(0, 50)
    print(a)
    listax = [i for i in range(0, len(listaa)) if listaa[i] > a]
    print(listax)
zad4()
# 5
def zad5():
    x = math.pow(math.pow(math.e, 3) + math.pow(math.cos(39), 2) + pow((2/7), 3) + math.pi,(1/5))
    print(round(x, 2))