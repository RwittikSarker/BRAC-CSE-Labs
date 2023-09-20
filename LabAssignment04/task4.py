input1=open("input4.txt","r")
output1=open("output4.txt","w")
temp = [int(i) for i in input1.readline().split(" ")]
n = temp[0]
m = temp[1]
lines = [tuple(map(int, input1.readline().split())) for i in range(m)]

def cycle(adjlst,u,v,n):
    u[n] = 1
    v[n] = 1
    for i in adjlst[n]:
        if not u[i]:
            if cycle(adjlst,u,v,i):
                return 1
        elif v[i]:
            return 1
    v[n] = 0
    return 0

def mapcycle(n,lines):
    adjlist = [[] for i in range(n+1)]
    for i, j in lines:
        adjlist[i].append(j)
    u = [0]*(n+1)
    v = [0]*(n+1)
    for n in range(1,n+1):
        if not u[n]:
            if cycle(adjlist,u,v,n):
                return "YES"
    return "NO"

result = mapcycle(n,lines)
output1.write(result)
input1.close()
output1.close()