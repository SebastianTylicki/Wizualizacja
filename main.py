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
