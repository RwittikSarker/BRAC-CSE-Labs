with open("input3.txt", "r") as input1:
  with open("output3.txt", "w") as output1:
    N = int(input1.readline())
    id = [int(i) for i in input1.readline().split(" ")]
    mark = [int(i) for i in input1.readline().split(" ")]
    sorted_mark = mark.copy()
    sorted_mark.sort(reverse=True)
    indx = []
    for i in sorted_mark:
      for j in range(0,len(mark)):
        if (i == mark[j]) and (j not in indx):
          output1.writelines(f"ID:{id[j]} Mark:{i}\n")
          indx.append(j)
output = open("output3.txt", "r")
print(output.read())
output.close()