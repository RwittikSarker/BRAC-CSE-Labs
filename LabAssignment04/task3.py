input1 = open("input3.txt","r")
output1 = open("output3.txt","w")
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

def DFS(graph,vertex,color):
    color[vertex] = 1
    output1.writelines(f"{vertex} ")
    for i in graph[vertex]:
        if color[i] == 0:
            DFS(graph,i,color)

DFS(graph,1,color)
input1.close()
output1.close()