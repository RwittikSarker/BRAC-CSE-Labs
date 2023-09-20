def time_comparision(schedule1, schedule2):
  if schedule1[0] < schedule2[0]:
        return -1
  elif schedule1[0] > schedule2[0]:          
        return 1
  else:
        if schedule1[1] < schedule2[1]:
            return 1
        else:
            return -1
        
def sortSchedules(schedule):
  length=len(schedule)                 
  for i in range(length-1):
    for j in range(length-i-1):
      if time_comparision(schedule[j], schedule[j+1]) > 0:
        schedule[j], schedule[j+1]=schedule[j+1], schedule[j]
  return schedule
        
with open('input4.txt','r') as input1:
  with open('output4.txt','w') as output1:
    schedule = []
    N = int(input1.readline())
    for i in range(N):
      line = input1.readline().split(" ")
      name = line[0]
      location=line[4]
      time = line[6] 
      schedule.append((name, time, location))

    sorted_schedule=sortSchedules(schedule)
    for idx in sorted_schedule:
      name = ''.join(idx[0])
      time = idx[1]
      location=idx[2]
      output1.writelines(f"{name} will departure at {location} {time}")

output = open("output4.txt", "r")
print(output.read())
output.close()