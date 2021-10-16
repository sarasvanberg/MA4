#1.3  Parallelprogramering
from time import perf_counter as pc
from time import sleep as pause
import concurrent.futures as future
import random
import time


def hyper_s(n, d):
    #tstart = time.perf_counter()
    lst = [[random.uniform(-1.00000, 1.00000) for i in range(int(d))] for i in range(0, int(n))]

    n_in = 0

    for punkt in lst:
        V1= list(map(lambda x: x**2 , punkt))
        V2 = sum(V1)
        if V2 <= 1:
            n_in += 1
                   
    V = 2**int(d)*(n_in/int(n))
    #tstop =time.perf_counter()
    #print(f"Process for 1 processor took {round(tstop-tstart, 2)} seconds")
    return V
    

#hyper_s(1000000, 11)

            
if __name__ == "__main__":
    start = pc()
    n_lst=[1000000 for x in range(10)]
    d_lst=[11 for x in range(10)] #10 processers
    with future.ProcessPoolExecutor() as ex:

        results = list(ex.map(hyper_s, n_lst, d_lst))
        results = (lambda x, y: x + y / float(len(results)), results)

            
    end = pc()
    print(f"Process for 10 processors took {round(end-start, 2)} seconds")

    start2 = pc()
    n_lst=[10000000 for x in range(1)]
    d_lst=[11 for x in range(1)] #1 processers
    with future.ProcessPoolExecutor() as ex:

        results = list(ex.map(hyper_s, n_lst, d_lst))
        results = (lambda x, y: x + y / float(len(results)), results)

            
    end2 = pc()
    print(f"Process for 1 processors took {round(end2-start2, 2)} seconds")
    
#Time for process with 10 processors took 39.63 seconds
#Time for process with 1 processors took 194.55 min


