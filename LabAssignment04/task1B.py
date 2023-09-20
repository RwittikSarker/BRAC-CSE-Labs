input1 = open("input1B.txt","r")
output1 = open("output1B.txt","w")
temp = [int(i) for i in input1.readline().split(" ")]
n = temp[0]
m = temp[1]
adjlist = [[] for _ in range(n+1)]
for i in range(0,m):
  temp = input1.readline()
  adjlist[int(temp[0])].append((int(temp[2]),int(temp[4])))
for i in range(0,n+1):
  str1 = ""
  for j in adjlist[i]:
    str1 += str(j) + ","
  output1.writelines(f"{i}:{str1[0:-1]}")
  output1.writelines("\n")
input1.close()
output1.close()