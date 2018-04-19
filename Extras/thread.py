
import threading

myLock = threading.Lock()

def funcA():
    for i in range(3):
        # Wait until we have the lock - then print - then release the lock
        myLock.acquire(True)
        print('A')
        myLock.release()

def funcB():
    for i in range(2):
        myLock.acquire(True)
        print('B')
        myLock.release()

# Setup a thread for each A and B
threadA = threading.Thread(target=funcA)
threadB = threading.Thread(target=funcB)

# Start running them
threadA.start()
threadB.start()

# Wait for something then print
myLock.acquire(True)
print('Over hear')
myLock.release()