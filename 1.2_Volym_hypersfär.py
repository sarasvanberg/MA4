#1.2  Approximera volymen av end-dimensionell hypersfär
import random
import math
import functools
import time

n = input('Ange antal slumpvisa koordinater: ')
d = input('Ange antal dimensioner: ')

tstart = time.perf_counter()

lst = [[random.uniform(-1.00000, 1.00000) for i in range(int(d))] for i in range(0, int(n))]

n_in = 0

for punkt in lst:
    V1= list(map(lambda x: x**2 , punkt))
    V2 = sum(V1)
    if V2 <= 1:
        n_in += 1
               
V = 2**int(d)*(n_in/int(n))
tstop =time.perf_counter()

print("Approximation av " + str(d) + "-dimmensionell hypersfär: " + str(V))
r=1    
V_formel=(((float(math.pi))**(int(d)/2))/(math.gamma((int(d)/2)+1)))*r**int(d)
print("Beräknat värde med formel: " + str(V_formel))
print(f"Process took {round(tstop-tstart, 2)} seconds")
