import time 
import math


def calculate(func):


    def mycal(*args,**kwargs):
        begin = time.time()
        func(*args,**kwargs)
        end = time.time()
        print("Total time taken in :",func.__name__,end-begin)
    return mycal

@calculate
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))
factorial(0)