import multiprocessing

def process(num):
  print("processing %s" % num)

for i in range(4):
  p = multiprocessing.Process(target=process, args=(i,))
  p.start()

cpu_num = multiprocessing.cpu_count()
print("CPU number %s" % cpu_num)

for p in multiprocessing.active_children():
  print("child process, name: %s, id: %s" % (p.name, p.pid))




class MyProcess(multiprocessing.Process):
  def __init__(self, loop):
    multiprocessing.Process.__init__(self)
    self.loop = loop

  def run(self):
    for i in range(self.loop):
      print("Pid: %s, loop_index: %s" % (self.pid, i))

for i in range(5):
  p = MyProcess(i)
  # p.daemon = True
  p.start()
  p.join()

print('Main process Ended!')