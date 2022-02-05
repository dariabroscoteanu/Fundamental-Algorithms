# Se dă un graf neorientat conex cu n>3 vârfuri și m>n muchii. Să se afișeze punctele critice în
# care sunt incidente muchii critice. Pentru fiecare astfel de punct se va afișa numărul de
# muchii critice care sunt incidente în el și numărul de componente biconexe care îl conțin, fără
# a memora componentele biconexe ale grafului și fără a memora muchiile critice.
# Complexitate O(m)
# Informațiile despre graf se citesc din fișierul graf.in cu structura:

f = open("graf.in")
line = f.readline()
v = line.split()
n = int(v[0])
m = int(v[1])


def citire_matrice_liste(noduri,muchii,orientat):
    l = {}
    for i in range(1, noduri + 1):
        l[i] = []

    for i in range(muchii):
        line = f.readline()
        v = line.split()
        x, y = v
        x = int(x)
        y = int(y)
        if orientat:
            l[x].append(y)
        else:
            l[x].append(y)
            l[y].append(x)
    return l


lista = citire_matrice_liste(n, m, 0)
f.close()
puncte_critice = [False] * (n + 1)
vizitat = [0] * (n + 1)
discovery_time = [float("Inf")] * (n + 1)
low = [float("Inf")] * (n + 1)
parent = [-1] * (n + 1)
time = 0


def DFS(nod):
    global lista, vizitat, discovery_time, low, muchii_critice, parent, time

    vizitat[nod] = 1
    discovery_time[nod] = time
    low[nod] = time
    time += 1
    copii = 0

    for vecin in lista[nod]:
        if vizitat[vecin] == 0:
            parent[vecin] = nod
            copii += 1
            DFS(vecin)
            low[nod] = min(low[nod], low[vecin])
            if parent[nod] == -1 and copii > 1:
                puncte_critice[nod] = True
            if low[vecin] >= discovery_time[nod] and parent[nod] != -1:
                puncte_critice[nod] = True
        elif vecin != parent[nod]:
            low[nod] = min(low[nod], discovery_time[vecin])


for nod in range(1, n + 1):
    if vizitat[nod] == 0:
        DFS(nod)



puncte = [0] * (n + 1)
vizitat = [0] * (n + 1)
discovery_time = [float("Inf")] * (n + 1)
low = [float("Inf")] * (n + 1)
parent = [-1] * (n + 1)
time = 0


def DFS_muchii(nod):
    global lista, vizitat, discovery_time, low, muchii_critice, parent, time

    vizitat[nod] = 1
    discovery_time[nod] = time
    low[nod] = time
    time += 1

    for vecin in lista[nod]:
        if vizitat[vecin] == 0:
            parent[vecin] = nod
            DFS_muchii(vecin)
            low[nod] = min(low[nod], low[vecin])
            if low[vecin] > discovery_time[nod]:
                if puncte_critice[vecin]:
                    puncte[vecin] += 1
                if puncte_critice[nod]:
                    puncte[nod] += 1
        elif vecin != parent[nod]:
            low[nod] = min(low[nod], discovery_time[vecin])



for i in range(1, n + 1):
    if vizitat[i] == 0:
        DFS_muchii(i)

for i in range(1, n + 1):
    if puncte[i]:
        print(f"{i}: incidente cu {puncte[i]} muchii critice")