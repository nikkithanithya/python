# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 03:03:06 2022

@author: SPTINT-14
"""
fruits=['mango','apple','orange','cherry']
print(list(filter(lambda fruit: 'g' in fruit, fruits)))
        

fibonacci=[0,1,1,2,3,5,8,13,21,34,55]
odd_numbers=list(filter(lambda x:x % 2,fibonacci))
print ("add numbers",odd_numbers)


fibonacci=[0,1,1,2,3,5,8,13,21,34,55]
even_numbers=list(filter(lambda x:x %2==0,fibonacci))
print ("even numbers",even_numbers)
