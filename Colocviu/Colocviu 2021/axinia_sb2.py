# Se citesc informații despre un graf orientat ponderat G din fișierul graf.in. Fișierul are
# următoarea structură:
# - pe prima linie sunt două numere reprezentând numărul de vârfuri n (n>4) și numărul de arce
# m ale grafului, m>n
# - pe următoarele m linii sunt câte 3 numere întregi pozitive reprezentând extremitatea inițială,
# extremitatea finală și costul unui arc din graf
# - pe următoarea linie (a (m+2)-a linie) din fișier este un număr natural k (0<k<n)
# reprezentând numărul de vârfuri sursă; vârfurile sursă din G vor fi 1, 2, ... , k
# - pe ultima linie a fișierului sunt două vârfuri t1 și t2, reprezentând vârfurile destinație ale
# grafului.
# Notăm cu S ={1,…,k} mulțimea vârfurilor sursă din G și cu T={t1,t2} mulțimea vârfurilor
# destinație din G. Spunem că un vârf y este accesibil din x în G dacă există un drum de la x la
# y. Presupunem că există cel puțin un vârf destinație care este accesibil dintr-un vârf sursă.
# Să se determine distanța între cele două mulțimi:
# d(S, T) = min {d(x, y) | x ∈ S, y ∈ T}
# Să se determine în plus și o pereche de vârfuri (s,t) cu sS și tT cu
# d(s,t) = d(S,T) = min {d(x, y) | x ∈ S, y ∈ T}
import heapq

f = open("graf_subiect2.in")
line = f.readline()
v = line.split()
n = int(v[0])
m = int(v[1])
graph = [[] for i in range(n + 1)]
for i in range(m):
    line = f.readline()
    v = line.split()
    x = int(v[0])
    y = int(v[1])
    cost = int(v[2])
    graph[x].append((y, cost))

line = f.readline()
v = line.split()
k = int(v[0])
heap = []
distante = [float("infinity")] * (n + 1)
tata = [0] * (n + 1)

for i in range(1, k + 1):
    heap.append((0, i))
    distante[i] = 0

line = f.readline()
v = line.split()
t1 = int(v[0])
t2 = int(v[1])

f.close()
heapq.heapify(heap)
while len(heap) > 0:
    dist, nod = heapq.heappop(heap)
    if dist <= distante[nod]:
        for vecin, cost in graph[nod]:
            if dist + cost <= distante[vecin]:
                distante[vecin] = dist + cost
                tata[vecin] = nod
                heapq.heappush(heap, (dist + cost, vecin))

mi = min(distante[t1], distante[t2])
if distante[t1] == mi:
    nod = t1
else:
    nod = t2
print(f"Distanta minima intre multimi = {mi}")
drum = []
while nod != 0:
    drum.append(nod)
    nod = tata[nod]

nod1 = drum[len(drum) - 1]
nod2 = drum[0]
drum.reverse()
print(f"s = {nod1} t = {nod2}")
print(f"drum minim: {drum}")


