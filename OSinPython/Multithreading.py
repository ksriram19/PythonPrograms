import threading
import time

def thread1():
    for i in range(0,10):
        time.sleep(1)
        print(f"Task 1: {i}")

def thread2():
    for i in range(0,10):
        time.sleep(10)
        print(f"Task 2: {i}")

if __name__ == "__main__":
    t1 = threading.Thread(target=thread1)  #This is to create an object in thread
    t2 = threading.Thread(target=thread2)

    t1.start()   # Starts the thread
    t2.start() 

    t1.join()   # This function is to tell main thread to wait for completion of t1 thread execution 

    print("Hello World")
