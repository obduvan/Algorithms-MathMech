#Алгоритм Борувки-Краскла

NAME, SIZE, NEXT, NUM_V, V_NUM, T = {}, {}, {}, {}, {}, []


def read_data() -> int:
    with open('in.txt', 'r') as f:
        N = int(f.readline())
        for i in range(N):
            a, b = map(int, f.readline().split())
            NAME[(a, b)] = (a, b)
            NUM_V[i] = (a, b)
            V_NUM[(a, b)] = i
            SIZE[(a, b)] = 1
            NEXT[(a, b)] = (a, b)
    return N


def get_distance(a: tuple, b: tuple) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_sorted_arr(NAME: dict):
    sorted_arr = []
    vertexs = list(NAME.keys())

    for x in range(len(vertexs)):
        for y in range(x + 1, len(vertexs)):
            v1, v2 = vertexs[x], vertexs[y]
            sorted_arr.append((v1, v2, get_distance(v1, v2)))

    sorted_arr = sorted(sorted_arr, key=lambda _: _[2])
    return sorted_arr


def main(N: int) -> int:
    common_weight = 0
    sorted_arr = get_sorted_arr(NAME)
    while len(T) != N - 1:
        v, w, weight = sorted_arr.pop(0)
        p = NAME[v]
        q = NAME[w]
        if p != q:
            if SIZE[p] > SIZE[q]:
                connect(v=v, w=w, p=p, q=q)
            else:
                connect(v=w, w=v, p=q, q=p)
            common_weight += weight
            T.append((v, w, weight))

    return common_weight


def connect(v: (int, int), w: (int, int), p: (int, int), q: (int, int)):
    NAME[w] = p
    u = NEXT[w]
    while NAME[u] != p:
        NAME[u] = p
        u = NEXT[u]

    SIZE[p] += SIZE[q]
    NEXT[v], NEXT[w] = NEXT[w], NEXT[v]


def get_neigh(vertex) -> list:
    neighbors = []
    for el in T:
        if vertex == el[1]:
            neighbors.append(V_NUM[el[0]] + 1)
        elif vertex == el[0]:
            neighbors.append(V_NUM[el[1]] + 1)
    neighbors.sort()

    return list(map(str, neighbors))


def write_data(common_weight: int, N: int):
    with open("out.txt", "w") as f:
        for i in range(N):
            vertex = NUM_V[i]
            neighbors = get_neigh(vertex)
            f.write(f"{str(i + 1)}: {' '.join(neighbors)} 0 \n")

        f.write(str(common_weight))


if __name__ == "__main__":
    N = read_data()
    common_weight = main(N)
    write_data(common_weight, N)
