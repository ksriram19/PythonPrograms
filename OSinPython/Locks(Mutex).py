from threading import *

lock = Lock()
count = 0

def task1():
    global count
    lock.acquire()

    for i in range(10):
        count += 1


    lock.release()

if __name__ == "__main__":
    t1 = Thread(target=task1)
    t2 = Thread(target=task1)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    print(count)
