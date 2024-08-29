# A company is assigned a project to develop an online share trading application. In the application there are two groups of shares i.e. group 1 and group 2. Group1 has N number of shares identified by codes from 0 to (N-1) and group 2 has M number of shares identified by share codes 0 to (M-1). Both groups consist of share positions in the market. The share positions can be similar between the groups and also within the group. The share application must be designed with an algorithm that provides maximum profit to its users at minimum cost by swapping the shares' position in group 1. In one operation, the application swaps the share positions of any two shares in group 1 so that the share position in group 1 with respect to its code becomes unequal to the share position in group 2. The cost of the operation is calculated as the sum of the share codes. For the next similar operation the new share positions in group 1 will be considered. The whole process continues until each share position at group 1 with respect to their code becomes unequal to the share position of group 2. The minimum cost is the sum of all the operations cost incurred while carrying out the whole process.
# Write an algorithm to find the minimum cost.

# Input:
# The first line of input consists of an integer – numGroup1 , representing the total number of shares in group 1 (N).
# The second line consists of N space-separated integers representing the share positions of each code in group 1.
# The third line consists of an integer – numGroup2 , representing the total number of shares in group 2 (M).
# The last line consist of M space-separated integers representing the share positions of each code in group 2.

# Output:
# Print an integer representing the minimum cost. In case of no output print -1.

g1 = []
g2 = []
cost = 0
minimum = 0

# def mincost(index,k):
#     global cost
#     global minimum
#     cost = cost + index + k
#     if cost < minimum:
#         minimum = cost
#     return minimum

n = int(input("Enter the number of stocks: "))
m = n

for i in range(0,n):
    g1.append(int(input("Enter the stock position of g1: ")))

for i in range(0,m):
    g2.append(int(input("Enter the stock position of g2: ")))

minimum = 10000

for i in range(0,n):
    for j in range(0,n):
        if g1[j] == g2[j]:
            c = j
            for k in range(0,n):
                index = c
                if g1[index] != g1[k] and g1[index] != g2[k]: 
                    cost = k + index
                    if cost < minimum:
                        minimum = cost
                        g1[index],g1[k] = g1[k],g1[index]
            

print(cost)

