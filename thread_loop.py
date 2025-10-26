import threading
import time
def print_mumbers():
    
    for i in range(5):
        time.sleep(1)
        print(i)
def print_alphabets():
    
    for i in "abcde":
        time.sleep(1)
        print(i)
t=time.time()
t1=threading.Thread(target=print_mumbers)
t2=threading.Thread(target=print_alphabets)
t1.start()
t2.start()
t1.join()
t2.join()
print(time.time()-t)