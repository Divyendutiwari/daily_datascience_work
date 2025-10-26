from concurrent.futures import ThreadPoolExecutor
import time
def print_num(number):
    time.sleep(23)
    return number
numbers=[1,3,4,5,6,6]
t=time.time()
with ThreadPoolExecutor(max_workers=7)as executor:
    results=executor.map(print_num,numbers)
for result in results:
    print(result)
print(time.time()-t)