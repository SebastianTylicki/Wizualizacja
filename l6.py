import math as m

# 1
def zad1():
    plik = open("tekst.txt",'a+',encoding= 'utf-8')
    plik.seek(71)
    znaki = plik.read(40)
    x = int(0)
    for i in znaki:
        if i == "A":
            x = x + 1
    print(x)
    if x == 0:
        print("Brak A")
    plik.close()
zad1()
# 2
def zad2():
    lista = [10, 4, 2.5, 1.7, 8.1, 4.5, 1, 99, -1, -5.3]
    listaz = [i for i in lista if isinstance(i, int)]
    print(lista)
    print(listaz)
zad2()
# 3
listax = [1, 3, 6, -1, 4.6, 2.7, 99, -5.32]
def zad3(listax):
    x = listax[0]
    for i in range(1, len(listax)):
        x = x + listax[i]
    listax.append(x)
    print(listax)
zad3(listax)
# 4
def zad4():
    z = m.pow(m.sin(56), 2) + m.pow((m.pow(4, 2) / 25 + m.log(85, 3)), (1/4))
    print(z)
zad4()
# 5
def zad5():
    n = input("Wstaw n: ")
    try:
        n = int(n)
        x = 0
        for i in range(1, n+1):
            x = x + i
        plik = open('zadanie5.txt', 'w+')
        plik.write(str(x))
    except ValueError:
        print("N musi być liczbą całkowitą")
zad5()