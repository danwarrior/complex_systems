#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 22:36:54 2020

@author: jackal
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

'''
inputs:
x0 - initial condition
r_min - min value for parameter r
r_max - max value for parameter r
iterations - number of iterations
'''

print 'System arguments:\n'
print 'Initial condition x0:', sys.argv[1]
print 'r interval: from', sys.argv[2], 'to', sys.argv[3]
print 'Number of iterations: ', sys.argv[4], '\n'



def logistic(r,x):
    return r * x * (1 - x)


n = 10000
#iterations = 1000
#r = np.linspace(2.5, 4, n)
#x = 1e-5 * np.ones(n)

def logistic_system():
    
    x0 = float(sys.argv[1])
    iterations = int(sys.argv[4])
    r = np.linspace(float(sys.argv[2]), float(sys.argv[3]), iterations)
    x = np.full(iterations, x0)

    fig, ax = plt.subplots(1, 1, figsize=(12, 9),
                               sharex=True)

    for i in range(iterations):
        
        x = logistic(r, x)
        if i >= (iterations - 100):
            ax.plot(r, x, ',b', alpha=.25)
    ax.set_xlim(r.min(), r.max())
    ax.set_title("Bifurcations (logistic map)")
    ax.set_xlabel('r values') 
    ax.set_ylabel('x values') 
    plt.tight_layout()
    plt.savefig("plot/logistic_plot.png") 
        

if __name__ == '__main__':
    logistic_system()
    print('Figure saved in the path: plot/logistic_plot.png...')




