# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 18:12:07 2019

@author: gdiaconu

What is the value of the variable count that is printed out (at the print statement) on iteration 0?
What is the value of the variable count that is printed out (at the print statement) on iteration 1?
What is the value of the variable count that is printed out (at the print statement) on iteration 2?
What is the value of the variable count that is printed out (at the print statement) on iteration 3?
What is the value of the variable count that is printed out (at the print statement) on iteration 4?

"""

iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 