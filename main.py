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
