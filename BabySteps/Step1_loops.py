# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 16:46:16 2018

@author: gdiaconu
"""

#using while loop
x= int(input('Enteran integer: '))
ans = 0
while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) + ' is not a perfect cube')
else:
    print('Cuberoot of '+ str(x) + ' is ' + str(ans))
    
    
#using a for loop

for guess in range(abs(x)+1):
    if guess**3 >= abs(x):
        break
if guess**3 != abs(x):
    print(x, "is not a perfect cube")
else:
    if x < 0:
        guess = -guess
        print('Cube root of ' + str(x) + ' is ' + str(guess))