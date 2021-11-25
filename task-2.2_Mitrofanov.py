import collections

graph_1 = {}
parent = {}
uv_c = 1
visited = []
edge_f = {}
result = []

# graph_2 = {'1': ['5', '6', '8'],
#            '2': ['5', '6', '7'],
#            '3': ['8', '9'],
#            '4': ['6'],
#            's': ['1', '2', '3', '4'],
#            '5': ['1', '2', 't'],
#            '6': ['1', '2', '4', 't'],
#            '7': ['2', 't'],
#            '8': ['1', '3', 't'],
#            '9': ['3', 't']}


def read_data():
    with open('in.txt', 'r') as f:
        K, L = map(int, f.readline().split())
        graph_1 = {'s': [str(i) for i in range(1, K + 1)]}
        for i in graph_1['s']:
            edge_f['s' + i] = 0
        for i in range(K):
            inplist = f.readline().split()
            graph_1[str(i + 1)] = inplist
            for v in inplist:
                if v not in graph_1:
                    graph_1[v] = []
                graph_1[v].append(str(i+1))
                edge_f[str(i+1)+v] = 0

        for i in range(L):
            if str(i + 1 + K) not in graph_1:
                    graph_1[str(i + 1 + K)] = []
            graph_1[str(i + 1 + K)].append('t')
            edge_f[str(i+1+K)+'t'] = 0

    return K, graph_1


def change_f(hp, s, f):
    if s+f in edge_f:
        edge_f[s + f] += hp
    else:
        edge_f[f+s] -= hp


def is_not_nul(s, f):
    if s+f in edge_f:
        hp = 1 - edge_f[s + f]
        return hp > 0, hp
    else:
        hp = edge_f[f + s]
        return hp > 0, hp


def has_st(start, end, graph_1):
    queue = collections.deque([start])
    parent.clear()

    hp = 10 ** 8
    visited = [start]
    while queue:
        vertex = queue.pop()
        for neighboor in graph_1[vertex]:
            res, hp_new = is_not_nul(vertex, neighboor)
            if res and neighboor not in visited:
                queue.append(neighboor)
                parent[neighboor] = vertex
                visited.append(neighboor)

                hp = min(hp, hp_new)

                if neighboor == end:
                    return True, hp
    return False, hp


def start(graph_1):

    while True:
        tr, hp = has_st('s', 't', graph_1)
        if not tr:
            break
        else:
            s = 't'
            while s != 's':
                vertex = parent[s]
                change_f(hp, vertex, s)
                s = vertex
    for i in edge_f:
        if edge_f[i] != 0 and 's' not in i and 't' not in i:
            result.append(i)


def write_data(k):
    res = []
    with open("out.txt", "w") as ff:
        for i in range(1, k + 1):
            f = False
            for el in result:
                if str(i) in el:
                    res.append(el.replace(str(i), ""))
                    f = True
            if not f:
                res.append('0')
        ff.write(' '.join(res))


if __name__ == "__main__":
    k, graph_1 = read_data()
    start(graph_1)
    write_data(k)
