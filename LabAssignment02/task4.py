def comparison(a, b):
    lindx = 0
    rindx = 0
    result = 0

    while lindx < len(a) and rindx < len(b):
        if a[lindx] <= b[rindx]:
            result = b[rindx]
            lindx += 1
        else:
            result = a[lindx]
            rindx += 1
    while lindx < len(a):
        if a[lindx] >= result:
            result = a[lindx]
        lindx += 1
    while rindx < len(b):
        if b[rindx] >= result:
            result = b[rindx]
        rindx += 1
    return [result]

def divide_and_conquer(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        a1 = divide_and_conquer(arr[:mid])
        a2 = divide_and_conquer(arr[mid:])

        result = comparison(a1, a2)
    return result 
with open("input4.txt", "r") as input1:
  with open("output4.txt", "w+") as output1:
    N = int(input1.readline())
    strlist = input1.readline()
    list1 = [int(i) for i in strlist.split(" ")]
    result = divide_and_conquer(list1)
    output1.writelines(f"{result[0]}")