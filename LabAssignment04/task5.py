input1=open("input5.txt","r")
output1=open("output5.txt","w")
temp = [int(i) for i in input1.readline().split(" ")]
n = temp[0]
m = temp[1]
d = temp[2]

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, element):
        self.queue.append(element)
    def dequeue(self):
        temp = self.queue[0]
        self.queue = self.queue[1:]
        return temp
    def peek(self):
        if len(self.queue)!=0:
            return self.queue[0]
        else:
            return None

class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent = []
        self.parent = None
        self.distance = 0
        self.color = 0

vertices = {i: Vertex(i) for i in range(1,n+1)}
Q = Queue()
for i in input1:
    u, v = map(int, i.rstrip().split())
    vertices[u].adjacent += [v]
    vertices[v].adjacent += [u]
a = vertices[1]
a.color = 1
Q.enqueue(a)
a = vertices[1]
a.color = 1
Q.enqueue(a)
while Q.peek():
    current = Q.dequeue()
    for v in current.adjacent:
        v = vertices[v]
        if v.color == 0:
            v.color = 1
            v.parent = current
            v.distance += current.distance + 1
            Q.enqueue(v)
    current.color = 2
v = vertices[d]
output1.write(f"Time: {v.distance}\n")
result = [v.value]
while v.parent:
    result.append(v.parent.value)
    v = v.parent
result.reverse()
output1.write("Shortest Path: ")
for i in result:
    output1.write(f"{i} ")
input1.close()
output1.close()