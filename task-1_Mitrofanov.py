import collections


x_cord = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
rev_x_cord = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
commands_k = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
commands_p = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def insert_prev(neighbour, vertex):
    neighbour = transform_cord(rev_x_cord, neighbour, 1)
    vertex = transform_cord(rev_x_cord, vertex, 1)
    prev.update({neighbour: vertex})


def get_neighbors(x, y, commands):
    neighbors = []
    for command in commands:
        new_x, new_y = x + command[0], y + command[1]
        if -1 < new_x < 8 and -1 < new_y < 8:
            neighbors.append((new_x, new_y))
    return neighbors


def exists_king_way(np_x, np_y, nk_x, nk_y):
    visited = [(nk_x, nk_y)]
    queue = collections.deque([(nk_x, nk_y)])

    while queue:
        vertex = queue.popleft()
        for neighbour in get_neighbors(vertex[0], vertex[1], commands_k):
            if neighbour not in visited and neighbour not in died_zone:
                visited.append(neighbour)
                queue.append(neighbour)
                insert_prev(neighbour, vertex)
                if neighbour == (np_x, np_y):
                    return True
    return False


transform_cord = lambda dict, edge, un: (dict[edge[0]], int(edge[1]) + un)


a = []
filepath = input()
with open(filepath, "r") as file:
    for line in file.readlines():
        a.append(line.strip())

k_x, k_y = list(a[0])
p_x, p_y = list(a[1])
k_y, p_y = int(k_y), int(p_y)
nk_x, nk_y = transform_cord(x_cord, (k_x, k_y), -1)
np_x, np_y = transform_cord(x_cord, (p_x, p_y), -1)
prev = {(k_x, k_y): -1}
died_zone = get_neighbors(np_x, np_y, commands_p)

answer = []
if exists_king_way(np_x, np_y, nk_x, nk_y,):
    last = prev[(p_x, p_y)]
    answer.append((p_x, p_y))
    answer.append(last)
    while last != (k_x, k_y):
        last = prev[last]
        answer.append(last)
    answer.reverse()

    with open("result.txt", "w") as f:
        for el in answer:
            # print("{0}{1}".format(el[0], el[1]))
            f.writelines("{0}{1}\n".format(el[0], el[1]))

else:
    with open("result.txt", "w") as f:
        # print("Маршрута не существует")
        f.write("Маршрута не существует")
