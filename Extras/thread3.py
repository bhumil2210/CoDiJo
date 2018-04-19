import threading
import time
from threading import Timer

'''
class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter'''


def run(name):

    time.sleep(10)
    # Get lock to synchronize threads
    threadLock.acquire()
    #print_time(self.name, self.counter, 3)
    # Free lock to release next thread
    print("Starting ", name)
    print("hello",name)
    print("hi",name)
    threadLock.release()


def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1


def hello():
    print('HI')


def hi():
    print('chal ja')


threadLock = threading.Lock()
threads = []

# Create new threads
#thread1 = myThread(1, "Thread-1", 1)
#thread2 = myThread(2, "Thread-2", 2)
#thread3=Timer(10, )
#thread4=Timer(10, hi)
#thread3.start()
thread3 = threading.Thread(target=run,args=('0',))
thread4 = threading.Thread(target=run,args=('1',))
thread5 = threading.Thread(target=run,args=('2',))
thread6 = threading.Thread(target=run,args=('3',))
#thread4 = threading.Thread(target=run('1'))
#thread5 = threading.Thread(target=run('2'))
#thread6 = threading.Thread(target=run('3'))


# Start new Threads
#thread1.start()
#thread2.start()

thread3.start()
thread4.start()
thread5.start()
thread6.start()

# Add threads to thread list
#threads.append(thread1)
#threads.append(thread2)
threads.append(thread3)
threads.append(thread4)

# Wait for all threads to complete
for t in threads:
    t.join()
print ("Exiting Main Thread")