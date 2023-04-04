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