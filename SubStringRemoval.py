# This program removes a substring from the left and later from the right.
# Here the substring choosen is 01 and each iteration is completed after both side removals
# The time complexity is O(n^2) ie 
# O(n) for traverse and O(1) for deletion ---> O(2n) in total for both sides
# O(n/2) for function call of both filters


X = "01010"
N = list(X)
flag = True
count = 0

def filter1(N):
    for i in range(len(N) - 1):
        if N[i] == '0' and N[i + 1] == '1':
            del N[i:i + 2]  
            return True
    return False

def filter2(N):
    for i in range(len(N) - 1, 0, -1):
        if N[i - 1] == '0' and N[i] == '1':
            del N[i - 1:i + 1]  
            return True
    return False

def iteration(N): 
    global flag,count 
    while flag:
        if filter1(N) and filter2(N):
            count += 1
        else:
            flag = False
    return count

print("Number of iterations:", iteration(N))
