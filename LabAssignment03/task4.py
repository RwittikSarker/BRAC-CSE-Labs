def Partition(A,low,high):
  x = A[high]
  i = low-1
  for j in range(low,high):
    if A[j]<=x:
      i+=1
      A[i],A[j] = A[j],A[i]
  A[i+1],A[high] = A[high],A[i+1]
  return i+1

def Quick_select(arr,left,right,k):
    if left == right:
        return arr[left]

    pivot_index = Partition(arr,left,right)
    if k == pivot_index + 1:
        return arr[pivot_index]
    elif k < pivot_index + 1:
        return Quick_select(arr,left,pivot_index-1,k)
    else:
        return Quick_select(arr,pivot_index+1,right,k)
    
input1 = open("input4.txt","r")
output1 = open("output4.txt","w")
n = int(input1.readline())
strlist = input1.readline()
list1 = [int(i) for i in strlist.split(" ")]
Q=int(input1.readline())
for i in range(0,Q):
    K = int(input1.readline())
    result = Quick_select(list1,0,n-1,K)
    output1.writelines(f"{result}\n")
input1.close()
output1.close()