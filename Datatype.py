# Many datatypes in python

x = frozenset({"apple"})

# Frozenset is immutable
mylist = ['Apple','Mango']
y = frozenset(mylist)
mylist[0] = "Orange"

print(mylist)
y[0] = "Banana"
print(y)

# Buffer Protocol
