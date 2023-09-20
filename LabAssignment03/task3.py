def Quicksort(A,low,high):
  if low<high:
    q = Partition(A,low,high)
    Quicksort(A,low,q-1)
    Quicksort(A,q+1,high)
  return A

def Partition(A,low,high):
  x = A[high]
  i = low-1
  for j in range(low,high):
    if A[j]<=x:
      i+=1
      A[i],A[j] = A[j],A[i]
  A[i+1],A[high] = A[high],A[i+1]
  return i+1

input1 = open("input3.txt","r")
output1 = open("output3.txt","w")
high = int(input1.readline())
strlist = input1.readline()
list1 = [int(i) for i in strlist.split(" ")]
list2 = Quicksort(list1,0,high-1)
str1 = ""
for i in list2:
  str1 = str1 + str(i) + " "
output1.writelines(f"{str1}")
input1.close()
output1.close()
