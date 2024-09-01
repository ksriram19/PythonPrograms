from threading import *
import time

cond = Condition()
done = 1

def task(name):
    global done
    with cond:
        if done == 1:
            done = 2
            print("Waiting for cond variable: ",name)
            cond.wait()
            print("Condition met: ",name)
            cond.notify_all()
        else:
            for i in range(5):
                print(".")
                time.sleep(1)
            print("Signalling the condition variable: ",name)
            cond.notify_all()
            cond.wait()
            print("Notification Done: ",name) 

if __name__ == "__main__":
    t1 = Thread(target=task,args=('t1',))
    t2 = Thread(target=task,args=('t2',))

    t1.start()
    t2.start()
    t1.join()
    t2.join()