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