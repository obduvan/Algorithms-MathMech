def get_nextNode():
    minn = 10 ** 6
    res_node = -1
    for vertex in dump:
        for x in range(len(WEIGHTS[vertex])):
            weight_node = WEIGHTS[vertex][x]
            node = x
            if weight_node is not None and node not in dump and minn > weight_node:
                minn = weight_node
                res_node = node

    return res_node


def get_answer(nextNode):
    while nextNode != finish:
        for neighbor in GRAPH[nextNode]:
            v = neighbor[0]
            w = neighbor[1]
            if D[v] > max(D[nextNode], w):
                D[v] = max(D[nextNode], w)
                PRED.update({v: nextNode})

        dump.append(nextNode)
        nextNode = get_nextNode()


def read_file() -> (int, list):
    a = []
    with open('in.txt', 'r') as f:
        while True:
            n = f.readline()
            n = n.strip()
            b = []
            for el in n.split():
                b.append(int(el))
            if len(b) > 0:
                a.append(b)
            if not n:
                break
    return a


inputs_line = read_file()

n = inputs_line[0][0]

GRAPH = {i: [] for i in range(n + 1)}
PRED = {}
D = {i: 1000 for i in range(n + 1)}
WEIGHTS = [[None] * (n + 1) for i in range(n + 1)]

for line, i in zip(inputs_line[1::], range(n)):
    if len(line) > 1:
        for x in range(len(line)):
            if x % 2 == 0:
                if line[x] == 0:
                    break
            else:
                GRAPH[line[x - 1]].append((i + 1, line[x]))
for x in GRAPH:
    for el in GRAPH[x]:
        y = el[0]
        w = el[1]
        WEIGHTS[x][y] = w

start = inputs_line[n + 1][0]
finish = inputs_line[n + 2][0]
dump = []
nextNode = start
D[start] = -1

print(GRAPH)
get_answer(nextNode)


def print_answer():
    node = finish
    answer = [finish]
    with open("out.txt", "w") as f:

        if finish not in PRED:
            f.write("N")
        else:
            while start != node:
                node = PRED.get(node)
                answer.append(node)

            answer.reverse()
            f.write("Y\n")
            for el in answer:
                f.write(f"{el} ")
            f.write("\n")
            f.write(f"{D.get(finish)}")
            exit()


print_answer()
print(PRED)
print(GRAPH)
print(D)
