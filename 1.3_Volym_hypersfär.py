#1.3  Parallelprogramering
from time import perf_counter as pc
from time import sleep as pause
import concurrent.futures as future
import random


def hyper_s(n, d):
    lst = [[random.uniform(-1.00000, 1.00000) for i in range(int(d))] for i in range(0, int(n))]

    n_in = 0

    for punkt in lst:
        V1= list(map(lambda x: x**2 , punkt))
        V2 = sum(V1)
        if V2 <= 1:
            n_in += 1
                   
    V = 2**int(d)*(n_in/int(n))
    return V

            
if __name__ == "__main__":
    start = pc()
    n_lst=[1000000 for x in range(10)]
    d_lst=[11 for x in range(10)] #10 processers
    with future.ProcessPoolExecutor() as ex:

        results = list(ex.map(hyper_s, n_lst, d_lst))
        results = (lambda x, y: x + y / float(len(results)), results)


#             for r in results:
#                 print(r)
            
    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")


