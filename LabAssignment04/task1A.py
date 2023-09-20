input1 = open("input1A.txt","r")
output1 = open("output1A.txt","w")
temp = [int(i) for i in input1.readline().split(" ")]
n = temp[0]
m = temp[1]
matrix = [[0]*(n+1) for i in range(n+1)]
for i in range(0,m):
  temp = input1.readline()
  matrix[int(temp[0])][int(temp[2])] = int(temp[4])
for i in range(n+1):
  for j in range(n+1):
    output1.writelines(f"{matrix[i][j]} ")
  output1.writelines("\n")
input1.close()
output1.close()