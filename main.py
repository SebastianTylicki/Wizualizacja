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