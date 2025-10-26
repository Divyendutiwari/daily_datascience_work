from concurrent.futures import ProcessPoolExecutor
import time
def print_num(number):
    time.sleep(1)
    return number
numbers=[1,3,4,5,6,6]
t=time.time()
if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=5)as executor:
        results=executor.map(print_num,numbers)
    for result in results:
        print(result)
    print(time.time()-t)