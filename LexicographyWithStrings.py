# In python, strings when compared using >,< and other relational operators
# The code does the comparison based on lexicographical order

word = 'apple'

if word < "banana":
    print("The word "+word+" comes before banana")


# String Methods

print(word[::-1]) #Reversal of string

str1 = " Hello World....How are you doing "
y = str1.strip() #To get string with no space at ends

print(str1)
print(y)

# Formatted strings
name = "Suhas"
str2 = f"Hello World...My name is {name}"
print(str2)