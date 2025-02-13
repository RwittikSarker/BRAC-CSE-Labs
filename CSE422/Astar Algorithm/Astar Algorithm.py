graph = {}
heuristic = {}
with open("InputFile.txt", "r") as file:
    line = file.readline()
    while line:
        list1 = line.split(" ")
        heuristic[list1[0]] = int(list1[1])
        graph[list1[0]] = {}
        for i in range(2, len(list1)-1, 2):
            graph[list1[0]][list1[i]] = int(list1[i+1])
        line = file.readline()

flag = True

def astar(graph, heuristic, start, goal, flag):
    open_list = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]

    while open_list:
        current_f, current_node = min(open_list, key=lambda x: x[0])
        open_list.remove((current_f, current_node))

        if current_node == goal:
            distance = g_score[current_node]
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1], distance

        for neighbor, cost in graph[current_node].items():
            tentative_g_score = g_score[current_node] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic[neighbor]
                open_list.append((f_score[neighbor], neighbor))

    flag = False
    print("NO PATH FOUND")
    return 0, 0

path, distance = astar(graph, heuristic, 'Arad', 'Bucharest', flag)
if flag == True:
    print("Path:", end=" ")
    for i in range(len(path)):
        if i == len(path) - 1:
            print(path[i])
        else:
            print(f"{path[i]} ->", end=" ")
    print(f"Total distance: {distance} km")