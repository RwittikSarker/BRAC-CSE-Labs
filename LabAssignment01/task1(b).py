with open("input1b.txt", "r") as input1:
    with open("output1b.txt", "w") as output1:
        j = 0
        for i in input1:
            if j == 0:
                T = int(i)
                j+=1
                continue
            if j > T:
                break
            else:
                j+=1
                list1 = i.split(" ")
                match list1[2]:
                    case "+":
                        result = int(list1[1]) + int(list1[3])
                    case "-":
                        result = int(list1[1]) - int(list1[3])
                    case "*":
                        result = int(list1[1]) * int(list1[3])
                    case "/":
                        result = int(list1[1]) / int(list1[3])
                output1.writelines(f"The result of {list1[1]} {list1[2]} {int(list1[3])} is {result}\n")
output = open("output1b.txt", "r")
print(output.read())
output.close()