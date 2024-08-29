#String 

a = "Hello"
print(a)

#Multiline strings

b = '''Hi
how are you !!
'''
print(b)

c = """"
Hi How do you do
"""
print(c)

# To check a certain phrase in a string
txt = "Hello, Good Morning"
print("Good" in txt)

if "Good" in txt:
    print("Good")

# To check whether it is not in the string
txt2 = "Good Morning"
if "Very" not in txt2:
    print(True)

# Slicing Strings

d = "Hello World"
print(d[2:7])

# Slice from the start
print(d[:5])

#Negative Indexing
print(d[-5:-2])

# Modify Strings
#upper() is to convert to uppercase
#lower() is to convert to lowercase

print(d.upper()) #This only prints but doesnt changes d
print(d.lower())
print(d)

# strip() is used to remove blank spaces at beginning or end
print(d.strip())

# replace() is used to replace a string
print(d.replace("Hel","hEL"))

# split() is used to split string at given character

print(d.split(" "))
print(d.split("o"))

# String Concatenation
e = "Good"
f = "Morning"
print(e+" "+f)

# String Format
name = "Sriram"
txt3 = f"My name is {name}"
# Placeholder ie {} can have a variable,operation,python code
# Modifier is added by : Ex-> .2f for 2 decimal places
price = 45
txt3 = f"The price is {price:.2f}"
txt4 = f"The price is {e+f}"
print(txt3)
print(txt4)

# Escape character
print("The old lady said \"Hello\"")
# \n newline
# \t tab
# \r Carriage return is to return to beginning of the same line

print('Hello Everyone \rI am Sriram')
# \b is for backspace

print("\156")
print("\xFF")
