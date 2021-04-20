#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 23:11:34 2020

@author: jackal
"""

import numpy as np
import matplotlib.pyplot as plt
%matplotlib auto

import automata_utils as au


initial_automata = au.create_initial_automata(100)

# Select rule (only for 13, 90 and 110)
rule = 90

# Time for evolving process
T = 100

# Evolve inital automata
automata = au.evolve_atutomata(initial_automata, rule, T)


au.display_automata(automata)
