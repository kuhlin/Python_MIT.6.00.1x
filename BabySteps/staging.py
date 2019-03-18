# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 15:36:05 2019

@author: gdiaconu
"""

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 