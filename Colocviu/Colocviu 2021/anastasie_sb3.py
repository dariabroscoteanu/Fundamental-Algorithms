
f = open("intrare.in")
line = f.readline()
v = line.split()
n = int(v[0])
m = int(v[1])

line = f.readline()
v = line.split()
sursa = []
for x in v:
    y = int(x)
    sursa.append(y)


line = f.readline()
v = line.split()
destinatie = []
for x in v:
    y = int(x)
    destinatie.append(y)


line = f.readline()
v = line.split()
k = int(v[0])
# sursa = 2n + 1
# destinatie = 2n + 2
# x1 .. xn = 1 .. n
# y1 .. yn = n+1 .. 2n
s = 2 * n + 1
t = 2 * n + 2

g = open("creare_retea.in", mode='w')
g.write(f"{2 * n + 2} { k + 2 * m}\n")

for i in range(1, m + 1):
    g.write(f"{s} {i} {sursa[i - 1]}\n")

for i in range(n + 1, 2 * n + 1):
    g.write(f"{i} {t} {destinatie[i - n - 1]}\n")

for i in range(k):
    line = f.readline()
    v = line.split()
    x, y, cost = int(v[0]), int(v[1]), int(v[2])
    g.write(f"{x} {y} {cost}\n")
g.close()
f.close()


def create_graph():
    f = open("creare_retea.in")

    line = f.readline()
    v = line.split()
    n = int(v[0])
    m = int(v[1])
    graph = [[0 for i in range(n + 1)] for j in range(n + 1)]
    initial_graph = [[0 for i in range(n + 1)] for j in range(n + 1)]
    for i in range(m):
        line = f.readline()
        v = line.split()
        x = int(v[0])
        y = int(v[1])
        cost = int(v[2])
        graph[x][y] = cost
        initial_graph[x][y] = cost
    f.close()

    for i in range(1, n + 1):
        for j in range (1, n + 1):
            print(f"{graph[i][j]} ", end=" ")
        print()

    return graph, initial_graph, n


graph, initial_graph, n = create_graph()


def BFS(s, t, graph, parent):
    vizitat = [False] * (n + 1)
    coada = []
    coada.append(s)
    vizitat[s] = True

    while len(coada):
        nod = coada.pop(0)
        for vecin, cost in enumerate(graph[nod]):
            if vizitat[vecin] == False and cost > 0:
                coada.append(vecin)
                vizitat[vecin] = True
                parent[vecin] = nod
                if vecin == t:
                    return True

    return False


def FordFulkerson(source, sink):
    global graph
    parent = [-1] * (n + 1)
    max_flow = 0
    while BFS(source, sink, graph, parent):
        path_flow = float("infinity")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow


source = n - 1
sink = n
max_flow = FordFulkerson(source, sink)
print(max_flow)

if max_flow != sum(destinatie):
    print("Nu exista")
else:
    for i in range(1, n):
        if i != source:
            for j in range(1, n):
                if initial_graph[i][j] != 0:
                    if initial_graph[i][j] != graph[i][j]:
                        print(f"{i} {j} {initial_graph[i][j] - graph[i][j]}")
