# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:36:53 2018

@author: gdiaconu

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. 

For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart. 
If you've spent more than a few hours on this problem, 
we suggest that you move on to a different part of the course.
 If you have time, come back to this problem after you've had a break and cleared your head
"""
s = 'caqcsyapqgbglr'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
lonngestString1 = ""
lonngestString2 = ""
positionInAplhabet1 = 0
positionInAplhabet2 = 0


for testChar in range(len(s)):
    for letter in range(len(alphabet)):
        if s[testChar] == alphabet[letter]:
            positionInAplhabet1 = positionInAplhabet2
            positionInAplhabet2 = letter
            #print("Letra actual:", s[testChar])
            #print("Posicion letra atenrior:", positionInAplhabet1, "Posicion letra actual:", positionInAplhabet2)
            if positionInAplhabet2 >= positionInAplhabet1:
                lonngestString2 += s[testChar]
               #print(lonngestString2)
            elif len(lonngestString2) > len(lonngestString1):
                #print("Reset:",s[testChar])
                lonngestString1 = lonngestString2
                lonngestString2 = s[testChar]
            else:
                lonngestString2 = s[testChar]
                
    
if len(lonngestString2) > len(lonngestString1):
    print("Longest substring in alphabetical order is:", lonngestString2)
else:
    print("Longest substring in alphabetical order is:", lonngestString1)