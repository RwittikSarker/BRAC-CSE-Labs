input1 = open("input6.txt",'r')
output1 = open("output6.txt",'w')
rows, columns = map(int, input1.readline().rstrip().split())
list1 = []
for line in input1:
    list1.append([i for i in line.rstrip()])

def DFS(i, j):
    global columns, rows
    if i<0 or i>=rows or j<0 or j>=columns:
        return
    elif list1[i][j] == '#':
        return
    else:
        if list1[i][j] == 'D':
            global diamonds
            diamonds+=1
        list1[i][j] = '#'
        DFS(i+1, j)
        DFS(i-1, j)
        DFS(i, j+1)
        DFS(i, j-1)

def floodFill():
    global rows, columns, diamonds
    diamondsArr = []
    for i in range(rows):
        for j in range(columns):
            diamonds = 0
            if list1[i][j] != "#":
                DFS(i, j)
                diamondsArr.append(diamonds)
    return diamondsArr

maxDiamonds = max(floodFill())
output1.write(str(maxDiamonds))
input1.close()
output1.close()