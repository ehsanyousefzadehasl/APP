import threading
import time
import random

def function(i):
    time.sleep(random.randint(1,5))
    print("function called by thread " + str(i))
    return

threads = []
for i in range(5):
    t = threading.Thread(target=function, args=(i,))
    threads.append(t)
    t.start()
    # t.join()