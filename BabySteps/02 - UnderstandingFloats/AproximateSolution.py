# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 19:08:10 2018

@author: gdiaconu

good enough solution
start with a guess and increment by some small value

|guess3|-cube<= epsilonfor some small epsilon

decreasing increment size -> slower program
increasing epsilon less -> accurate answer
"""

cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses= 0
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num_guesses=', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)