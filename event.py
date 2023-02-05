import threading
import time
import random

# event = threading.Event()
# print(event.__dict__)
# print(event.__dict__['_cond'].__dict__)

threads = []

def func():    
    event = threading.Event()
    t = random.randint(0,3)
    event.wait(t)
    print('complete')
        
def create_thread(function):
    t = threading.Thread(target=function)
    threads.append(t)
        
def start_threads(L):
    for thread in L:              
        print(thread.is_alive())
        print(thread.name)
        thread.start()
        print(thread.is_alive())
        
        
                

# creating threads
for i in range(5):
    create_thread(func)
start_threads(threads)    







# time.sleep(2)
# print('running event')
# event.set()
# print(t1.__dict__)
