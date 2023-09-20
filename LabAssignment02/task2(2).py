with open("input2(2).txt", "r") as input1:
  with open("output2(2).txt", "w+") as output1:
    N = int(input1.readline())
    strlist1 = input1.readline()
    list1 = [int(i) for i in strlist1.split(" ")]
    M = int(input1.readline())
    strlist2 = input1.readline()
    list2 = [int(i) for i in strlist2.split(" ")]
    merged = []
    lindx = 0
    rindx = 0

    while lindx < len(list1) and rindx < len(list2):
        if list1[lindx] <= list2[rindx]:
            merged.append(list1[lindx])
            lindx += 1
        else:
            merged.append(list2[rindx])
            rindx += 1
    while lindx < len(list1):
        merged.append(list1[lindx])
        lindx += 1
    while rindx < len(list2):
        merged.append(list2[rindx])
        rindx += 1
    output1.writelines(f"{merged}")