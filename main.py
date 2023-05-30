
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
