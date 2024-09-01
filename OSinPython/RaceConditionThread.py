# Critical section problem

import threading

count = 0

def task():
    global count
    for i in range(5):
        count += 1

if __name__ == "__main__":
    t1 = threading.Thread(target=task)
    t2 = threading.Thread(target=task)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(count)