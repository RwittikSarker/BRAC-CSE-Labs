with open("input1(1).txt", "r") as input1:
  with open("output1(1).txt", "w+") as output1:
    list1 = [int(i) for i in input1.readline().split(" ")]
    list2 = [int(i) for i in input1.readline().split(" ")]
    flag = False
    for i in range(0,list1[0]):
      for j in range(i+1,list1[0]):
        if list2[i] + list2[j] == list1[1]:
          output1.writelines(f"{i+1} {j+1}")
          flag = True
          break
      if flag == True:
        break
    if flag == False:
      output1.writelines("IMPOSSIBLE")