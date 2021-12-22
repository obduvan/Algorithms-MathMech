array_doors = []
set_doors = set()


def get_door_price(door: int) -> int:
    # print(door)
    # print(door_price)
    return int(door_price[door - 1])

with open('in.txt', 'r') as f:
    rooms_number, doors_number, woke_room, money = map(int, f.readline().split())
    for i in range(rooms_number):
        inp = set(f.readline().split()[1::])
        array_doors.append(inp)

    door_price = ''.join(f.readlines()).split()

woke_room -= 1
out_rooms = {}
graph = [[0 for j in range(rooms_number)] for i in range(rooms_number)]
graph_weight = [10 ** 6 for j in range(rooms_number)]
out_doors = set()
visited_doors = set()

for i in range(len(array_doors)):
    out_doors = array_doors[i]
    for x in range(i + 1, len(array_doors)):
        cross_door = array_doors[i] & array_doors[x]
        if len(cross_door) > 0:
            cross_door = cross_door.pop()
            out_doors.remove(cross_door)
            cross_door_price = get_door_price(int(cross_door))
            graph[i][x] = int(cross_door)
            graph[x][i] = int(cross_door)
            visited_doors.add(cross_door)

    for out_door in out_doors:
        if out_door not in visited_doors:
            out_rooms.update({i: (out_door, get_door_price(int(out_door)))})


def get_next_room():
    min_e = 10 ** 6
    next_rr = -1
    for i in range(rooms_number):
        if i not in visited:
            weight = graph_weight[i]
            if weight < min_e:
                min_e = weight
                next_rr = i
    return next_rr


pred = {}

min_edge = 10 ** 6
result = {}

graph_weight[woke_room] = 0
visited = set()
pred[woke_room] = woke_room

next_room = woke_room
while len(visited) != rooms_number:
    visited.add(next_room)
    if next_room in out_rooms:
        result.update({next_room: out_rooms[next_room][1]})

    for v in range(len(graph[next_room])):
        # print(v, next_room)
        door = graph[next_room][v]
        if v not in visited and v != next_room and door != 0:
            price_door = get_door_price(door)
            if price_door + graph_weight[next_room] < graph_weight[v]:
                graph_weight[v] = price_door + graph_weight[next_room]
                pred.update({v: next_room})

    next_room = get_next_room()

# print(graph_weight)
# print(pred)
#
# print(out_rooms)
# print(result)

min_res_sum = 10 ** 7
res_sum = 0
min_v = 0

for res_v in result:
    res_sum = result[res_v] + graph_weight[res_v]
    if res_sum < min_res_sum:
        min_v = res_v
        min_res_sum = res_sum

# print(min_res_sum)

finish = min_v
res_path = [out_rooms[min_v][0]]

while finish != woke_room:
    pred_finish = pred[finish]
    res_path.append(str(graph[finish][pred_finish]))
    finish = pred_finish

with open("out.txt", "w") as ff:
    result_answer = 'Y'
    if min_res_sum > money:
        result_answer = 'N'
        ff.write(result_answer)
    else:
        ff.write(f'{result_answer}\n', )
        ff.write(f'{min_res_sum}\n')
        ff.write(' '.join(reversed(res_path)))
