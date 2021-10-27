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
        
length = [x for x in range(30, 45)]
fib_py_time = []
fib_cpp_time = []

def main():
	
	for i in length:
		ts = time.time()
		fib_py(i)
		fib_py_time.append(time.time() - ts)
	
	#f = Integer(5)
	#print(f.get())
	#f.set(47)
	#print(f.get())
	#print(f.fib())
	#f.fib()


	for i in length:
		ts = time.time()
		f=Integral(i)
		f.fib()
		fib_cpp_time.append(time.time() - ts)


	plt.plot(length, fib_py_time) # do your plotting here
	plt.plot(length, fib_cpp_time) # do your plotting here
	plt.legend("Py CPP")
	plt.xlabel("Fibbonacci number")
	plt.ylabel("Time")
	plt.savefig("fibonacci_timing.png")
	plt.show()
 
#f = Integer(47) blir ett stort negativt tal pga Int overflow, det blir den större
# värde än vad dator kan hantera


if __name__ == '__main__':
	main()




