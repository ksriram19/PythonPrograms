# To find the runner up score in the given scores list

n = int(input("Enter the number of elements: "))
arr = list(map(int,input("Enter the elemnts").split()))

arr1 = set(arr)
arr2 = sorted(arr1)

print(arr2[-2])

# input().split() is used to give input in a single line with spaces than a new line

