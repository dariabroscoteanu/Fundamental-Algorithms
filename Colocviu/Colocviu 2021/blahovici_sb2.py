# Se citesc informații despre un graf orientat fără circuite G din fișierul graf.in.
# Fișierul are următoarea structură:
# - Pe prima linie sunt două numere reprezentând numărul de vârfuri n (n>4) și numărul de arce
# m ale grafului, m>=n
# - Pe următoarele m linii sunt câte 3 numere întregi reprezentând extremitatea inițială,
# extremitatea finală și costul unui arc din graf (costul unui arc poate fi și negativ).
# - Pe ultima linie sunt două noduri sursa s1 și s2
# a) Să se determine dacă există un vârf din graf v egal depărtat de s1 și s2: d(s1,v)=d(s2,v).
# Dacă există mai multe astfel de vârfuri se va afișa cel mai apropiat de cele două surse
# (cel cu d(s1,v) cea mai mică). Complexitate O(m)
# b) Pentru vârful v determinat la a) (dacă există) să se determine dacă există mai multe
# drumuri minime de la s1 la v. Daca exista doar unul, se va afișa acest drum, dacă nu se
# vor afișa două dintre drumurile minime de la s la v1 Complexitate O(m)

from queue import Queue

f = open("blahovici.in")
line = f.readline()
v = line.split()
n = int(v[0])
m = int(v[1])
grad1 = [0] * (n + 1)
grad2 = [0] * (n + 1)

lista = [[] for i in range(n + 1)]

for i in range(1, m + 1):
    line = f.readline()
    v = line.split()
    x = int(v[0])
    y = int(v[1])
    cost = int(v[2])
    lista[x].append((y, cost))
    grad1[y] += 1
    grad2[y] += 1

line = f.readline()
v = line.split()
nod1 = int(v[0])
nod2 = int(v[1])
f.close()
sortate1 = []
sortate2 = []
coada1 = Queue()
coada2 = Queue()
for i in range(1, n + 1):
    if grad1[i] == 0:
        coada1.put(i)
        sortate1.append(i)
        coada2.put(i)
        sortate2.append(i)


def distanta(nod1, coada, sortate, grad):
    dist = [float("infinity") for x in range(n + 1)]
    dist[nod1] = 0
    nr = [0 for i in range(n + 1)]
    nr [nod1] = 0
    while not coada.empty():
        nod = coada.get()
        for (vecin, cost) in lista[nod]:
            grad[vecin] -= 1
            if grad[vecin] == 0:
                coada.put(vecin)
                sortate.append(vecin)
            if dist[vecin] > dist[nod] + cost:
                dist[vecin] = dist[nod] + cost
                nr[vecin] = 1
            elif dist[vecin] == dist[nod] + cost:
                nr[vecin] += 1

    return dist, nr


d1, nr1 = distanta(nod1, coada1, sortate1, grad1)
d2, nr2 = distanta(nod2, coada2, sortate2, grad2)
print(d1)
print(d2)
v = -1
nr = 0
for nod in range(1, n + 1):
    if d1[nod] == d2[nod]:
        v = nod
        nr = nr1[nod]

print(v)
print(nr)
