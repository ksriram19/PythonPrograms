# This is an example for recursion
# Check whether array is sorted or not

def CheckSort(a):
    #Base case
    if len(a) == 1:
        return True
    return a[0] <= a[1] and CheckSort(a[1:])

A = [122,233,324,311]
print(CheckSort(A))

# Time complexity is O(n) and space complexity is O(n)