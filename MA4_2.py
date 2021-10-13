#!/usr/bin/env python3

from integer import Integer
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def main():
	f = Integer(5)
	print(f.get())
	f.set(7)
	print(f.get())
	plt.plot([1,2,3],[1,2,3]) # do your plotting here
	plt.savefig("fibonacci_timing.png") 

if __name__ == '__main__':
	main()