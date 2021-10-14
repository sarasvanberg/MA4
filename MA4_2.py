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
	length = [x for x in range(35)]

	fib_py_time = []

	for i in length:
		ts = time.time()
		fib_py(i)
		fib_py_time.append(time.time() - ts)
	

	f = Integer(5)
	print(f.get())
	f.set(7)
	print(f.get())
	#print(f.fib())

	plt.plot(length, fib_py_time) # do your plotting here
	plt.savefig("fibonacci_timing.png")

 



if __name__ == '__main__':
	main()

def fib_py(n):
    if n <= 1:
        return n
    else:
        return(fib_py(n-1) + fib_py(n-2)) 



