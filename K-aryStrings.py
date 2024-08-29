# This an example of Backtracking

def rangeToList(k): 
        result = [] 
        for i in range(0,k): 
            result.append(str(i)) 
        return result 

def KString(n,k):
    if n == 0:
        return []
    if n == 1:
        return (rangeToList(k))
    else:
        return [digit+bitstring for digit in KString(1,k) for bitstring in KString(n-1,k)]

print(KString(4,3))