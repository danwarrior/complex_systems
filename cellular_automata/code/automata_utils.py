#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 00:18:04 2020

@author: jackal
"""
import numpy as np
import matplotlib.pyplot as plt

def create_initial_automata(lentgh: int):
    '''
    

    Parameters
    ----------
    lentgh : TYPE
        DESCRIPTION.

    Returns
    -------
    initial_automata : TYPE
        DESCRIPTION.

    '''
    size = int(np.floor(lentgh/3))
    size = size * 3
    half = int((size-1)/2)
    
    center = np.array([1])
    side = np.zeros(half,dtype=int)

    initial_automata = np.concatenate((side, center, side))
    initial_automata = np.expand_dims(initial_automata, axis=0)
    
    return initial_automata
     

   
def define_rule(rule_number):
    '''
    

    Parameters
    ----------
    rule_number : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    
    r = 'r' + str(rule_number)
    print(r)
    
    rules = {
        'r30': {'111':0,
       '110':0,
       '101':0,
       '100':1,
       '011':1,
       '010':1,
       '001':1,
       '000':0},
        
        'r90': {'111':0,
       '110':1,
       '101':0,
       '100':1,
       '011':1,
       '010':0,
       '001':1,
       '000':0},
        
        'r110': {'111':0,
       '110':1,
       '101':1,
       '100':0,
       '011':1,
       '010':1,
       '001':1,
       '000':0}
        
        }
    
    return rules[r], str(rule_number)


def evolve_atutomata(initial_automata, rule, T):
    '''
    

    Parameters
    ----------
    initial_automata : TYPE
        DESCRIPTION.
    T : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    
    automata = initial_automata.copy()
    
    rule, r_number = define_rule(rule)
    
    c1 = np.array([0])
    cn = np.array([0])    
    
    for t in range(T):
        #print(f'Time: {t}')
        step_list = []
        for i in range(automata.shape[1]-2):
            #print('---->')
            #print(automata)
            #print(initial[0][i:3+i].shape)
            window = automata[t][i:3+i].tolist()
            #print(s)
            window_string = ''.join([str(w) for w in window])
            #print(s1)
            mutated_cell = rule[window_string]
            #print(d)
            step_list.append(mutated_cell)
            
        step = np.array(step_list)
        step = np.concatenate((c1,step,cn))
        step = np.expand_dims(step, axis=0)
        
        automata = np.concatenate((automata,step), axis=0)
        
    fig, ax = plt.subplots(1, 1)
    ax.set_title(f'Rule {r_number}', fontsize=25)
    ax.set_xlabel('Automata size', fontsize=15)
    ax.set_ylabel('Time', fontsize=15)
    plt.imshow(automata)
    
    return automata


def display_automata(automata):
    
    fig, ax = plt.subplots(1, 1)
    ax.set_title(f'Rule r_number', fontsize=25)
    ax.set_xlabel('Automata size', fontsize=15)
    ax.set_ylabel('Time', fontsize=15)
    plt.imshow(automata)
    
    
    
