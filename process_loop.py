import multiprocessing
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
if __name__=="__main__":
    p1=multiprocessing.Process(target=print_mumbers)
    p2=multiprocessing.Process(target=print_alphabets)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(time.time()-t)
    

  