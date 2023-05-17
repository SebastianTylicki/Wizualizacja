a = 'napis \ndrugi napis'
print(a)
b = 5
c = 11
print(b, c)
d = 5+3j
print(d)

e = c+d
print(e)

f = c // b
print(f)
g = c % b
print(g)
h = b ** 2
print(h)
i = b ** 1/2
j = pow(b, 1/2)
print(i, j)

print('b = b + 2')
print(b)
b += 2
print(b)

listy = ['a', 4, 5, 6, [1, 2, 3], 5.6]
print(listy)
listy.append(4)
print(listy)
print(listy[5])

# 1) dodac element na wybrane miejsce
# 2) dodac kilka elementow
# 3) usunac element z listy o danej pozycji
# 4) usunac element z listy o danej wartosci
# 5) odwrocic elementy listy
# 6) zrobic sortowanie

tab = [1, 2, 3, 4, 5, 5, 5, 2, 4]
# 1)
listy.insert(4, 'bb')
print(listy)
# 2)
listy.extend(tab)
print(listy)
# 3)
listy.pop(4)
print(listy)
# 4)
listy.remove('a')
print(listy)
# 5)
listy.reverse()
print(listy)
# 6)
tab.sort()
print(tab)

slownik = {'a': 2, 4: 'ab', 1: 3}
print(slownik)
print(slownik[4])
slownik['klucz'] = 'wartosc'
print(slownik)
slownik.pop('klucz')
print(slownik)
print(slownik.keys())
print(slownik.values())

print('a=%(zm)d' % {'zm': 12})
napis = 'a={}, b={}'
print(napis.format(12, 12))

# if warunek:
    # instrukcja 1
    # instrukcja 2
# elif warunek 2:
    # instrukcja 1
    # instrukcja 2
# else:
    # instrukcja 1

# x = input('Podaj x: ')
# y = input('Podaj y: ')
#  print(x)
#  print(y)
#  print(type(x))
#  print(type(y))
# x = int(x)
# y = int(y)
#  print(type(x), type(y))
#  if x > y:
#      print(x)
#  elif x < y:
#      print(y)
#  else:
#      print('x = y')

# z = input('Podaj Z: ')
# q = input('Podaj Q: ')
# q = int(q)
# z = int(z)
#
# if (x > y) & (z > q):
#     print('x wieksze od y i z jest wieksze q')
# else:
#     print('x nie jest wieksze od y lub z nie jest wieksze od q')

# for element in sekwencja:
    # instrukcja 1
    # instrukcja 2
# else:
    # instrukcja 1
    # instrukcja 2

print('---')

for i in listy:
    print(i)

for j in range(0, len(listy)):
    print(listy[j])

# while warunek:
    # instrukcja 1
    # instrukcja 2
# else:
    # instrukcja

print('Pętla while')

licznik = 0
while licznik != len(listy):
    print(listy[licznik])
    licznik += 1

# licznik2 = 0
# k = int(input('Podaj k: '))
# while licznik2 != len(tab):
#     if k - tab[licznik2] == 0:
#         print('{} - {} = 0'.format(k, tab[licznik2]))
#         break
#     licznik2 += 1

licznik3 = 0
liczby = [1, 2, 2, 2, 4, 5, 6]

print('Zadanie ')

while licznik3 != len(liczby):
        while liczby[licznik3] == 2:
            liczby.pop(licznik3)
        licznik3 += 1
print(liczby)
import math
# 1
z1 = math.exp(10)
print(z1)
z2 = pow(math.log(5+pow(math.sin(8), 2)), (1/6))
print(z2)
z3 = math.floor(3.55)
print(z3)
z4 = math.ceil(4.80)
print(z4)
# 2
q1 = 'SEBASTIAN'
q2 = 'TYLICKI'
print(q1.capitalize())
print(q2.capitalize())
# 3
piosenka = 'la la la la afaf la f a sg grg sg sg se la la'
print(piosenka.count('la'))
# 4
list = 'Sebastian Tylicki'
print(list[0])
print(list[len(list)-1])

# 6
s = "jeden dwa trzy cztery"
s = str(s)
f = 12.73
f = float(f)
ab = 0x123ac
ab = hex(ab)
print(s)
print(f)
print(ab)

