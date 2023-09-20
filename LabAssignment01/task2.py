def bubbleSort(arr):
  for i in range(len(arr)-1):
    flag = False
    for j in range(len(arr)-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        flag = True
    if flag == False:
      break
  return arr
#In the best case, the array is already sorted, so if no swapping happens inside the nested loop, flag would remain False and for this, while the second loop would run n times, the parent loop would run only one time making the time complexity θ(n)
with open("input2.txt", "r") as input1:
  with open("output2.txt", "w") as output1:
    num = 0
    for i in input1:
      num += 1
      if num % 3 == 0:
        list1 = [int(j) for j in i.split(" ")]
        list2 = bubbleSort(list1)
        output1.writelines(f"Output {int(num/3)}\n{list2}\n")
output = open("output2.txt", "r")
print(output.read())
output.close()