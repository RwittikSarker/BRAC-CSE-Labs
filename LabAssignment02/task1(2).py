with open("input1(2).txt", "r") as input1:
  with open("output1(2).txt", "w+") as output1:
    list1 = [int(i) for i in input1.readline().split(" ")]
    list2 = [int(i) for i in input1.readline().split(" ")]
    list3 = list2.copy()
    list2.sort()
    u = 1
    v = 0
    j = list2[list1[0]-u]
    i = list2[v]
    flag = False
    for k in range(list1[0]):
      if i+j > list1[1]:
        u = u+1
        j = list2[list1[0]-u]
      elif i+j < list1[1]:
        v = v+1
        i = list2[v]
      else:
        flag = True
        break
    if flag == True:
      for k in range(0,list1[0]):
        if i == list3[k]:
          idx1 = k+1
        if j == list3[k]:
          idx2 = k+1
      output1.writelines(f"{idx2} {idx1}")
    else:
      output1.writelines("IMPOSSIBLE")