# 5
m = s.split()
print(m)
# 7
sporty1 = ['siatkowka', 'koszykowka', 'kolarstwo']
sporty2 = ['golf', 'football']
sporty1.reverse()
sporty1.extend(sporty2)
print(sporty1)
# 8
slownik = {'np':'na przyklad', 'itp':'i tym podobne','itd':'i tak dalej'}
# 9
slownikgry = {150 : 'LOL', 80 : 'Valorant', 367 : 'Cs Go', 479 : 'Warframe'}
count = 0
for key, value in slownikgry.items():
    count += 1
print(count)
# 10
zdanie = input('Podaj zdanie: ')
zd = zdanie.count('a')
print(zd)
# 11
a = input('Podaj a: ')
b = input('Podaj b: ')
c = input('Podaj c: ')
a = int(a)
b = int(b)
c = int(c)
if a >= b:
    if a >= c:
        print('a jest najwieksze')
elif b >= c:
    print('b jest najwieksze')
else:
    print('c jest najwieksze')

# 12
lll = [1, 2, 4.2, 6.1, 5, 1.2]
for i in lll:
    print(i*i)
# 13
zxv = []
count2 = 0
while count2 < 10:
    y = input('Podaj liczbe: ')
    y = int(y)
    count2 += 1
    x = y % 2
    if x == 0:
        zxv.insert(count2, y)
print(zxv)

import random
import math
# 1
A = [1-x for x in range(1, 11)]
print(A)
B = [4**i for i in range(8)]
print(B)
C = [x for x in B if x % 2 == 0]
print(C)
# 2
listy1 = random.sample(range(1, 3000), 10)
list = [i for i in listy1 if i % 2 == 0]
print(list)
# 3
slownik = {'mleko': 'litry', 'cukier': 'kg', 'chleb': 'sztuki', 'banany': 'sztuki'}
list2 = [i for i in slownik if slownik[i] == 'sztuki']
print(list2)
# 4
c = int(input("Wstaw najwiekszy bok: "))
b = int(input("Wstaw a: "))
a = int(input("Wstaw b: "))
def trojkat(a, b, c):
    c2 = pow(c, 2)
    b2 = pow(b, 2)
    a2 = pow(a, 2)
    if c2 == a2+b2:
        print('Trojkat jest prostokatny')
    else:
        print('Trojkat nie jest prostokatny')
trojkat(a, b, c)
# 5
def trapez(a = 9, b = 3, h = 3):
    pole = ((a+b)*h)/2
    print(pole)
trapez()
# 6
ls = []
def fun(a = 1, b = 4, ile = 10):
    for i in range(ile):
        print(a)
        a = a*b
fun()
# 7
def fun2(* ile):
    a = 1
    for i in ile:
        print(a)
        a = a*4
fun2(1,2,3,4,5,6,7,8,9,10)
# 8

# 9
x = int(input('Wstaw x: '))
try:
    print(math.sqrt(x))
except ValueError:
    print('x jest ujemny')

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

    import math as m

def zad1():
    x = m.pow((m.log(32, 2) + m.pi + m.sin(56)), (1/4))
    print(round(x, 2))

def zad2():
    lista = [10, 4, 2.5, 1.7, 8.1, 4.5, 1, 99, -1, -5.3]
    listaz = [i for i in lista if isinstance(i, int)]
    print(lista)
    print(listaz)

def zad3(slownik):
    lista = []
    x = 0
    for key in slownik:
        if isinstance(key, int):
            if isinstance(slownik[key], int):
                x = key + slownik[key]
                lista.append(x)
    print(lista)

def zad4():
    plik = open('tekst.txt', 'r+', encoding='utf-8')
    plik.seek(35)
    znaki = plik.read(27)
    x = 0
    for i in znaki:
        if i == " ":
            x = x + 1
    print(znaki)
    print(x)
    plik.close()

def zad5():
    a1 = input('Wstaw a1: ')
    n = input('Wstaw n: ')
    r = input('Wstaw r: ')
    try:
        a1 = int(a1)
        n = int(n)
        r = int(r)
        an = a1 + (n-1)*r
        print("N-ty wyraz ciągu wynosi: ", an)
        plik = open('zad5', 'w+')
        plik.write(str(an))
        plik.close()
    except ValueError:
        print("Wartości muszą być całowite")

slownik = {1 : 3, 4 : 1.5, 3.2 : 2, 1.2 : 9.9, 8 : 11}

zad1()
zad2()
zad3(slownik)
zad4()
zad5()

