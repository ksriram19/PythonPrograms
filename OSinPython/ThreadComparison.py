import threading
import time

def prime(n):
    primes = [2]
    num = 3
    while len(primes) < n:
        is_prime = True
        for i in range(len(primes)):
            if num % primes[i] == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(num)

        num += 2

    #print(primes)
   


def fibb(n):
    fib = [1,1]
    for i in range(3,n+1):
        fib.append(fib[-1]+fib[-2])
    #print(fib)
    

if __name__ == "__main__":
    t1 = threading.Thread(target=prime,args=(5000,))
    t2 = threading.Thread(target=fibb,args=(5000,))

    start1 = time.time()
    prime(5000)
    #time.sleep(2)
    fibb(5000)
    end1 = time.time()
    print("Execution time without threads: ",(end1-start1)*10**3," ms")

    print("------------------------------")

    start2 = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end2 = time.time()
    print("Execution time with threads: ",(end2-start2)*10**3," ms")
    