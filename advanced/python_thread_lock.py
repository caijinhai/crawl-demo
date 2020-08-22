import threading
import time

class MyThread(threading.Thread):

  def __init__(self, thread_id, name, counter):
    threading.Thread.__init__(self)
    self.thread_id = threading
    self.name = name
    self.counter = counter

  def run(self):
    print ("开始线程：" + self.name)
    thread_lock.acquire()
    print_time(self.name, self.counter, 5)
    thread_lock.release()
    print ("退出线程：" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

thread1 = MyThread(1, 'Thread-1', 1)
thread2 = MyThread(2, 'Thread-2', 2)

thread_lock = threading.Lock()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

