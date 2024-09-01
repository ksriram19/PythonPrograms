import threading
import time
import random
from collections import deque

# Buffer settings
BUFFER_SIZE = 5
buffer = deque(maxlen=BUFFER_SIZE)

# Semaphores
empty = threading.Semaphore(BUFFER_SIZE)  # Initially, buffer has BUFFER_SIZE empty slots
full = threading.Semaphore(0)  # Initially, buffer has 0 full slots
mutex = threading.Lock()  # Mutex lock for synchronizing access to the buffer

def producer():
    while True:
        item = random.randint(1, 100)  # Produce a random item
        empty.acquire()  # Decrease empty count
        mutex.acquire()  # Lock the buffer
        buffer.append(item)  # Add the item to the buffer
        print(f"Produced {item} | Buffer: {list(buffer)}")
        mutex.release()  # Unlock the buffer
        full.release()  # Increase full count
        time.sleep(random.random())  # Simulate time to produce the item

def consumer():
    while True:
        full.acquire()  # Decrease full count
        mutex.acquire()  # Lock the buffer
        item = buffer.popleft()  # Remove the item from the buffer
        print(f"Consumed {item} | Buffer: {list(buffer)}")
        mutex.release()  # Unlock the buffer
        empty.release()  # Increase empty count
        time.sleep(random.random())  # Simulate time to consume the item

if __name__ == "__main__":
    # Create producer and consumer threads
    producers = [threading.Thread(target=producer) for _ in range(2)]
    consumers = [threading.Thread(target=consumer) for _ in range(2)]

    # Start the producer and consumer threads
    for p in producers:
        p.start()

    for c in consumers:
        c.start()

    # Join the threads
    for p in producers:
        p.join()

    for c in consumers:
        c.join()
