from threading import *
import time

sem = Semaphore(3)

def task(name,i):
    sem.acquire()

    time.sleep(i)
    print(name)
    
    sem.release()

if __name__ == "__main__":
    t1 = Thread(target=task,args=('t1',1,))
    t2 = Thread(target=task,args=('t2',4,))
    t3 = Thread(target=task,args=('t3',2,))
    t4 = Thread(target=task,args=('t4',1,))
    t5 = Thread(target=task,args=('t5',1,))
    
    
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()