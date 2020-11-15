#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:20:25 2020

@author: jackal
"""
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

import itertools
import collections

import netwok_generator_utils as ng
#%%
%matplotlib auto

#%% 
# Parameters
n = 150 # number of nodes
p = 0.1 # probability of edge between two nodes

# Bulid and plot
g = ng.er_netowrk(n, p)
plt.figure()
plt.title(f'Erdös-Renyi Network ({n}, {p})', fontsize=25)
nx.draw(g, with_labels=True) # node_color=<color>
plt.show()

#%%
# Parameters
n = 200 # number of nodes
k = 6 # number of adjacent nodes to form the initial ring
p = 0.1 # probability of re-wire a given edge

# Build and plot
g = ng.ws_netowrk(n, 6, p)
plt.figure()
plt.title(f'Wattson-Strogatz Network ({n}, {k}, {p})', fontsize=25)
nx.draw(g, with_labels=True) # node_color=<color>
plt.show()

#%% - BA_NETWORK_PLOT
# Parameters
n = 300 # number of nodes
n0 = 5 # number of initial nodel to start the network with

# Build and plot
g = ng.ba_netowrk(n0,n)
plt.figure()
plt.title(f'Barabasi-Albert Network', fontsize=25)
nx.draw(g, with_labels=True) # node_color=<color>
plt.show()


