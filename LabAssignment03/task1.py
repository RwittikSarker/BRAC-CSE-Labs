input1 = open("input1.txt","r")
output1 = open("output1.txt","w")
n = int(input1.readline())
arr = [int(a) for a in input1.readline().split(" ")]

def merge(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inversions = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
            inversions += mid - i + 1
        k += 1
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    for i in range(left, right + 1):
        arr[i] = temp[i]
    return inversions

def merge_sort(arr, temp, left, right):
    inversions = 0
    if left < right:
        mid = (left + right) // 2
        inversions += merge_sort(arr, temp, left, mid)
        inversions += merge_sort(arr, temp, mid + 1, right)
        inversions += merge(arr, temp, left, mid, right)
    return inversions

def count_pairs_with_condition(arr):
    n = len(arr)
    temp = [0] * n
    return merge_sort(arr, temp, 0, n - 1)

result = count_pairs_with_condition(arr)
output1.write(str(result))   
input1.close()
output1.close()