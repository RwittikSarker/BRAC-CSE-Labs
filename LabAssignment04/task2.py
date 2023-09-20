input1 = open("input2.txt","r")
output1 = open("output2.txt","w")
temp = [int(i) for i in input1.readline().split(" ")]
n = temp[0]
m = temp[1]
graph = {}
for i in range(n+1):
    graph[i] = []
for i in range(m):
    list1 = input1.readline().split(" ")
    graph[int(list1[0])].append(int(list1[1]))
color = [0]*(n+1)

def BFS(graph,vertex,color):
    q = []
    color[vertex] = 1
    q.append(vertex)
    while q != []:
        node = q.pop(0)
        output1.writelines(f"{node} ")
        for i in graph[node]:
            if color[i] == 0:
                color[i] = 1    
                q.append(i)

BFS(graph,1,color)
input1.close()
output1.close()