# Lists
l = [2,3,5,7,11]
print(l)

# Add two more primes
l.append(13)
l.append(17)
print(l)

# Removing 5th prime
i = 5
l.pop(i-1)
print(l)

# Converting a list to a tuple
t = tuple(l)
print(t)

# Inserting 5th prime
l.append(11)
print(l)

#Sort list
l.sort()
print(l)

for j in range(len(l)):
    print(l[j]," ",type(l[j]))

# Total elements
print(len(l))

#
# For 2D list....([0]*columns)*rows

n = int(input("Enter the order: "))
row = col = n

unitmatrix = [[0]*col for _ in range(row)]   # This is to create multiple lists ie like matrix
# unitmatrix = [[0]*col]*row This creates a copy of list   

print("0"*7)
print(type(unitmatrix))
print(unitmatrix)
z = 0
for row in range(n):
    for col in range(n):
        if row == col:
            unitmatrix[row][col] = 1
        else:
            unitmatrix[row][col] = 0

print(unitmatrix)



