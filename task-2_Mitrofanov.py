import collections


def read_file() -> (int, list):
    with open('in.txt', 'r') as f:
        n = int(f.readline())
        matrix = [[int(num) for num in line.split()] for line in f]
    return n, matrix


def matrix_to_dict(matrix: list, n: int) -> dict:
    graph = collections.defaultdict(set)
    for vertex in range(n):
        for a in range(n):
            if matrix[a][vertex] == 1 or matrix[vertex][a] == 1:
                graph[vertex].add(a)
    return graph


def print_answer(survivors, last_vert):
    f_ind = survivors.index(last_vert)
    answer_list = survivors[f_ind::]
    answer_list = list(map(lambda x: x + 1, answer_list))
    with open("out.txt", "w") as f:
        for el in answer_list:
            f.writelines(f"{el} ")
    exit()


def dfs(current_vertex, prev_vertex):
    visited.add(current_vertex)
    # print(current_vertex, prev_vertex)
    survivors.append(current_vertex)
    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            dfs(neighbor, current_vertex)
        elif neighbor != prev_vertex:
            print_answer(survivors, neighbor)
    survivors.pop()


def main():
    global graph, visited, survivors
    n, matrix = read_file()
    graph = matrix_to_dict(matrix, n)
    visited = set()
    survivors = []
    dfs(0, -1)


if __name__ == '__main__':
    main()
