# This is a program to find the maximum possible tasks completed in a given time
# Time tiken by a set of tasks is given

t = int(input("Enter the total time: "))
n = int(input("Enter the number of tasks: "))
tasks = []

for i in range(0,n):
    taski = int(input())
    tasks.append(taski)

tasks.sort()
print(tasks)
sum = 0
counttask = 0

for j in range(len(tasks)):
    if sum <= t:
        sum = sum + tasks[j]
        counttask += 1
    
print(counttask-1)