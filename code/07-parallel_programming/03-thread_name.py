import threading
import time

def first_function():
    print(threading.currentThread().getName() + " is starting!\n")
    time.sleep(2)
    print(threading.currentThread().getName() + " is exiting! \n")
    return


def second_function():
    print(threading.currentThread().getName() + " is starting!\n")
    time.sleep(2)
    print(threading.currentThread().getName() + " is exiting! \n")


def thrid_function():
    print(threading.currentThread().getName() + " is starting!\n")
    time.sleep(2)
    print(threading.currentThread().getName() + " is exiting! \n")


t1 = threading.Thread(name="first_thread", target=first_function)
t2 = threading.Thread(name="second thread", target=second_function)
t3 = threading.Thread(name="third thread", target=thrid_function)

t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()