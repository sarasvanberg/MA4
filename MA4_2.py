#!/usr/bin/env python3

from integer import Integer
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import sys
import time

def fib_py(n):
    if n <= 1:
        return n
    else:
        return(fib_py(n-1) + fib_py(n-2))
        


def main():
	length = [x for x in range(30, 45)]

	fib_py_time = []
	fib_cpp_time=[]

	for i in length:
		ts = time.time()
		fib_py(i)
		fib_py_time.append(time.time() - ts)
	
	f = Integer(5)
	print(f.get())
	f.set(47)
	print(f.get())
	print(f.fib())
	#f.fib()

	#length2 = [x for x in range(30, 45)]

	for y in length:
		ts = time.time()
		f.fib()
		fib_cpp_time.append(time.time() - ts)


	plt.plot(length, fib_py_time, label="py") # do your plotting here
    plt.plot(length2, fib_cpp_time, label="cpp") # do your plotting here
	plt.legend()
	plt.xlabel("Fibbonacci number")
    plt.ylabel("Time")
	plt.savefig("fibonacci_timing.png")
	
 



if __name__ == '__main__':
	main()




