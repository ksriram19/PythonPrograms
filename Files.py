# Open a file
fhand = open('hello.txt')
print(fhand) # This operation provides the file handle

# File operations are open,close,read,write

n = "Hello\nWorld"
n # In the interpreter this only gives Hello\nWorld 
print(n)

count = 0
for lines in fhand:
    count = count + 1
print(count)
