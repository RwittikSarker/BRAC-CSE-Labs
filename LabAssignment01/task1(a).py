with open("input1a.txt", "r") as input1:
  with open("output1a.txt", "w") as output1:
    for i in input1:
      if int(i)%2 == 0:
        output1.writelines(str(int(i)) + " is an Even number\n")
      else:
        output1.writelines(str(int(i)) + " is an Odd number\n")
output = open("output1a.txt", "r")
print(output.read())
output.close()