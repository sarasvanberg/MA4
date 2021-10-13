#!/usr/bin/env python3

from integer import Integer
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import sys

def main():
	f = Integer(5)
	print(f.get())
	f.set(7)
	print(f.get())
	plt.plot([1,2,3],[1,2,3]) # do your plotting here
	plt.savefig("fibonacci_timing.png")

#	for n in range(40, 46):
#		append



if __name__ == '__main__':
	main()

def fib_py(n):
    if n <= 1:
        return n
    else:
        return(fib_py(n-1) + fib_py(n-2)) 

