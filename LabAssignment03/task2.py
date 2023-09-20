input1 = open("input2.txt","r")
output1 = open("output2.txt","w")
n = int(input1.readline())
strlist = input1.readline()
list1 = [int(i) for i in strlist.split(" ")]

def Find_max_sum_squared(A,n):
    left = 0
    right = n-1
    max_sum = float('-inf')
    while left < right:
        current_sum = A[left] + A[right] * A[right]
        max_sum = max(max_sum, current_sum)
        if A[left+1] > abs(A[right-1]):
            left += 1
        else:
            right -= 1
    return max_sum
output1.writelines(f"{Find_max_sum_squared(list1,n)}")
input1.close()
output1.close()