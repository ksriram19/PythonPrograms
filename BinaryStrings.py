# This an example of Backtracking
# Generate all binary strings with n-bits

def AddBitAtBeginning(x,L):
    return [x + element for element in L]

def BinaryStrings(n):
    if n == 0:
        return []
    if n == 1:
        return ['0','1']
    else:
        return (AddBitAtBeginning('0',BinaryStrings(n-1)) + AddBitAtBeginning('1',BinaryStrings(n-1)))
    
print(BinaryStrings(4)) 

# For k-ary string


