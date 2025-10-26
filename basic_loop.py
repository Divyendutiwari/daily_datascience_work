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
print_mumbers()
print_alphabets()
print(time.time()-t)

        
    