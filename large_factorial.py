import multiprocessing
import time
import math
import sys
sys.set_int_max_str_digits(100000)
def factorial(number):
    print(number)
    result=math.factorial(number)
    print(result)
    return result
if __name__=="__main__":
    numbers=[5,400]
    t=time.time()
    with multiprocessing.Pool() as pool:
        results=pool.map(factorial,numbers)
print(time.time())