import numpy as np

# inicjalizacja tablic
a = np.array([[0, 1], [2, 3]])
print(a)
# drugi sposób
a = np.arange(2, 5, 0.1)
print(a)
# wypisywanie typu zmiennej
print(type(a))
# sprawdzenie typu danych tablicy
print(a.dtype)
# inicjalizacja tablicy z konkretnym typem danych
a = np.arange(2, dtype='int64')
print(a.dtype)
# zapisywanie kopii tablicy jako tablicy z innym typem
b = a.astype('float')
print(b)
print(b.dtype)
# wypisanie rozmiaru tablicy
print(b.shape)
# można też sprawdzić ilość wymiarów tablicy
print(a.ndim)
# stworzenie tablicy wielowmiarowej może wyglądać tak
# parametrem przekazywanym do funkcji array jest obiekt
# może to być Pythonowa lista
m = np.array([np.arange(2), np.arange(2)])
print(m.shape)
# ponownie typem jest ndarray
print(type(m))

zera = np.zeros((5, 5))
jedynki = np.ones((4, 4))
print(zera)
print(jedynki)
# domyślny typ danych
print(zera.dtype)
print(jedynki.dtype)
# można również stworzyć "pustą" macierz o podanych wymiarach
# wartości umieszczane są losowo
pusta = np.empty((2, 2))
print(pusta)

macierz = np.array([[12, 11], [2, 1]])
print(macierz)
# odwołanie do elementu
poz_1 = macierz[1, 1]
poz_2 = macierz[0][1]
print(poz_1)
print(poz_2)

liczby_lin = np.linspace(1, 2, 5, endpoint=False)
print(liczby_lin)
z = np.indices((5, 3))
print(z)
mat_diag = np.diag([a for a in range(5)])
print(mat_diag)
z = np.fromiter(range(5), dtype='int32')
print(z)

znaki = b'ogolna'
z1 = np.frombuffer(znaki, dtype='S1')
print(z1)
z2 = np.frombuffer(znaki, dtype='S2')
print(z2)
znaki = 'ogolna'
z3 = np.array(list(znaki))
z4 = np.array(list(znaki), dtype='S1')
z5 = np.array(list(b'ogolna'))
z6 = np.fromiter(znaki, dtype='S1')
print(z3)
print(z4)
print(z5)
print(z6)

a = np.arange(10)
print(a)
s = slice(2, 7, 2)
print(a[s])
s = range(2, 7, 2)
print(a[s])
print(a[2:7:2])
print(a[1:])
print(a[2:5])

mat = np.arange(25)
mat = mat.reshape((5, 5))
print(mat)
print(mat[1:]) # od 2 wiersza
print(mat[:, 1:2]) # 2 kolumna jako wektor
print(mat[:, -1]) # ostatania kolumna
print(mat[2:5, 1:3]) # 2 i 3 kolumna dla 3, 4, 5 wierszy
print(mat[:, [2, 4]]) # 3 i 5 kolumna
print('')

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print(y)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

# a = np.arange(0, 5, 0.2)

# plt.plot(a, a, 'r--', a, a**2, 'bs', a, a**3, 'g^')
# plt.legend(labels = ['liniowa','kwadratowa','sześcienna'], loc='center left')
# plt.show()

# plt.plot(a, a, 'r--', label='liniowa')
# plt.plot(a, a**2, 'bs', label='kwadratowa')
# plt.plot(a, a**3, 'g^', label='sześcienna')
# plt.ylabel('etykieta y')
# plt.xlabel('etykieta x')
# plt.title('tytuł')
# plt.legend()
# plt.savefig('wykres1.png')
# plt.show()
# x = np.arange(0, 10.1, 0.1)
# y = np.sin(x)
# plt.plot(x, y, 'b-')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('t')
# plt.show()

# data = {'a': np.arange(50), 'c': np.random.randint(0, 50, 50),'d': np.random.randn(50)}
# data['b'] = data['a']+10*np.random.randn(50)
# data['d']= np.abs(data['d'])*100
# plt.scatter('a','b',c='c',s='d', data=data, cmap='magma')
# plt.xlabel('wartosci a')
# plt.ylabel('wartosci b')
# plt.show()
#
# x1 = np.arange(0, 2, 0.02)
# x2 = np.arange(0, 2, 0.02)
#
# y1 = np.sin(2*np.pi * x1)
# y2 = np.cos(2*np.pi * x2)
# plt.subplot(4,1,1)
# plt.plot(x1, y1)
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Sin(x)')
#
# plt.subplot(4,1,4)
# plt.plot(x2, y2, 'r')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.title('Cos(x)')
# plt.subplots_adjust(hspace=0.5)
# plt.show()

