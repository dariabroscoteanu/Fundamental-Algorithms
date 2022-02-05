# ALgoritmul lui Dijkstra pentru determinarea distantelor de la un nod la celelalte noduri.
import heapq


f = open("graf.in")

line = f.readline()
v = line.split()
n = int(v[0])
m = int(v[1])


def citire(noduri, muchii, orientat):
    lista = dict()
    matrice = [[0 for j in range(n + 1)] for i in range(n + 1)]
    for i in range(1, noduri + 1):
        lista[i] = dict()

    for i in range(muchii):
        line = f.readline()
        v = line.split()
        x = int(v[0])
        y = int(v[1])
        cost = int(v[2])
        if orientat:
            lista[x][y] = cost
            matrice[x][y] = cost
        else:
            lista[x][y] = cost
            matrice[x][y] = cost
            lista[y][x] = cost
            matrice[y][x] = cost

    return lista, matrice


lista, matrice = citire(n, m, 1)
line = f.readline()
v = line.split()
buget = int(v[0])
line = f.readline()
v = line.split()
sursa = int(v[0])


def dijkstra(lista, start):
    distante = [float("infinity")] * (n + 1)
    tata = [0] * (n + 1)
    vizitat = [0] * (n + 1)
    distante[start] = 0
    vizitat[start] = 1
    heap = [(0, start)]
    heapq.heapify(heap)
    while len(heap) > 0:
        dist, nod = heapq.heappop(heap)
        if dist <= distante[nod]:
            for vecin, cost in lista[nod].items():
                if dist + cost <= distante[vecin] and vizitat[vecin] == 0:
                    distante[vecin] = dist + cost
                    vizitat[vecin] = 1
                    heapq.heappush(heap, (dist + cost, vecin))
                    tata[vecin] = nod

    return distante, tata


distante, tata = dijkstra(lista, sursa)
ma = -1
nod = -1
for i in range(1, n + 1):
    if distante[i] != float("infinity") and distante[i] > ma and distante[i] <= buget:
        ma = distante[i]
        nod = i
print("a)")
print(f"v = {nod}")
parcurg = []


def afis(nod):
    global parcurg
    if nod != 0:
        parcurg.append(nod)
        afis(tata[nod])


afis(nod)
parcurg.reverse()
print(*parcurg)

# b)
maxim_b = -1
nod_b = -1
for vecin in range(1, n + 1):
    cost = matrice[vecin][nod]
    if cost > 0 and distante[vecin] + cost <= buget and distante[vecin] + cost > maxim_b:
        maxim_b = distante[vecin] + cost
        nod_b = vecin

print("b)")
parcurg = []
afis(nod_b)
parcurg.reverse()
parcurg.append(sursa)
print(*parcurg)