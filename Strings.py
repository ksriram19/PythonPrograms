fruit = 'apple'
print(fruit[1])

b = len(fruit)

# To get last letter
print(fruit[b-1])
#OR
print(fruit[-1])

for i in fruit:
    print('a')

# Strings are immutable
str1 = "Sriram"
#str1[0] = "K"

list1 = []
list1 = str1
print(list1)
#list1[0] = "K"

# Slicing 
print(fruit[1:-1])
print(fruit[1:-1])

word = "hi"
count = 0
counts = 0

for letter in word:
    if letter == 's':
        count += 1
print(count)

print(word[1:])

# in operator (returns boolean value)

if word < "banana":
    print(1)


a = "Apple"
for i in a:
    if i < 'l':
        print(i)