# fig, axs = plt.subplots(3, 2)
# axs[0, 0].plot(x1, x2, 'g-')
# axs[0, 0].set_xlable('x')
# axs[0, 0].set_ylable('sin(x)')
# axs[0, 0].set_title('Wykres sin(x)')
# plt.show()

data = {'Kraj': ['Belgia','Indie','Brazylia','Polska'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia','Warszawa'],
        'Kontynent': ['Europa','Azja', 'Ameryka Południowa','Europa'],
        'Populacja': [11190846, 1303171035, 207847528, 38675467]}
df = pd.DataFrame(data)
print(df)
grupa = df.groupby('Kontynent')
etykiety = list(grupa.groups.keys())
wartosc = list(grupa.agg('Populacja').sum())
plt.bar(etykiety, wartosc, color=['yellow','green','red'])
plt.xlabel('Kontynent')
plt.ylabel('Populacja w mld')
plt.show()


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
from PIL import Image
import seaborn as sns

# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
#
# df = pd.DataFrame(ts,columns=['wartosc'])
# print(df)
# df['Srednia krocząca'] = df.rolling(window=50).mean()
# df.plot()
# plt.legend()
# plt.show()
#
# x = np.random.randn(10000)
# plt.hist(x, bins=50, facecolor='g', alpha=0.75, density=True)
# plt.xlabel('Wartości')
# plt.ylabel('Prawdopodobieństwo')
# plt.title('Histogram')
# plt.grid()
# plt.show()

# df = pd.read_csv('dane.csv', header=0, sep=";", decimal=".")
# print(df)
# seria = df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
#
# wedges, texts, autotext = plt.pie(x=seria, labels=seria.index,
#                                   autopct=lambda pct:"{:.1f}%".format(pct),
#                                   textprops=dict(color="black"),
#                                   colors=['red','green'])
# plt.title('Suma zamówień dla sprzedawców')
# plt.legend(loc='lower right')
# plt.ylabel('Procentowy wynik wartości zamówienia')
# plt.show()

# sns.set(rc={'figure.figsize':(8,8)})
# sns.lineplot(x=[1, 2, 3, 4], y=[1,4,9,16], label='linia nr',
#             color='red', marker='o',linestyle=':')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()


sns.set()
# s = pd.Series(np.random.randn(1000))
# s - s.cumsum()
# wykres = sns.relplot(kind='line',data=s, label='dane z serii')
# wykres.fig.set_size_inches(8, 6)
# wykres.fig.suptitle('Wykres liniowy')
# wykres.set_xlabels('indeksy')
# wykres.set_ylabels('wartosci')
# wykres.add_legend('Wykres liniowy')
# plt.show()


# df = pd.read_csv('iris.data',header=0, sep=',',decimal='.')
# print(df)
# sns.lineplot(data=df, x=df.index, y='sepal length', hue='class', palette=['yellow','green','red'])
# plt.xlabel('indeksy')
# plt.title('Wykres liniowy danych z Iris database')
# plt.show()


# data = {'a': np.arange(10), 'c': np.random.randint(0, 50, 10), 'd': np.random.randn(10)}
# data['b'] = data['a'] + 10 * np.random.randn(10)
# data['d'] = np.abs(data['d']) * 100
# df = pd.DataFrame(data)
# plot = sns.relplot(data=df, x='a', y='b', hue='c',palette='bright', size='d', legend=True)
# plot.set(xticks=data['a'])
# plt.show()

data = {'Kraj': ['Belgia','Indie','Brazylia','Polska'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia','Warszawa'],
        'Kontynent': ['Europa','Azja', 'Ameryka Południowa','Europa'],
        'Populacja': [11190846, 1303171035, 207847528, 38675467]}
df = pd.DataFrame(data)
plot = sns.barplot(data=df, x='Kontynent', y='Populacja',
                   hue='Kontynent', estimator=np.sum, errorbar=None,
                   dodge=False, palette='plasma')
plot.legend(title='Populacja na kontynentach')
plot.set(title='Wykres słupkowy')
plt.show()
