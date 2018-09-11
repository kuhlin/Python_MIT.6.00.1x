# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 17:40:10 2018

@author: gdiaconu


Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:
"""

s = 'azcbobobegghakl'
sumOfVowels = 0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' \
    or char == 'o' or char == 'u':
       sumOfVowels += 1
print("Number of vowels:", sumOfVowels)