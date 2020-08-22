from multiprocessing import Process, Lock, Semaphore, Queue
import time

buffer = Queue(10)
empty = Semaphore(2)
full = Semaphore(0)
lock = Lock()


class Consumer(Process):
  def __init__(self):
    Process.__init__(self)

  def run(self):
    while True:
      full.acquire()
      lock.acquire()
      buffer.get()
      print("Consumer one")
      lock.release()
      empty.release()

class Producer(Process):
  def __init__(self):
    Process.__init__(self)
  
  def run(self):
    while True:
      empty.acquire()
      lock.acquire()
      buffer.put(1)
      print("Producer one")
      lock.release()
      full.release()

if __name__ == '__main__':
    p = Producer()
    c = Consumer()
    p.daemon = c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print("End!")
