
def prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2,n-1):
        if(n%i==0):
            return False
        
    return True

primenum = []

N = int(input())
for i in range(1,N-1):
    if(prime(i)):
        primenum.append(i)

print(primenum[-1])

