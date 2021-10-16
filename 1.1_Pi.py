""" 
Student: Sara Svanberg
Mail: Sara.Svanberg.1109@student.uu.se
Reviewed by: Kieran
Date reviewed: 2021-10-15
"""
import random
import math
import matplotlib.pyplot as plt

#1.1 Monte Carlo beräkning av π
def pi_funk(n):
    inC = 0
    for i in range(0, (n)):
        x=(random.uniform(-1.00000, 1.00000))
        y=(random.uniform(-1.00000, 1.00000))
    
        if (x**2 + y**2) <= 1.0:
           inC += 1
           plt.plot(x , y , 'ro')
        else:
          plt.plot(x , y , 'bo')
    pi =4*(inC/int(n))
    real_pi=math.pi

    print ("Estimationen av pi med " + str(n) + " slumpvariabler blev: " + str(pi) + "\n" "Inbyggda konstantes värdet av pi är: " + str(real_pi) +  "\n" "Antalet punkter inne i cirkel: " + str(inC)  )

    plt.show()
    
pi_funk(1000)
pi_funk(10000)
pi_funk(100000)

