#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 00:46:48 2020

@author: jackal
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
%matplotlib auto

rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0

state0 = [1.0, 1.0, 1.0]
t = np.arange(0.0, 40.0, 0.01)

def lorenz(state, t):
    x, y, z = state  # Unpack the state vector
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z  # Derivatives


states = odeint(lorenz, state0, t)



# 3D ATTRACTOS PLOT
fig = plt.figure()
ax = fig.gca(projection="3d")
ax.plot(states[:, 0], states[:, 1], states[:, 2])
plt.draw()
plt.title('Lorenz attractor', fontsize=25)
ax.set_xlabel('x(t)', fontsize=15)
ax.set_ylabel('y(t)', fontsize=15)
ax.set_zlabel('z(t)', fontsize=15)
plt.show()


#  2D PLANE PLOT
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 8), sharex=True)
ax1.plot(states[:,0],states[:,1], 'b', alpha=.25) # XY plane
ax2.plot(states[:,0],states[:,2], 'g', alpha=.25) # XZ plae
ax3.plot(states[:,1],states[:,2], 'r', alpha=.25) # YZ plane 

ax1.set_title("XY Plane", fontsize=25)
ax2.set_title("XZ Plane", fontsize=25)
ax3.set_title("YZ Plane", fontsize=25)

ax1.set_xlabel('X', fontsize=20) 
ax1.set_ylabel('Y',fontsize=20)
ax2.set_xlabel('X', fontsize=20) 
ax2.set_ylabel('Z', fontsize=20) 
ax3.set_xlabel('Y', fontsize=20) 
ax3.set_ylabel('Z', fontsize=20) 

