# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 17:56:59 2018

@author: gdiaconu

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
 For example, if s = 'azcbobobegghakl', then your program should print
 
Number of times bob occurs is: 2 
"""

testString = "bob"
s = 'azcbobobegghakl'
sumOfBobs = 0
startOfString = 0

while startOfString < len(s):    
    if s[startOfString : startOfString + len(testString)] == testString:        
        sumOfBobs += 1
    startOfString += 1
print("Number of times bob occurs is:", sumOfBobs)
    