#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:19:38 2020

@author: jackal
"""


import numpy as np
import networkx as nx

import itertools
import collections


#%% - ER_NETWORK
def er_netowrk(n: int, p: float):
    '''
    

    Parameters
    ----------
    n : int
        DESCRIPTION.
    p : float
        DESCRIPTION.

    Returns
    -------
    g : TYPE
        DESCRIPTION.

    '''
    g = nx.Graph()
    nodes = [ni for ni in range(n)]
    
    g.add_nodes_from(nodes)
    
    edges = itertools.combinations(range(n), 2)
    for edge in edges:
            prob = np.random.rand()
            if prob < p:
                g.add_edge(*edge)
                
    created_edges = len(g.edges)
    p_of_edges = np.round(created_edges / (n*(n-1)/2), 4)
    
    print(f'Total edges: {created_edges}')
    print(f'Pecentage of edges: {p_of_edges}')
     
    return g


#%% - WS_NETWORK
def ws_netowrk(n: int, k: int, p: float):
    '''
    

    Parameters
    ----------
    n : int
        DESCRIPTION.
    k : int
        DESCRIPTION.
    p : float
        DESCRIPTION.

    Returns
    -------
    g : TYPE
        DESCRIPTION.

    '''
    g = nx.Graph()
    nodes = [ni for ni in range(n)]
    
    for j in range(1, k // 2 + 1): #take up to K/2 nodes (pair)
        # in each iteration we have two coincidences (2*iterations = edges per node)
        targets = nodes[j:] + nodes[0:j]  # first j nodes are now last in list
        #print(nodes)
        #print(targets)
        g.add_edges_from(zip(nodes, targets))
        
    for j in range(1, k // 2 + 1):  # outer loop is neighbors
        targets = nodes[j:] + nodes[0:j]  # first j nodes are now last in list
        # inner loop in node order
        for u, v in zip(nodes, targets):
            
            prob = np.random.rand()
            
            if prob < p:
                w = np.random.choice(nodes)
                # Enforce no self-loops or multiple edges
                while w == u or g.has_edge(u, w):
                    w = np.random.choice(nodes)
                    if g.degree(u) >= n - 1:
                        break  # skip this rewiring
                else:
                    g.remove_edge(u, v)
                    g.add_edge(u, w)
                    
    return g


#%%
    #%% - BA_NETWORK
def ba_netowrk(n0: int, n: int):
    '''
    

    Parameters
    ----------
    n0 : int
        DESCRIPTION.
    n : int
        DESCRIPTION.

    Returns
    -------
    g : TYPE
        DESCRIPTION.

    '''
    
    g = nx.Graph()
    initial_nodes = [ni for ni in range(n0)]
    g.add_nodes_from(initial_nodes)
    
    n_added = n - n0
    added_nodes = np.arange(n0, n, step=1).tolist()
    
    p = np.array([1/g.number_of_nodes() for ni in g.nodes])
    for nj in added_nodes:
        #print('\n',g.degree)
        #print(p)
        selected = np.random.choice(g.nodes, p=p)
        #print(nj, selected)
        g.add_edge(nj,selected)
        p = []
        for i in g.degree:
            p.append(i[1])
        p = np.array(p)
        p = (p+1) / (np.sum(p)+ len(p))

    return g
